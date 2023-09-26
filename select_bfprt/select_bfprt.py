from partition_bfprt import partition_BFPRT

def select_pivot(array, start, end):
  candidates= list()
  fraction = list()

  if(start == end):
    return array[start]

  for index in range(start, end, 5):
    indexEnd = index + min(5, end-index)
    
    fraction = sorted(array[index:indexEnd])

    pivot = fraction[(len(fraction)-1)//2]

    candidates.append(pivot)

  return select_pivot(candidates, 0, len(candidates)-1)

def select_BFPRT(array, start, end, search):
  if(start == end):
    return array[start]
  
  pivot = select_pivot(array, start, end)
  pivotIndex = array.index(pivot)

  pivotIndex = partition_BFPRT(array, pivotIndex)

  if(search == pivotIndex+1):
    return array[pivotIndex]
  
  if(search > pivotIndex+1):
    return select_BFPRT(array, pivotIndex+1, end, search)
  else:
    return select_BFPRT(array, start, pivotIndex -1, search)