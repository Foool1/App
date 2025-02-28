from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open('result.png')

result = decode(img)

print(result)
