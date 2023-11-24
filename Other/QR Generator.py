import pyqrcode 
from pyqrcode import QRCode 
  
# String which represent the QR code 
s = "https://www.google.com/?authuser=0"
  
# Generate QR code 
url = pyqrcode.create(s) 
  
# Create and save the png file naming "myqr.png" 
url.png("myyoutube.png", scale = 8) 