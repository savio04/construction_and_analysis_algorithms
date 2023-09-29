def partition_BFPRT(array, size):
  candidates = list()

  for index in range(0, size, 5):
    group = sorted(array[index:index+5])

    newCandidate = group[(len(group) - 1)//2]
    
    candidates.append(newCandidate)

  pivot = sorted(candidates)[(len(candidates)-1)//2]
  pivotIndex = array.index(pivot)
  
  array[pivotIndex], array[size-1] = array[size-1], array[pivotIndex]

  return partition(array, size)


def partition(array, size):
  pivotIndex = size-1
  middle = 0
  
  for index in range(size):
    if(array[index] > array[pivotIndex]):
      array[middle], array[index] = array[index], array[middle]
      middle += 1
    
  array[middle], array[pivotIndex] = array[pivotIndex], array[middle]

  return middle