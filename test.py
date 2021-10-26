import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# load Image as Grayscale
i = Image.open("Files\Risunok_58 first try.jpg").convert("L")
# convert to numpy array
n = np.array(i)
array = []
# average columns and rows
# left to right
cols = n.mean(axis=0)
# bottom to top
rows = n.mean(axis=1)

# plot histograms
f, ax = plt.subplots(2)
ax[0].plot(cols)
ax[1].plot(rows)
#f.show()
f.savefig('Saves\мой график2')

