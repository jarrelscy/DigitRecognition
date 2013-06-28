'''
Created on 27/06/2013

@author: jarrelscy, justinpoh
'''
import numpy
import scipy
import time
from utils import *



## Please note that you have to download train.csv for this to work duh
#setup file with training csv
dataObject = database("train.csv", max=100)
dataObject.images[2].displayImage()

time.sleep(30) #hack for my poor windows which can't display images without waiting else the temp cache is cleared -.-'
