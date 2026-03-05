print("welcome to the cooler calc") #tells people what the program is

while True: #means the program repeats forever without restarting

    num1 = int(input("enter a num: ")) #sets num1 to an integer which the user enters
    num2 = int(input("enter second num: ")) #sets num2 to an integer which the user enters

    ops = ["+","-","*","/"] #sets the variable ops to a list of the available operations

    for num in range(4): #does the loop four times
        print(num+1,"for",ops[num]) #prints the number in the loop and the corresponding operator

    choice = int(input("\nwhat operation: ")) #asks the user which operation they want to use and converts it to an integer

    match choice: #tells the program what to do depending on the number entered

        case 1:
            print(num1+num2) #adds the two numbers

        case 2:
            print(num1-num2) #subtracts the two numbers

        case 3:
            print(num1*num2) #multiplies the two numbers

        case 4:
            print(num1/num2) #divides the two numbers

        case _:
            print("try again sucker") #if the number entered is invalid it prints this message

    
    print() #prints an extra line to make the output easier to read
