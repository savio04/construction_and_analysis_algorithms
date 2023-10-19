output = ""

while True:
  try:
    input_text = input()
    result = list()

    if(input_text == ""):
      break
    
    variableS, variableT = input_text.split(" ")

    variableS = [*variableS]
    variableT = [*variableT]

    current_position = 0

    for letter in variableT:
      if(current_position > len(variableS) -1):
        break

      if(letter == variableS[current_position]):
        result.append(letter)
        current_position += 1
    
    if(len(result) == len(variableS)):
      output += f"Yes\n"
    else:
      output += f"No\n"

  except EOFError:
    break

print(output[:-1])