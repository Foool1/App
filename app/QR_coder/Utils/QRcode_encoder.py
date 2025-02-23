from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open('image.png')

result = decode(img)

print(result)