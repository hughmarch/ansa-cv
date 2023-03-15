from skimage import io
import numpy as np
import time

def ImportTifData(path):
  Data = io.imread(path)
  [n_images, length, width] = np.shape(Data)
  return Data