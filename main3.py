print("welcome back again\n") #welcomes the user 

while True: #stops printing first message over and over...
    
    num1 = int(input("first num bro: ")) #sets num 1 to the users input
    num2 = int(input("sec num bro: ")) #" " num2 
    
    if num2 == 0:
        print("nah nah\n")
        continue
    
    operator = int(input("\n1 for plus \n2 for minus \n3 for times \n4 for divide: ")) #sets the operator to an integer and asks the user what integer

    match operator: #match case 

        case 1: 
            print(num1 + num2) #adds the first and second number

        case 2:
            print(num1 - num2) #subtracts the first and second number

        case 3:
            print(num1 * num2) #times the first and second number

        case 4:
            print(num1 / num2) #divides the first and second number

        case _:
            print("please try again!") #if a number isnt entered this stops errors 

    print () #ends the while true loop
