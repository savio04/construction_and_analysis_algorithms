#Função que calcula a distancia entre dois pontos
def distance(first_point, second_point):
  return (
    (abs(first_point[0] - second_point[0]) ** 2) + 
    (abs(first_point[1] -second_point[1]) ** 2)
  ) ** (1/2)

#Função que verifica se aquela aresta não forma ciclo
def find(parent, i): 
  if parent[i] != i: 
    parent[i] = find(parent, parent[i]) 
  return parent[i] 
  
# Função que faz a união de dois conjuntos
def union(parent, rank, x, y): 
  if rank[x] < rank[y]: 
    parent[x] = y 
  elif rank[x] > rank[y]: 
    parent[y] = x 
  else: 
    parent[y] = x 
    rank[x] += 1

def KruskalMST(graph, V):
  # Aqui armazenamos a arvore geradora minima
  result = [] 

  # Indice para auxiliar nas interções
  i = 0

  # Número de aresta que é atualizando a cada interação
  e = 0

  # Ordena o nosso grafo baseado nas menores arestas (distancias)
  graph = sorted(graph, key=lambda item: item[2]) 

  parent = [] 
  rank = [] 

  for node in range(V): 
    parent.append(node) 
    rank.append(0) 

  # Ficamos nesse laço equanto o número de arestas for menor que V-1 (número de vertices menos um)
  while e < V - 1: 
    u, v, w = graph[i]
    i = i + 1
    x = find(parent, u) 
    y = find(parent, v) 

    if x != y: 
      e = e + 1
      result.append([u, v, w]) 
      union(parent, rank, x, y) 

  sum = 0

  for u, v, weight in result: 
    sum += weight 

  return f"{sum/100:.2f}"

# Função com a logica principal
def main():
  #Quantidade de testes
  input_size = int(input())

  #Armazena a saida
  output = ""

  for _ in range(input_size):
    # Quantidade de pessoas ou número de vertices
    amount_people = int(input())

    # Coordenadas das pessoas
    coordinates = list()

    #Lista de adjacencia
    graph = list()

    #Laço que pega a coordenada de cada pessoa e adiciona na lista "coordinates" ja calculando a distancia entre as pessoas/vetices
    for _ in range(amount_people):
      input_coodinates = input().split(" ")

      x, y = input_coodinates

      coordinates.append((int(x), int(y)))

      if(len(coordinates) > 1):
        last_coordinate = coordinates[len(coordinates) - 1]

        for index in range(len(coordinates) - 1):
          result_distance = distance(coordinates[index], last_coordinate)
          graph.append((index, len(coordinates) - 1, result_distance))

    result = KruskalMST(graph, amount_people)

    #Armazena o resultado final
    output += f"{result}\n"

  #Imprime o resultado
  print(output[:-1])

# Chamamos a função main
main()