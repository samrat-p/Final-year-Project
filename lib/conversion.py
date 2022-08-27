import numpy as np
from copy import copy as cpy

def dec_to_bin(val):
    ''' Convert decimal value to binary
    Parameters: val (int): value to convert
    Returns: (str) : binary value of the corrosponding decimal number '''
    return str(bin(val).replace("0b", "")).zfill(8)

def bin_to_dec(val):
    ''' Convert binary value to decimal 
    Parametes: val (int): value to convert
    Returns: (int) : decimal value of the corrosponding binary value '''
    return int(str(val), 2)

def convert_to_255(img):
    ''' Scale a binary image to grayscale level (0-255)
    Parameters: img (numpy array) : source binary image
    Returns: (numpy array) : grayscale image '''
    _img = cpy(img)
    _img[_img==1] = 255
    return np.array(_img, dtype=np.uint8)

def bin_to_gray(img, height, width):
    ''' Convert a binary image to grayscale image
    Parameters : img (numpy array) : original image
                 height (int) : height of the image
                 width (int) : width of the image
    Returns: img (numpy array) : grayscale image '''
    for i in range(height):
        for j in range(width):
            img[i][j] = bin_to_dec(img[i][j])
    return img

def horizontal_adj(img, height, width):
    ''' Returns a horizontal adjacent of the image
    Parameters: img (numpy array): original image
                height (int) : image height
                width (int) : image width 
    Returns: img (numpy array) : horizontal adjacent image of the original image '''
    for i in range(height):
        for j in range(width-1):
            img[i][j] = img[i][j+1]
        if i!=height-1:
            img[i][width-1]=img[i+1][0]
    img[height-1][width-1]=0
    return np.array(img, dtype=np.uint8)

def entropy(pic):
    ''' Calculate entropy of the image
    Parameters: pic (numpy array) : original image
    Returns: e (double): calculated entropy of the image '''
    p =np.array([(pic--v).sum() for v in range (256)])
    p= p/p.sum()
    #compute e= -sum(p(si)*log2(p(si))
    e=-(p*np.log2(p)).sum()
    return e