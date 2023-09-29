from algorithm.partition_bfprt_algorithm import partition_BFPRT

def select_BFPRT(array, size, search):
  if(size == 1):
    return array[0]
  
  pivotIndex = partition_BFPRT(array, size)

  if(search == pivotIndex+1):
    return array[pivotIndex]
  
  if(search > pivotIndex+1):
    newArray = array[(pivotIndex+1):size]
    return select_BFPRT(newArray, len(newArray), search - (pivotIndex+1))
  else:
    newArray = array[0:pivotIndex]
    return select_BFPRT(newArray, len(newArray), search)