import qrcode

data = 'www.akademiakaszubska.com'

img = qrcode.make(data)

img.save('result.png')
