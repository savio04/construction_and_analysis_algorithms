#Função que calcula a distancia entre dois pontos
def distance(first_point, second_point):
  return (
    (abs(first_point[0] - second_point[0]) ** 2) + 
    (abs(first_point[1] -second_point[1]) ** 2)
  ) ** (1/2)

# Prim
def prim(adj, number):
  #Aqui armazenamos as arestas que ainda não foram visitados
  queue = []

  #Aqui armazenamos os vertices ja visitados
  visited = [False] * number

  #Adicionando o primeiro vertice como não visitado
  queue.append((0,0))
  
  #Aqui armazenamos a soma total das distancias da nossa arvore geradora
  sum = 0

  # Enquanto existir vertices que não analisamos, ou seja, vertices não visitados.
  while queue:

    # Pegamos o vertice de menor distancia
    v, dis = min(queue, key=lambda x: x[1])
    min_index = queue.index((v, dis))

    # Removemos esse vertice da lista
    queue.pop(min_index)

    #Se esse vertice com a menor distancia ja tiver sido visitado, vai para a proxima interação do laço
    if visited[v]:
      continue

    # A distancia é adicionada ao total
    sum += dis

    # Marcamos o vertice como visitado
    visited[v] = True

    # Pecorremos todos os vertices que estão ligados ao vertice (v) que estamos analisando
    for edge in adj[v]:
      new_v = edge[0]

      # Caso essa aresta no ligue a um vertice que ja visitamos, pulamos para a proxima interação
      if visited[new_v]:
        continue
      
      # Adicionamos a lista de arestas ainda não visitados
      queue.append(edge)

  # Retornamos a soma divida por 100
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

    #Armazena as coordenadas de cada pessoa
    coordinates = list()

    #Laço que pega a coordenada de cada pessoa e adiciona na lista "coordinates"
    for index in range(amount_people):
      input_coodinates = input().split(" ")

      x, y = input_coodinates

      coordinates.append((int(x), int(y)))

    #Lista de adjacencia
    adj = [[] for _ in range(amount_people)]

    # Neste laço é preenchido a lista de adjacencias
    for first_index in range(amount_people):
      for second_index in range(amount_people):

        # Aqui calculamos a distancia do vertice analisado(first_index) em relação aos demais (second_index)
        if(first_index != second_index):
          result_distance = distance(coordinates[first_index], coordinates[second_index])
          adj[first_index].append((second_index, result_distance))
    
    #Chama o prim passado a lista de adjacencia e o numero de pessoas/vertices
    result = prim(adj, amount_people)

    #Armazena o resultado final
    output += f"{result}\n"

  print(output[:-1])

# Chamamos a função main
main()