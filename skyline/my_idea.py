buildings = list() #Armazena todos os prédios

while True:
  try:
    input_items = input()

    if(input_items == ""):
      break
    
    [start, height, end] = input_items.split(" ")

    buildings.append((int(start), int(height), int(end)))
  except EOFError:
    break

def find_group(item, groups): # Econtra o grupo que o prédio pertence
  for group, items in groups.items():
    for tupla in items:
      if item[0]< tupla[0]:
        return group
  return None


groups = {"1": []}
number_of_groups = 0

# Neste laço separamos os prédios em grupos que de prédios de se tocam
for currentBuild in buildings:
  group = find_group(currentBuild, groups)

  start, height, end = currentBuild

  if(group != None):
    groups[group].append((start, height, "start"))
    groups[group].append((end, height, "end"))
  else:
    number_of_groups += 1
    groups[str(number_of_groups)] = [(start, height, "start")]
    groups[str(number_of_groups)].append((end, height, "end"))

result = []
heights = [0]  # Lista para rastrear as alturas dos predios

# Neste laço combinamos os prédios de cada grupo
for key in groups:
  items = groups[key]

  items.sort()

  for item in items:
    x, height, event_type = item

    if event_type == "start":
      heights.append(height)
      max_height = max(heights)
      if not result or max_height != result[-1][1]:
        result.append((x, max_height))
    else:
      heights.remove(height)
      max_height = max(heights)
      if not result or max_height != result[-1][1]:
        result.append((x, max_height))

output = ""

# Percorre as tuplas na lista e concatena seus elementos com espaço
for item in result:
  output += f"{item[0]} {item[1]} "

print(output[:-1])