import os
import sys
import socket
import threading
import random
import json
import hashlib
import argparse
import time
from pathlib import Path
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

BUFFER_SIZE = 4096
# This relay server will run on port 8081 (internal)
DEFAULT_PORT = 8081
DEFAULT_RELAY = "127.0.0.1:8081"
WORD_LIST = [
    'alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot',
    'golf', 'hotel', 'india', 'juliet', 'kilo', 'lima',
    'mike', 'november', 'oscar', 'papa', 'quebec', 'romeo',
    'sierra', 'tango', 'uniform', 'victor', 'whiskey', 'xray',
    'yankee', 'zulu'
]

class SecureTransfer:
    def __init__(self, code=None):
        self.code = code or self.generate_code()
        self.salt = os.urandom(16)
        self.iv = os.urandom(16)
        self.key = self.derive_key()

    @staticmethod
    def generate_code(words=3):
        return '-'.join(random.choice(WORD_LIST) for _ in range(words))

    def derive_key(self):
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=self.salt,
            iterations=600000,
        )
        return kdf.derive(self.code.encode())

    def get_cipher(self):
        return Cipher(algorithms.AES(self.key), modes.CTR(self.iv))

class RelayServer:
    def __init__(self, port=DEFAULT_PORT):
        self.port = port
        self.pairs = {}
        self.lock = threading.Lock()
        self.running = False

    def start(self):
        self.running = True
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind(('0.0.0.0', self.port))
            s.listen()
            print(f"⚡ Relay server listening on port {self.port}")
            while self.running:
                conn, addr = s.accept()
                threading.Thread(target=self.handle_connection, args=(conn, addr), daemon=True).start()

    def handle_connection(self, conn, addr):
        try:
            handshake = conn.recv(256).decode().strip()
            if not handshake.startswith("role:"):
                raise ValueError("Invalid handshake format")
            parts = handshake.split(':')
            role, code = parts[1], parts[3]
            with self.lock:
                if code not in self.pairs:
                    self.pairs[code] = {'send': None, 'recv': None}
                self.pairs[code][role] = conn
                pair = self.pairs[code]
                if pair['send'] and pair['recv']:
                    print(f"🔗 Paired connection for code: {code}")
                    self.pipe_connections(pair['send'], pair['recv'])
                    del self.pairs[code]
        except Exception as e:
            print(f"Connection error from {addr}: {str(e)}")
            conn.close()

    @staticmethod
    def pipe_connections(a, b):
        def forward(src, dest):
            try:
                while True:
                    data = src.recv(BUFFER_SIZE)
                    if not data:
                        break
                    dest.sendall(data)
            except Exception:
                pass
            finally:
                src.close()
                dest.close()
        threading.Thread(target=forward, args=(a, b), daemon=True).start()
        threading.Thread(target=forward, args=(b, a), daemon=True).start()

class FileTransfer:
    def __init__(self, relay=DEFAULT_RELAY):
        self.relay_host, self.relay_port = relay.split(':')
        self.relay_port = int(self.relay_port)

    @staticmethod
    def _recv_line(sock):
        data = b""
        while not data.endswith(b'\n'):
            chunk = sock.recv(1)
            if not chunk:
                break
            data += chunk
        return data

    def _file_checksum(self, path):
        hash_md5 = hashlib.md5()
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(BUFFER_SIZE), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()

    def _generate_metadata(self, path):
        path = Path(path)
        if path.is_file():
            return {
                "type": "file",
                "files": [{
                    "relpath": path.name,
                    "size": path.stat().st_size,
                    "checksum": self._file_checksum(path)
                }]
            }
        else:
            base = path
            files = []
            for file in base.rglob('*'):
                if file.is_file():
                    rel = str(file.relative_to(base))
                    files.append({
                        "relpath": rel,
                        "size": file.stat().st_size,
                        "checksum": self._file_checksum(file)
                    })
            files.sort(key=lambda x: x["relpath"])
            return {
                "type": "folder",
                "name": base.name,
                "files": files
            }

    def _send_file(self, sock, cipher, file_path):
        file_path = Path(file_path)
        total_size = file_path.stat().st_size
        bytes_sent = 0
        start_time = time.time()
        with open(file_path, 'rb') as f:
            while True:
                chunk = f.read(BUFFER_SIZE)
                if not chunk:
                    break
                encrypted_chunk = cipher.update(chunk)
                sock.sendall(encrypted_chunk)
                bytes_sent += len(chunk)
                elapsed = time.time() - start_time
                percent = (bytes_sent / total_size) * 100
                speed = bytes_sent / elapsed if elapsed > 0 else 0
                print(f"\rSending {file_path.name}: {bytes_sent}/{total_size} bytes ({percent:.2f}%) at {speed/(1024*1024):.2f} MB/s", end='')
            print()

    def _send_data(self, sock, cipher, path, metadata):
        path = Path(path)
        if metadata["type"] == "file":
            self._send_file(sock, cipher, path)
        else:
            base = path
            for file_info in metadata["files"]:
                full_path = base / file_info["relpath"]
                self._send_file(sock, cipher, full_path)
        remaining = cipher.finalize()
        if remaining:
            sock.sendall(remaining)

    def _receive_file(self, sock, cipher, out_path, file_info):
        out_path.parent.mkdir(parents=True, exist_ok=True)
        total_size = file_info["size"]
        bytes_received = 0
        start_time = time.time()
        with open(out_path, 'wb') as f:
            while bytes_received < total_size:
                to_read = min(BUFFER_SIZE, total_size - bytes_received)
                chunk = sock.recv(to_read)
                if not chunk:
                    raise Exception("Connection closed before file transfer was complete")
                decrypted = cipher.update(chunk)
                f.write(decrypted)
                bytes_received += len(decrypted)
                elapsed = time.time() - start_time
                percent = (bytes_received / total_size) * 100
                speed = bytes_received / elapsed if elapsed > 0 else 0
                print(f"\rReceiving {out_path.name}: {bytes_received}/{total_size} bytes ({percent:.2f}%) at {speed/(1024*1024):.2f} MB/s", end='')
            print()

    def _receive_data(self, sock, cipher, metadata, output_dir):
        output_dir = Path(output_dir)
        if metadata["type"] == "file":
            file_info = metadata["files"][0]
            out_path = output_dir / file_info["relpath"]
            self._receive_file(sock, cipher, out_path, file_info)
        else:
            base_out = output_dir / metadata["name"]
            base_out.mkdir(parents=True, exist_ok=True)
            for file_info in metadata["files"]:
                out_path = base_out / file_info["relpath"]
                self._receive_file(sock, cipher, out_path, file_info)
        try:
            cipher.finalize()
        except Exception:
            pass

    def send(self, path):
        path = Path(path).resolve()
        transfer = SecureTransfer()
        metadata = self._generate_metadata(path)
        if metadata["type"] == "file":
            size = metadata["files"][0]["size"]
            print(f"Sending: {path.name} ({size} bytes)")
        else:
            file_count = len(metadata["files"])
            folder_count = len({Path(f["relpath"]).parent for f in metadata["files"] if Path(f["relpath"]).parent != Path('.')})
            total_size = sum(f["size"] for f in metadata["files"])
            print(f"Sending {file_count} files and {folder_count} folders ({total_size/1024:.1f} kB)")
        print(f"Code is: {transfer.code}\n")
        print(f"py croc.py {transfer.code}\n")
        try:
            with socket.create_connection((self.relay_host, self.relay_port)) as s:
                s.sendall(f"role:send:code:{transfer.code}".ljust(256).encode())
                s.sendall(transfer.salt + transfer.iv)
                meta_json = json.dumps(metadata).encode() + b'\n'
                s.sendall(meta_json)
                ack = s.recv(256).decode().strip()
                if ack != "READY":
                    print("Did not receive READY from receiver. Aborting.")
                    sys.exit(1)
                cipher = transfer.get_cipher().encryptor()
                self._send_data(s, cipher, path, metadata)
                time.sleep(1)
                print("\nTransfer completed successfully ✅")
        except Exception as e:
            print(f"\nTransfer failed: {str(e)}")
            sys.exit(1)

    def receive(self, code, output_dir='.'):
        transfer = SecureTransfer(code)
        try:
            with socket.create_connection((self.relay_host, self.relay_port)) as s:
                s.sendall(f"role:recv:code:{code}".ljust(256).encode())
                salt_iv = s.recv(32)
                transfer.salt, transfer.iv = salt_iv[:16], salt_iv[16:]
                transfer.key = transfer.derive_key()
                meta_line = self._recv_line(s)
                metadata = json.loads(meta_line.decode())
                if metadata["type"] == "folder":
                    file_count = len(metadata["files"])
                    folder_count = len({Path(f["relpath"]).parent for f in metadata["files"] if Path(f["relpath"]).parent != Path('.')})
                    total_size = sum(f["size"] for f in metadata["files"])
                    answer = input(f"Accept {file_count} files and {folder_count} folders ({total_size/1024:.1f} kB)? (Y/n) ")
                    if answer.lower() not in ['y', 'yes', '']:
                        print("Transfer declined.")
                        sys.exit(0)
                else:
                    file_info = metadata["files"][0]
                    total_size = file_info["size"]
                    answer = input(f"Accept file {file_info['relpath']} ({total_size/1024:.1f} kB)? (Y/n) ")
                    if answer.lower() not in ['y', 'yes', '']:
                        print("Transfer declined.")
                        sys.exit(0)
                s.sendall("READY".ljust(256).encode())
                cipher = transfer.get_cipher().decryptor()
                self._receive_data(s, cipher, metadata, output_dir)
                print("\nFiles received successfully ✅")
        except Exception as e:
            print(f"\nReceive failed: {str(e)}")
            sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] not in {"server", "send", "recv"}:
        sys.argv.insert(1, "recv")
        
    parser = argparse.ArgumentParser(description="Secure real-time file transfer (croc-like)")
    subparsers = parser.add_subparsers(dest='command')
    
    server_parser = subparsers.add_parser('server', help='Start relay server (croc relay)')
    server_parser.add_argument('-p', '--port', type=int, default=DEFAULT_PORT)
    
    send_parser = subparsers.add_parser('send', help='Send files or folders in real time')
    send_parser.add_argument('path', help='File or directory to send')
    send_parser.add_argument('-r', '--relay', default=DEFAULT_RELAY)
    
    recv_parser = subparsers.add_parser('recv', help='Receive files')
    recv_parser.add_argument('code', help='Transfer code')
    recv_parser.add_argument('-o', '--output', default='.')
    recv_parser.add_argument('-r', '--relay', default=DEFAULT_RELAY)
    
    args = parser.parse_args()
    
    if args.command == 'server':
        RelayServer(args.port).start()
    elif args.command == 'send':
        ft = FileTransfer(args.relay)
        ft.send(args.path)
    elif args.command == 'recv':
        ft = FileTransfer(args.relay)
        ft.receive(args.code, args.output)
    else:
        parser.print_help()
