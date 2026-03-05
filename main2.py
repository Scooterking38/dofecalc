print("welcome to the cooler calc")

while True:
    num1 = int(input("enter a num: "))
    num2 = int(input("enter second num: "))

    ops = ["+","-","*","/"]

    for num in range(4):
        print(num+1,"for",ops[num])

    choice = int(input("\nwhat operation: "))

    match choice:

        case 1:
            print(num1+num2)

        case 2:
            print(num1-num2)

        case 3:
            print(num1*num2)

        case 4:
            print(num1/num2)

        case _:
            print("try again sucker")

    
    print()
