from algorithm.partition import partition

def select_BFPRT_v2(array, size, groupSize , search):
  # condição de parada
  if(size == 1):
    return array[0]
  
  # Este array guarda a mediana de cada grupo
  candidates = list()

  # Percorrendo o array em intervalos de groupSize
  for index in range(0, size, groupSize):
    #Forma um grupo com "groupSize" elementos ordenados
    group = sorted(array[index:index+groupSize])

    # Pegamos a mediana deste grupo
    newCandidate = group[(len(group) - 1)//2]
    
    # Esse candidato é inserido no array de medianas
    candidates.append(newCandidate)
   
  # Chamamos o algortimo novamente passando o array de medianas e porcurando a mediana deste array
  pivot = select_BFPRT_v2(candidates, len(candidates), groupSize, ((len(candidates)-1)//2) + 1)
  pivotIndex = array.index(pivot)

  # O pivô é colocando no fim do array
  array[pivotIndex], array[size-1] = array[size-1], array[pivotIndex]

  pivotIndex = partition(array, size)

  # Essa é a ordem do elemento, por exemplo se o pivotIndex for 2 significa que esse pivô é o terceiro maior elemento do array
  elementOrder = pivotIndex+1
  
  # Verifica se o pivô encontrado é o z-esimo item que estamos procurando
  if(search == elementOrder):
    return array[pivotIndex]
  
  # Caso o item que estamos procurando seja maior
  if(search > elementOrder):
    # Procuramos na parte superior ao pivô
    newArray = array[(elementOrder):size]
    return select_BFPRT_v2(newArray, len(newArray), groupSize, search - (elementOrder))
  else: # Caso seja menor
    # Procuramos na parte inferior ao pivô
    newArray = array[0:pivotIndex]
    return select_BFPRT_v2(newArray, len(newArray), groupSize, search)