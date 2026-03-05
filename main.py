print("Welcome to Calculator!") #tells people what it is
while True: #means that the program will be repeated without restarting forever loop 
    num1 = int(input("Please Enter A Number: ")) #sets num1 to an integer which the user enters
    num2 = int(input("Please Enter A Number: ")) #sets num2 to an integer which the user enters

    ops = ['+', '-', 'x', '/'] #sets the variable ops to a list of the available operations

    for number in range(4): #does it four times
        print(str(number + 1) + " For " + ops[number]) #prints the number in the loop and the corresponding operator
    
    choice = input("\nEnter An Operation: ") #asks the user what operator to use
    match choice: #tells the program what to do with each operator
        case "1":
            print(num1 + num2) #adds the two numbers
  
        case "2":
            print(num1 - num2) #subtracts the two numbers

        case "3":
            print(num1 * num2) #multiplies the two numbers

        case "4":
            print(num1 / num2) #divides the two numbers

        case _:
            print("Please try again") #if the number entered is invalid nothing happens
      
    print() #prints extra line
