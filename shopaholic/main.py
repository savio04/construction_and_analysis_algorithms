def checkDiscount(items):
  items.sort(reverse=True)
  discount = 0

  for index in range(0, len(items), 3):
    start, end = index, min(index + 3, len(items))
    newGroup = items[start:end]
    
    if(len(newGroup) == 3):
      discount += newGroup[-1]

  print(discount)

number_tests= int(input())

for index in range(number_tests):
  number_items = input()
  items = input().split(" ")
  items = list(map(int, items))
  checkDiscount(items)