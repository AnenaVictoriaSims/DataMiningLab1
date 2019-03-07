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