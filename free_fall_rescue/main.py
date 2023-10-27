def distance(first_point, second_point):
  return (
    (abs(first_point[0] - second_point[0]) ** 2) + 
    (abs(first_point[1] -second_point[1]) ** 2)
  ) ** (1/2)

def findMin(line, startIndex):
  if(startIndex == len(line)):
    return 0
  
  min_distance = line[startIndex]

  for index in range(startIndex, len(line)):
    if(line[index] < min_distance):
      min_distance = line[index]
  
  return min_distance

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

  matrix = list()
  for first_index in range(len(coodinates)):
    line = list()
    for second_index in range(len(coodinates)):
      result_distance = distance(coodinates[first_index], coodinates[second_index])
      line.append(result_distance)
    
    min_distance = findMin(line, first_index+1)

    matrix.append(line)
    total_distance += min_distance

  print(matrix)
  total_distance = total_distance/100
  output += f"{round(total_distance, 2)}\n"

print(output)