#Anena Sims 1001138287
#Lab 1

import numpy as np
import matplotlib.pyplot as plt

#Problem 1: k-means
def problemOne(mean1, mean2, cov):
	x1, y1 = genGauss2D(mean1, cov)						#assign the generated sets to variables
	x2, y2 = genGauss2D(mean2, cov)

	printGraphData(x1, y1, x2, y2)						#print the graph data

#Randomly generate 2 sets of data containing 500 samples using given parameters	
def genGauss2D(mean, cov):										
	x, y = np.random.multivariate_normal(mean, cov, 500).T
	return(x, y)

#Cluster the data 

#Print graph data for problem 1
def printGraphData(x1, y1, x2, y2):								
	plt.plot(x1, y1, '*')							# This is displayed in blue
	plt.plot(x2, y2, '*')							# This is displayed in orange
	plt.axis('equal')
	plt.show()


#Properties for problem 1 & 2 given by the professor
mean1 = np.array([1, 0])							#Problem 1 first mean property
mean2 = np.array([0, 1.5])							#Problem 1 second mean property
cov = np.array([[0.9, 0.4], [0.4, 0.9]])			#Probelm 1 diagonal covariance. cov1 & cov2 are the same

problemOne(mean1, mean2, cov)




