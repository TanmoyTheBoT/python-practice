# 7. Write a program to find out the line number where python is present from ques 6
from pathlib import Path

file = "file.log"
script_dir = Path(__file__).parent  # Get the directory where the script is located
file_path = script_dir / file  # Construct the full file path

with open(file_path, "r") as f:
    lines = f.readlines()

lineno = 1
for line in lines:

    if("python" in line):
        print(f"Yes python is present.  Line no: {lineno}")
        break
    lineno += 1

else:
    print("No python is not present")
