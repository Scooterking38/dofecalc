print("Welcome to Calculator!")
while True:
    num1 = int(input("Please Enter A Number: "))
    num2 = int(input("Please Enter A Number: "))


    ops = ['+', '-', 'x', '/']

    for number in range(4):
        print(str(number + 1) + " For " + ops[number])
    
    choice = input("\nEnter An Operation: ")
    match choice:
        case "1":
            print(num1 + num2)
  
        case "2":
            print(num1 - num2)

        case "3":
            print(num1 * num2)

        case "4":
            print(num1 / num2)

        case _:
            print("Please try again")
      
    print()
