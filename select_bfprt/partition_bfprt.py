def partition_BFPRT(array, pivotIndex):
  middle = 0
  
  array[len(array)-1], array[pivotIndex] = array[pivotIndex], array[len(array)-1]

  pivotIndex = len(array)-1

  for index in range(len(array)):
    if(array[index] > array[pivotIndex]):
      array[middle], array[index] = array[index], array[middle]
      middle += 1
    
  array[middle], array[pivotIndex] = array[pivotIndex], array[middle]

  return middle