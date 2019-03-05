#Anena Sims 1001138287
#Lab 1

import numpy as np
import matplotlib.pyplot as plt

#Problem 1: k-means
def problemOne(mean1, mean2, cov):
	x, y, set1 = genGauss2D(mean1, cov)						#Assign the generated sets and coords to variables
	a, b, set2 = genGauss2D(mean2, cov)

	printGraphData(x, y, a, b)								#Graph the data points using coords
	print("Set 1: ")										#Print the arrays of random data to check work
	print(set1)
	print("Set 2: ")
	print(set2)

#Randomly generate the sets of data containing 500 samples using given parameters	
def genGauss2D(mean, cov):										
	sampleData = np.random.multivariate_normal(mean, cov, 500)		#Get 2D array of random data (2col, 500row)
	x, y = sampleData.T 											#Get the x & y coords for each data point to plot
	return(x, y, sampleData)

#Cluster the data 

#Graph the coordinates of the data points for both sets
def printGraphData(x, y, a, b):								
	plt.plot(x, y, '*')							#Set1 is displayed in blue
	plt.plot(a, b, '*')							#Set2 is displayed in orange
	plt.axis('equal')
	plt.show()


#Properties for problem 1 & 2 given by the professor
mean1 = np.array([1, 0])							#Problem 1 first mean property
mean2 = np.array([0, 1.5])							#Problem 1 second mean property
cov = np.array([[0.9, 0.4], [0.4, 0.9]])			#Probelm 1 diagonal covariance. cov1 & cov2 are the same

problemOne(mean1, mean2, cov)




