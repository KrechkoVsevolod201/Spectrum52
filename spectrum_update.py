import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

class Spectrum1():
    def run(self):
        file = open('AssistFiles/FileWay1.txt', 'r')
        fileway = file.read()
        print(fileway)
        file.close()
        l = list(fileway)
        size = len(l) - 5
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
        print(len(l))
        filenamecopy1 = ''
        while (size >= 0):
            filenamecopy1 = filenamecopy1 + l[size]
            size -= 1
        print(filenamecopy1)
        # load Image as Grayscale
        i1 = Image.open(fileway).convert("L")
        # convert to numpy array
        n1 = np.array(i1)
        # average columns and rows
        # left to right
        cols1 = n1.mean(axis=0)
        # bottom to top
        rows1 = n1.mean(axis=1)

        # plot histograms
        #plt.plot(cols1)
        #plt.show()
        plt.savefig('Saves/' + filenamecopy1)
        '''
        _______________________________________________________________________
        '''
        file = open('AssistFiles/FileWay2.txt', 'r')
        fileway = file.read()
        print(fileway)
        file.close()
        l = list(fileway)
        size = len(l) - 5
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
        print(len(l))
        filenamecopy2 = ''
        while (size >= 0):
            filenamecopy2 = filenamecopy2 + l[size]
            size -= 1
        print(filenamecopy2)
        # load Image as Grayscale
        i2 = Image.open(fileway).convert("L")
        # convert to numpy array
        n2 = np.array(i2)
        # average columns and rows
        # left to right
        cols2 = n2.mean(axis=0)
        # bottom to top
        rows2 = n2.mean(axis=1)

        # plot histograms
        fig, (ax1, ax2) = plt.subplots(2)
        fig.suptitle('Vertically stacked subplots')
        ax1.plot(cols1)
        ax2.plot(cols2)
        plt.savefig('Saves/' + filenamecopy2)
        plt.show()


if __name__ == '__main__':
    print(__doc__)
    Spectrum1().run()