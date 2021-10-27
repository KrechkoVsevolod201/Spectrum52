from PIL import Image

class Scale():
    def run(self):
        # read the image
        im = Image.open("Files\Lines.JPG")
        (width1, height1) = im.size
        img = Image.open("Files\Risunok.jpg")
        (width2, height2) = img.size
        a = width1 / width2
        b = height1 / height2
        a = round(a)
        b = round(b)
        print(a, b)
        width2 = width2 * a * 2
        height2 = height2 * b
        # image size
        size = (width2, height2)
        # resize image
        out = img.resize(size)
        # save resized image
        out.save('Saves/resize-output1.png')




if __name__ == '__main__':
    print(__doc__)
    Scale().run()