def distance(first_point, second_point):
  return (
    (abs(first_point[0] - second_point[0]) ** 2) + 
    (abs(first_point[1] -second_point[1]) ** 2)
  ) ** (1/2)

def prim(graph):
  num_vertices = len(graph)
  chave = [float('inf')] * num_vertices
  pai = [None] * num_vertices
  chave[0] = 0
  conjunto_mst = [False] * num_vertices

  pai[0] = -1

  for _ in range(num_vertices):
    u = min_chave(chave, conjunto_mst)
    conjunto_mst[u] = True

    for v in range(num_vertices):
      if graph[u][v] and not conjunto_mst[v] and chave[v] > graph[u][v]:
        chave[v] = graph[u][v]
        pai[v] = u

  sum = 0

  for i in range(1, len(graph)):
    sum += graph[i][pai[i]]

  return f"{round(sum/100, 2)}" 

def min_chave(chave, conjunto_mst):
  minimo = float('inf')

  for v in range(len(chave)):
    if chave[v] < minimo and not conjunto_mst[v]:
      minimo = chave[v]
      minimo_indice = v
  return minimo_indice

output = ""

input_text = int(input())

for _ in range(input_text):
  input_tests = int(input())

  coodinates = list()

  for index in range(input_tests):
    input_coodinates = input().split(" ")

    x, y = input_coodinates

    coodinates.append((int(x), int(y)))

  total_distance = 0

  graph = list()

  for first_index in range(len(coodinates)):
    line = list()

    for second_index in range(len(coodinates)):
      result_distance = distance(coodinates[first_index], coodinates[second_index])
      line.append(result_distance)
    
    graph.append(line)

  result = prim(graph)
  output += f"{result}\n"

print(output[:-1])