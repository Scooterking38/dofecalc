print("Welcome to Calculator!")
while True:
    num1 = input("Please Enter A Number: ")
    num2 = input("Please Enter A Number: ")
  
    choice = input("\nEnter 1 for Plus, 2 for Minus, 3 for Times: ")
    match choice:
      case "1":
        print(int(num1) + int(num2))
  
      case "2":
        print(int(num1) - int(num2))

      case "3":
        print(int(num1) * int(num2))

      case _:
        print("Please try again")
      
    print()
