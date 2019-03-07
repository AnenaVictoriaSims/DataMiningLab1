#Anena Sims 1001138287
#Lab 1 - Problem #1

from scipy.stats import multivariate_normal
import numpy as np
import matplotlib.pyplot as plt
import math
import csv
import pandas
import random

numSamples = 10                                     #Problem 1 number of data samples to generate for each data set
centerRows = 0;
comboSampData = [[0 for x in range(2)] for y in range(numSamples*2)]
tableData = [[0 for x in range(7)] for y in range(numSamples*2)]

#----------------------------------------- Generate the random Gaussian data ------------------------------------------#
mean1 = [1, 0]                                            #Problem 1 first mean property
cov1 = [[0.9, 0.4],                                       #Probelm 1 diagonal covariance. cov1 & cov2 are the same
       [0.4, 0.9]]            

mean2 = [0, 1.5]                                          #Problem 1 second mean property
cov2 = [[0.9, 0.4],                                       #Probelm 1 diagonal covariance. cov1 & cov2 are the same
       [0.4, 0.9]]                    
    
x = np.linspace(0, 5, 10, endpoint=False)
y = multivariate_normal.pdf(x, mean1, cov1); y
#array([ 0.00108914,  0.01033349,  0.05946514,  0.20755375,  0.43939129,
       # 0.56418958,  0.43939129,  0.20755375,  0.05946514,  0.01033349])
fig1 = plt.figure()
ax = fig1.add_subplot(111)
ax.plot(x, y)