'''
Created on 27/06/2013

@author: jarrelscy, justinpoh
'''
import numpy
import scipy
import time
from utils import *

def createSVDInputMatrix(dataObject, answer): #creates a matrix of N rows by M columns where M is the number of images with 'answer' as the answer
                                            #and N is the number of pixels in total i.e. 28*28
    ret = []
    for image in dataObject.images:
        if image.answer == answer:
            ret.append(image.returnUnfoldedArray())
    return numpy.array(ret).transpose()
def interpretImage(image): #takes in image of the kind in utils
    print 1
    
## Please note that you have to download train.csv for this to work duh
#setup file with training csv
dataObject = database("train.csv", max=100)
dataObject.images[2].displayImage()
#Using http://www.csc.kth.se/utbildning/kth/kurser/DN2222/nummet2-10/elden.pdf as a reference
#train the matrix
inputMatrix = createSVDInputMatrix(dataObject, 3)
#perform SVD
u,s,v = numpy.linalg.svd(inputMatrix, full_matrices=False)
#do a bit of shifting into space where 255 is best
output =  numpy.abs(u.transpose()[0]) * 1000
#display image output
Image.fromarray(output.reshape((28,28))).show()


time.sleep(30) #hack for my poor windows which can't display images without waiting else the temp cache is cleared -.-'
