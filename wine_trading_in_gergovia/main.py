output = ""

while True:
  number_tests= int(input())

  if(number_tests == 0):
    break

  numbers = input().split(" ")
  numbers = list(map(int, numbers))
  result = 0

  for index in range(len(numbers)-1):
    current_number = numbers[index]
    next_number = numbers[index+1]
    result += abs(current_number)
    
    current_number += next_number

    numbers[index] = 0
    numbers[index+1] = current_number

  output += f"{result}\n"

print(output[:-1])