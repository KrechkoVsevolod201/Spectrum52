import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

class Spectrum1():
    def run(self):
        file = open('AssistFiles/FileWay2.txt', 'r')
        fileway = file.read()
        print(fileway)
        file.close()
        l = list(fileway)
        size = len(l) - 5
        sizeoffilename = size
        filenamecopy = ''
        slash = "/"
        while (size > 0):
            checkstring = l[size]
            if (checkstring == slash):
                break
            filenamecopy = filenamecopy + l[size]
            size -= 1
        print(filenamecopy)
        l = list(filenamecopy)
        size = len(l) - 1
        sizeofname = size
        print(len(l))
        filenamecopy2 = ''
        while (size >= 0):
            filenamecopy2 = filenamecopy2 + l[size]
            size -= 1
        print(filenamecopy2)
        # load Image as Grayscale
        i = Image.open(fileway).convert("L")
        # convert to numpy array
        n = np.array(i)
        # average columns and rows
        # left to right
        cols = n.mean(axis=0)
        # bottom to top
        rows = n.mean(axis=1)
        print(cols)
        # plot histograms
        plt.plot(cols)
        plt.savefig('Saves/' + filenamecopy2)
        plt.show()


# if __name__ == '__main__':
    # Spectrum().run("Files\Lines HIGHLIGHT.jpg")

if __name__ == '__main__':
    print(__doc__)
    Spectrum1().run()