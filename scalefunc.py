'''
Test function
'''
import math

from PIL import Image
# read the image
im = Image.open("Files\Lines.JPG")
(width1, height1) = im.size
img = Image.open("Files\Risunok_58 first try.jpg")
(width2, height2) = img.size
a = width1/width2
b = height1/height2
a = round(a)
b = round(b)
print(a, b)
width2 = width2 * a * 2
height2 = height2 * b * 2
# image size
size = (width2, height2)
# resize image
out = img.resize(size)
# save resized image
out.save('Saves/resize-output1.png')
