'''
Created on 28/06/2013

@author: jarrelscy justinpoh
'''
import numpy as np
import Image
class image:
    def __init__(self, data, answer):
        self.dataArray =  np.reshape(np.array(data), (28,28))
        self.answer = answer
    def returnUnfoldedArray(self):
        return np.reshape(self.dataArray, (28*28))
    def getPixelAt(self, y, x): #note that its y then x, this is just the python way
        # the arrays look like this: 
        #  [ [0,0,1,0],
        #    [0,1,0,0],
        #    [1,0,0,0] ]
        # 
        return self.dataArray[y][x]
    def displayImage(self):
        Image.fromarray(self.dataArray).show()    
class database:
    '''
    classdocs
    '''
    

    def __init__(self, filename, max=42000):
        '''
        Constructor
        '''
        self.numberOfImages = 0
        f = open(filename, 'r')        
        self.images = [] #this stores all the images
        f.readline() #get rid of first line
        
        for line in f:
            l = map(int, line.split(","))
            answer = l.pop(0) #remove the answer  from the start            
            self.images.append(image(l, answer))
            self.numberOfImages = self.numberOfImages + 1
            if(self.numberOfImages % 100 == 0):
                print self.numberOfImages, 'images have been loaded'
            if(self.numberOfImages > max):
                break
    def displayAnswerOf(self, index):
        print self.images[index].answer
        
        
        
