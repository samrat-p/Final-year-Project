from math import log10, sqrt
import random
import numpy as np

class Noise:
    def __init__(init):
        pass 

    def add_noise(self, img, height, width):          # adding salt paper noise
        number_of_pixels = random.randint(300,(height*width)/2)

        # adding salt noise
        for i in range(number_of_pixels):
            y_coord = random.randint(0,height-1)
            x_coord = random.randint(0,width-1)
            img[x_coord][y_coord] = 255

        number_of_pixels = random.randint(300,(height*width)/2)
        # adding paper noise
        for i in range(number_of_pixels):
            y_coord = random.randint(0,height-1)
            x_coord = random.randint(0,width-1)
            img[x_coord][y_coord] = 0

        return np.array(img, dtype=np.uint8)
    
    def PSNR(self, original, compressed):
        mse = np.mean((original - compressed) ** 2)
        if(mse == 0):   # MSE is zero means no noise is present in the signal .
            return 100
        max_pixel = 255.0
        psnr = 20 * log10(max_pixel / sqrt(mse))
        return psnr