import random

size_instance = 50000

def generate_instance():
  # Gere valores aleatórios para y e z
  y = size_instance
  z = random.randint(1, size_instance)

  # O tamanho de x será igual a y
  x = [random.randint(1, 5000) for _ in range(y)]

  # Criando um dicionário para representar a instância
  new_instance = {"x": x, "y": y, "z": z}

  return new_instance