 # A Random Bit Generator Using Chaotic Map
# Credit: paper proposed by Narendra K Pareek, Vinod Patidar, and Krishan K Sud, 2007
# Author: suvasish das (misuvasish114@gmail.com)

from conversion import *
import numpy as np

class PRNG:                                   # Pseudo random number generator
    def __init__(self, init, alpha = 0.4):    # constructor
        ''' Pseudo random number generator
        alpha and init value must not same value
        Parameters : alpha (double) : system parameter : default = 0.4
                     init (double) : system parameter '''
        self.alpha = alpha                      # 'alpha' and 'init' are system parameter and initial condition of the map respectively
        self.init = init 
    
    def generate(self):                         # generator class
        ''' Generate a single number in floating point between 0 to 1
        typically generate next value of X(i+1) in the series by using previous value of X(i) and upadate it
        Parameters : None
        Returns : self.init (double) : a random number between 0 to 1 '''
        if self.init > self.alpha:
            self.init = ((1 - self.init)/(1 - self.alpha))
        else:
            self.init = (self.init / self.alpha)
        return self.init 

class CCCBG:                                    # Cross-Coupled Chaotic random Bit Generator
    def __init__(self, x0 = 0.5, y0 = 0.7):     # constractor
        ''' Cross-Coupled Chaotic random Bit Generator 
        two skew tent maps which are piecewise linear chaotic maps and cross-coupled
        Parameters : x0 (double) : initial value of 1st tent map : default = 0.5
                     y0 (double) : initial value of 2nd tent map : default = 0.7 '''
        self.fx = PRNG(init = x0)               # for dynamic system parameters
        self.fy = PRNG(init = y0)
    
    def generateBit(self):                      # single random binary bit generator
        ''' A single random binary bit generator
        Returns: {0,1} : based on the X(i+1) value of the sequence '''
        if self.fx.generate() < self.fy.generate():
            return 1
        return 0
    
    def generateMatrix(self, height, width):    # pseudo random binary matrix generator
        ''' Generate a pseudo random binary matrix of height X width
        Parameters: height (int) : height of the original image
                    width (int) : width of the original image
        Returns: mat (numpy array) : random binary matrix '''
        mat = []                                # height X width binary matrix
        for i in range(height):
            temp = []
            for j in range(width):
                temp.append(self.generateBit())
            mat.append(temp)
        return np.array(mat, dtype=np.uint8)
