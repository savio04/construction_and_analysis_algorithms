def getSkyline(buildings):
  if not buildings:
    return []

  events = []
  for xstart, height, xend in buildings:
    events.append((xstart, height, "start"))
    events.append((xend, height, "end"))

  events.sort()  # Ordenando eventos pela coordenada x

  result = []
  heights = [0]  # Lista para rastrear as alturas dos edifícios

  for x, height, event_type in events:
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

  return result

buildings = list()

while True:
  try:
    input_items = input()

    if input_items == "":
        break

    [start, height, end] = input_items.split(" ")

    buildings.append((int(start), int(height), int(end)))
  except EOFError:
    break

result = getSkyline(buildings)

output = ""

# Percorre as tuplas na lista e concatena seus elementos com espaço
for item in result:
  output += f"{item[0]} {item[1]} "

print(output[:-1])