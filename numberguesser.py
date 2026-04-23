import random

while True:

    print ("\nWelcome to the number guessing game")
    number = random.randint(0,10)
    print("\nI have thought of a number between 1 and 10")
    guess = int(input("Guess my number: "))
    
    if guess == number:
        print("Well done you were right!")
        
    else:
        print(f"\n\nYou were wrong the answer was {number}.")
        
