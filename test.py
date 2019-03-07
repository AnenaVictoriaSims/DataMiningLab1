#Anena Sims 1001138287
#Lab 1 - Problem #1

import numpy as np
import matplotlib.pyplot as plt
import math
import csv
import pandas
import random

numSamples = 10                                     #Problem 1 number of data samples to generate for each data set
centerRows = 0;
comboSampData = [[0 for x in range(2)] for y in range(numSamples*2)]
tableData = [[0 for x in range(7)] for y in range(numSamples)]

#----------------------------------------- Generate the random Gaussian data ------------------------------------------#
def genGauss2D(mean1, cov1, mean2, cov2):                    
  x,y = np.random.multivariate_normal(mean1, cov1, numSamples)   #Get 1st set of random data 
  a,b = np.random.multivariate_normal(mean2, cov2, numSamples)   #Get 2nd set of random data
  i = 0
  
  for pair in comboSampData:
    if i >= numSamples:
      i = 0
      pair[0] = sampData2[i][0]
      pair[1] = sampData2[i][1]
    else:
      pair[0] = sampData1[i][0]
      pair[1] = sampData1[i][1]
    i += 1
  
  print(sampData1)
  return comboSampData, sampData1, sampData2

#-------------------------------------- Print all calculated data  -------------------------------------#
def printAllData(D, iteration, k, clusters, priorClusters):
  if iteration == 1:
    print("Original Center Points. No Data Table Yet...")
    print("Starting Center Points: ",priorClusters,)
    print()
  else:
    print("Table Data for iteration #", iteration, " with k = ", k)
    for row in tableData:
      print(row)
    print("Old Center Points: ",priorClusters," New Center Points: ",clusters)
    print()
  
  title = "Iteration #"+str(iteration)+" k = "+str(k)
  if centerRows == 2:
    cntrx1, cntry1, cntrx2, cntry2 = clusters[0][0], clusters[0][1], clusters[1][0], clusters[1][1];
    plt.plot(cntrx1, cntry1, cntrx2, cntry2, marker='X', color='r')
    plt.title(title)
    #plt.xlim(-10,10)
    #plt.ylim(-10,10)
    plt.scatter(D[:,0],D[:,1])
    #plt.scatter(set2[:,0],set2[:,1])
    plt.show()
  if centerRows == 4:
    cntrx1, cntry1, cntrx2, cntry2 = clusters[0][0], clusters[0][1], clusters[1][0], clusters[1][1];
    cntrx3, cntry3, cntrx4, cntry4 = clusters[2][0], clusters[2][1], clusters[3][0], clusters[3][1];
    plt.plot(cntrx1, cntry1, cntrx2, cntry2, cntrx3, cntry3, cntrx4, cntry4, marker='X', color='r') 
    plt.title(title)
    #plt.xlim(-10,10)
    #plt.ylim(-10,10)
    plt.scatter(D[:,0],D[:,1])
    #plt.scatter(set2[:,0],set2[:,1])
    plt.show()

#---------------------------------------------- Cluster the given data ------------------------------------------------#
def mykmeans(X, k, c):
  i, count = 0, 0;

  for pair in X:
    num = 1
    while num <= centerRows:
      a, b = c[num-1][0], c[num-1][1];
      x, y = pair[0], pair[1];
      tableData[i][0], tableData[i][1] = x, y;
      getEuclideanDistance(count, num, k, x, y, a, b)   #Get the centroid for first center
      num += 1
    count += 1
    i += 1

  assignCluster(k)
  centers = deriveNewCenters(X, k)
  return centers

#--------------------------------------------- Find Euclidean Distances -----------------------------------------------#
def getEuclideanDistance(count, i, k, x, y, a, b):                         
  tableData[count][i+1] = round(math.sqrt(pow((x-a),2) + pow((y-b),2)), 2)  

#---------------------------------------------- Assign a cluser value -------------------------------------------------#
def assignCluster(k):
  i = 0

  for val in tableData:
    if k == 2:
      if (min(tableData[i][2],tableData[i][3])) == tableData[i][2]:
        tableData[i][6] = 1
      else:
        tableData[i][6] = 2
    elif k == 4:
      if (min(tableData[i][2],tableData[i][3],tableData[i][4],tableData[i][5])) == tableData[i][2]:
        tableData[i][6] = 1
      elif (min(tableData[i][2],tableData[i][3],tableData[i][4],tableData[i][5])) == tableData[i][3]:
        tableData[i][6] = 2
      elif (min(tableData[i][2],tableData[i][3],tableData[i][4],tableData[i][5])) == tableData[i][4]:
        tableData[i][6] = 3
      else:
        tableData[i][6] = 4
    i += 1

#------------------------------------------------- Find New Centers --------------------------------------------------#    
def deriveNewCenters(X, k):
  count, xMean, yMean = 0, 0, 0;
  newCenters = [[0 for x in range(2)] for y in range(centerRows)]  

  for row in tableData:
    if row[6] == 1:
      xMean = row[0] + xMean
      yMean = row[1] + yMean  
      count += 1
  if count != 0:
    newCenters[0][0] = round((xMean/count), 2)
    newCenters[0][1] = round((yMean/count), 2)    
    count, xMean, yMean = 0, 0, 0;
  
  for row in tableData:
    if row[6] == 2:
      xMean = row[0] + xMean
      yMean = row[1] + yMean  
      count += 1     
  if count != 0:
    newCenters[1][0] = round((xMean/count), 2)
    newCenters[1][1] = round((yMean/count), 2)
    count, xMean, yMean = 0, 0, 0;

  if k == 4:
    for row in tableData:
      if row[6] == 3:
        xMean = row[0] + xMean
        yMean = row[1] + yMean  
        count += 1     
    if count != 0:
      newCenters[2][0] = round((xMean/count), 2)
      newCenters[2][1] = round((yMean/count), 2)
      count, xMean, yMean = 0, 0, 0;

    for row in tableData:
      if row[6] == 4:
        xMean = row[0] + xMean
        yMean = row[1] + yMean  
        count += 1  
    if count != 0:   
      newCenters[3][0] = round((xMean/count), 2)
      newCenters[3][1] = round((yMean/count), 2)

  return newCenters

#------------------------------------------------- Main for Problem 1 -------------------------------------------------#
mean1 = [1, 0]                                            #Problem 1 first mean property
cov1 = [[0.9, 0.4],                                       #Probelm 1 diagonal covariance. cov1 & cov2 are the same
       [0.4, 0.9]]            

mean2 = [0, 1.5]                                          #Problem 1 second mean property
cov2 = [[0.9, 0.4],                                       #Probelm 1 diagonal covariance. cov1 & cov2 are the same
       [0.4, 0.9]]   

X, D = genGauss2D(mean1, cov1, mean2, cov2)      #Getting the random data & combining it into one large array

#D = np.array([[5,3], [10,15], [15,12], [24,10], [30,45], [85,70], [71,80], [60,78], [55,52], [80,91]])

#2. Call the mykmeans() function with k = 2 and given 2 center points c1 -----------------------------------------------
iteration = 0
c1 = [[10, 10],                                        #Initial center values given by prof.
      [-10, -10]]
centerRows = len(c1)
k = 2
priorClusters = c1
printAllData(D, iteration, k, c1, priorClusters) 
while iteration < 10000:
  iteration += 1
  clusters = mykmeans(D, k, c1)              #Get new center points
  printAllData(D, iteration, k, clusters, priorClusters)
  i, term = 0, False;

  while i < centerRows:
    if clusters[i][0] == priorClusters[i][0]:
      if clusters[i][1] == priorClusters[i][1]:
        term = True
        break
    i += 1
  if term == True:
    print("L2-norm between prior center and current <= 0.001")
    print()
    break
  else:
    priorClusters = clusters
    c1 = clusters 

#3. Call the mykmeans() function with k = 4 and given 4 center points c2------------------------------------------------
iteration = 0
c2 = [[10,10],
      [-10, -10],
      [10, -10],
      [-10, 10]]
centerRows = len(c2)
k = 4
priorClusters = c2 
printAllData(D, iteration, k, c2, priorClusters) 
while iteration < 10000:
  iteration += 1
  clusters = mykmeans(D, k, c2)              #Get new center points
  printAllData(D, iteration, k, clusters, priorClusters)
  i, term = 0, False;

  while i < centerRows:
    if clusters[i][0] == priorClusters[i][0]:
      if clusters[i][1] == priorClusters[i][1]:
        term = True
        break
    i += 1
  if term == True:
    print("L2-norm between prior center and current <= 0.001")
    print()
    break
  else:
    priorClusters = clusters
    c2 = clusters 
    



