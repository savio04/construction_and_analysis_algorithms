#Função que calcula a distancia entre dois pontos
def distance(first_point, second_point):
  return (
    (abs(first_point[0] - second_point[0]) ** 2) + 
    (abs(first_point[1] -second_point[1]) ** 2)
  ) ** (1/2)

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
    for _ in range(amount_people):
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
    
    print("adj", adj)
    #Chama o prim passado a lista de adjacencia e o numero de pessoas/vertices
    # result = prim(adj, amount_people)

    #Armazena o resultado final
    # output += f"{result}\n"

  # print(output[:-1])

# Chamamos a função main
main()