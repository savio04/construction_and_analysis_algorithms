output = ""

while True:
  number_tests= int(input())

  if(number_tests == 0):
    break

  items_dict = {}
  number_of_pairs = 0

  for index in range(number_tests):
    start, end = input().split(" ")
    position_search = (end,start)

    if position_search in items_dict:
      number_of_pairs += 1
      del items_dict[position_search]
    else:
      items_dict[(start,end)] = (int(start), int(end))

  if((number_of_pairs*2) == number_tests):
    # print("YES\n")
    output += f"YES\n"
  else:
    # print("NO\n")
    output += f"NO\n"

print(output)