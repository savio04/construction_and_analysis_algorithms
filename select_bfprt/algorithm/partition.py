def partition(array, size):
  # Pega como pivo o ultimo item do array
  pivotIndex = size-1

  # Inicia a variabel middle que vai ser onde o pivô vai ter que ficar no fum do laço
  middle = 0
  
  for index in range(size):
    if(array[index] > array[pivotIndex]):
      array[middle], array[index] = array[index], array[middle]
      middle += 1
    
  array[middle], array[pivotIndex] = array[pivotIndex], array[middle]

  return middle