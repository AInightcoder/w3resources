def sortarraylittletobig(array):
  for i in range(len(array)):
    midindex=i
    for j in range( midindex, len(array)):
      if array[j]<array[midindex]:
        midindex=j
    (array[i], array[midindex])=(array[midindex], array[i])  

arr =[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
sortarraylittletobig(arr)
print(arr)
