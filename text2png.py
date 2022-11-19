# Using csdt_stl_tools' guide for converting text to png. https://pypi.org/project/csdt-stl-tools/

import os
from csdt_stl_tools import numpy2stl, text2png, text2array
from imread import imread
from scipy.ndimage import gaussian_filter

text = "$test$"
os.system("cd /srv")
text2png(text, "Test", fontsize=50)  # save png

A = imread("Test.png")  # read from rendered png
A = A.mean(axis=2)  # grayscale projection
A = gaussian_filter(A.max() - A, 1.)

numpy2stl(A, "Test.stl", scale=0.2,
          mask_val=5.)
