import random

print("Welcome to higher or lower.")
print("\nI have thought of a number between 1 and 100.")
print("You are aiming for the lowest score.")
hscore = False

while True:
    if != hscore:
        print(f"Current best score: {hscore}")
    else:
        print("No score set.")
    
    score = 0
    number = int(random.randint(1,100))
    
    while True:
        
        guess = int(input("Make your guess: "))
        
        if guess == number:
            print(f"Well done you guessed the number {number}")
            break
        
        if guess > number:
            print("Lower")
            score = score + 1
            
        
        if guess < number:
            print("Higher")
            score = score + 1
            
        print(f"Your score is: {score}.")
    
    print(f"\nYour final score is: {score}.")
    if score < hscore:
        hscore = score
        print("New High Score!")

    print("\n\n\nNEW ROUND:\n")
    
print(f"Current best score: {hscore}")
