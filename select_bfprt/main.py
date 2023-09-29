import json
from tqdm import tqdm 
from algorithm.select_bfprt_algorithm import select_BFPRT

# Lista para armazenar as tuplas lidas do arquivo
tuplas = []

# Nome do arquivo JSON
nome_arquivo_json = "instances/instances.jsonl"

# Descubra o número total de linhas no arquivo (opcional, mas útil)
with open(nome_arquivo_json, "r") as arquivo_json:
  num_linhas = sum(1 for _ in arquivo_json)


# Abra o arquivo JSON para leitura
with open(nome_arquivo_json, "r") as arquivo_json:
  #Conforme vamos lendo as linhas do arquivo vamos processando
  for line in tqdm(arquivo_json, total=num_linhas, desc="Executando instancias"):
    instance = json.loads(line)

    x = instance["x"]
    y = instance["y"]
    z = instance["z"]

    select_BFPRT(x, int(y), int(z))