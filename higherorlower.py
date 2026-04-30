import random

print("Welcome to higher or lower")
print("\nI have thought of a number between 1 and 100")

number = int(random.randint(1,100))
print({number})
while True:
    
    guess = int(input("Make your guess: "))
    
    if guess == number:
        print("Well done you guessed the number {number}")
        break
    
    if guess >> number:
        print("Lower")
    
    if guess << number:
        print("Higher")
