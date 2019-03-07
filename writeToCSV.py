#2. Call the mykmeans() function with k = 2 and given 2 center points c1 -----------------------------------------------
iteration = 1
c1 = [[5, 3],                                        #Initial center values given by prof.
     [10, 15]]
centerRows = len(c1)
k = 2
priorClusters = [[0 for x in range(2)] for y in range(centerRows)]  
while iteration < 10000:
  clusters = mykmeans(D, k, c1)              #Get new center points
  printAllData(D, iteration, k, clusters)
  i, term = 0, False;

  while i < centerRows:
    if clusters[i][0] - priorClusters[i][0] <= 0.001:
      if clusters[i][1] - priorClusters[i][1] <= 0.001:
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
    iteration += 1

#3. Call the mykmeans() function with k = 4 and given 4 center points c2------------------------------------------------
iteration = 1
c2 = [[5,3],
      [10, 15],
      [10, -10],
      [-10, 10]]
centerRows = len(c2)
k = 4
priorClusters = [[0 for x in range(2)] for y in range(centerRows)]  
while iteration < 10000:
  clusters = mykmeans(D, k, c2)              #Get new center points
  printAllData(D, iteration, k, clusters)
  i, term = 0, False;

  while i < centerRows:
    if clusters[i][0] - priorClusters[i][0] <= 0.001:
      if clusters[i][1] - priorClusters[i][1] <= 0.001:
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
    iteration += 1