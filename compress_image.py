import PIL 
from PIL import Image

mywidth=2666
myheight=3332

img=Image.open('1.jpg')
img=img.resize((mywidth,myheight),PIL.Image.ANTIALISAS)
img.save('resize.jpg')