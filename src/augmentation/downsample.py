from PIL import Image
import cv2
import scipy.ndimage 
import numpy as np
from matplotlib import pyplot as plt

img = Image.open("../../data/original/image1.jpg") #256x256
img2 = img.resize((int(img.size[0]/2), int(img.size[1]/2)), Image.Resampling.LANCZOS) #128x128
img3 = img2.resize((int(img2.size[0]/2), int(img2.size[1]/2)), Image.Resampling.LANCZOS) #64x64

#upsample back to original
img4 = img3.resize((img.size[0], img.size[1])) #256x256

img3.save("../../data/downsampled/image3.jpg") #save 64x64 image