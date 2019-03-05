#Anena Sims 1001138287
#Lab 1

import numpy as np
import matplotlib.pyplot as plt
import random
import math


#Randomly generate 2 sets of Gaussian data containing 500 samples using given parameters 
def genGauss2D(mean, cov, numSamples):                                      
    x, y = np.random.multivariate_normal(mean, cov, numSamples).T
    return(x, y)

#Cluster the data 

#Print graph data for problem 1
def printGraphData(set1, set2):                             
    #plt.plot(x, y, '*')                         # This is displayed in blue
    #plt.plot(a, b, '*')                         # This is displayed in orange
    #plt.axis('equal')
    #plt.show()
    plt.plot(set1[:,0], set1[:,1], '.')
    plt.plot(set2[:,0], set2[:,1], '.')


#Properties for problem 1 & 2 given by the professor
numSamples = 500
mean1 = np.array([1, 0])                            #Problem 1 first mean property
mean2 = np.array([0, 1.5])                          #Problem 1 second mean property
cov = np.array([[0.9, 0.4], [0.4, 0.9]])            #Probelm 1 diagonal covariance. cov1 & cov2 are the same

#x, y = genGauss2D(mean1, cov, numSamples)
set1 = genGauss2D(mean1, cov, numSamples)


#a, b = genGauss2D(mean2, cov, numSamples)
set2 = genGauss2D(mean2, cov, numSamples)



printGraphData(set1, set2)
print("Set One: ", set1)
print("Set Two: ", set2)