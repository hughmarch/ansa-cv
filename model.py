from skimage import io
import numpy as np
import time
import cv2

def ImportTifData(path):
  Data = io.imread(path)
  [n_images, length, width] = np.shape(Data)
  return Data

def centerCrop(data):
  b = 100
  return data[:,b:-b,b:-b]

def averageImg(data, n_frames=10):
  """
  Computes the average of every n_frames times.
  data: the input image stack of shape (n, h, w)
  Returns: resulting average image stack of shape (n / n_frames, h, w)
  """
  [n_images, length, width] = np.shape(data)
  frames = []
  for i in range(0, n_images, n_frames):
    frames.append(np.mean(data[i:i+n_frames], axis=0))
  
  return np.array(frames)

def backgroundSub(Data, n_bg=24):
  """Remove the background utilizng the average of 240 frames  
  Extended Summary: 
  -----------------
  This funciton will take the first 240 frames, average the data, then subtract
  it from the entire data set creating a backgorund removal dataset. 
  Parameters:
  -----------
  Data: numpy.ndarray
        [number of images, number of pixel rows, number of pixel columns]
  Returns:
  --------
    Data_adj: numpy.ndarray
        [number of images, number of pixel rows, number of pixel columns] 
  Example:
  --------
  >>>background(Data)
  
  """
  [n_images, length, width] = np.shape(Data)

  #Define background array 
  background = np.zeros((length, width))

  #Average the entire background data Frame 1-240
  for i in range (0, n_bg):
    background = background + Data[i,:,:]
  background = background / n_bg

  #Subtract the background from entire dataset 
  Data_adj = np.zeros((n_images, length, width))
  for i in range(n_images):
    Data_adj[i,:,:] = Data[i,:,:] - background
  
  return Data_adj.astype(np.int16)

def averageBlur(img):
  """
  Apply a box blurring for denoising.
  img: the input image stack to blur
  Returns the resulting image stack with each image blurred
  """
  return np.array([cv2.blur(i, (5, 5)) for i in img])