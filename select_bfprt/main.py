import matplotlib.pyplot as plt
import time
from tqdm import tqdm 
from algorithm.select_bfprt import select_BFPRT_v2
from instance_generator.generate import generate_instance

#Número de instancias
number_instances = 1000000

# Guarda todos os tempos de execução para cada valor de r
times = { "3": [], "5": [], "7": [], "9": [], "11": []}

# Uma nova instancia é gerada e o teste é feito em todos os valores de r
for index in tqdm(range(number_instances), total = number_instances, desc="Executando instancias"):
  # Gerando instancia
  instance = generate_instance()

  x = instance["x"]
  y = instance["y"]
  z = instance["z"]

  # Executando nosso algoritmo modificado que recebe como terceiro parametro um r => {3, 5, 7, 9, 11}
  for r in times.keys():
    start_time = time.time()
    select_BFPRT_v2(x, int(y), int(r), int(z))
    end_time = time.time()

    times[r].append(end_time-start_time)

# Calcule as médias de tempo de execução para cada algoritmo
averages = list()

for r in times.keys():
  average = sum(times[r]) / len(times[r])

  averages.append(average)
  
print("medias", averages)

# Lista de entradas
subtitle = ["Entrada 3", "Entrada 5", "Entrada 7", "Entrada 9", "Entrada 11"]

# Criando gráfico de barras
plt.bar(subtitle, averages)

# Adicione um título ao gráfico
plt.title("Comparação de Tempo Médio para Valores de r")

# Adicione rótulos aos eixos
plt.xlabel("Entrada")
plt.ylabel("Tempo Médio de Execução (s)")

# Mostre o gráfico
plt.show()