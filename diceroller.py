import random
while True:
  print("Welcome to the dice roller!")

  sides = input("How many sides: ")
  if sides == 0:
    print("0")
    break

  if sides.isalpha():
    print("Please try again later!")
    break
    
  number = random.randint(1,int(sides))
  print(number)
