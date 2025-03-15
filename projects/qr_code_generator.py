# QR Code Generator
# Write a program to generate a QR code based on user input, such as text or a
# URL. The QR code should be saved as an image file that can be scanned with a
# smartphone.

# Optional Enhancements
# • Add options for the user to choose the color of the QR code. This will allow
# users to generate QR codes that match their style or branding.
# • Implement a feature that lets the user generate multiple QR codes at once by
# providing a list of URLs or texts. Each QR code should be saved with a unique
# filename. 

import qrcode
data = input('Enter the text or URL: ').strip()
filename = input('Enter the filename without extension: ').strip()
img = qrcode.make(data)
type(img)
img.save(f"{filename}.png")
print(f'QR code saved as {filename}.png')