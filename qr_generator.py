import pyqrcode

content="enter content here"
url=pyqrcode.create(content)
url.png("myqr.png",scale=5)
print("QR code is generated")