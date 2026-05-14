from random import randint

print("Welcome to higher or lower.")
print("\nI have thought of a number between 1 and 100.")
print("You are aiming for the lowest score.")
hscore = False

while True:
    if not hscore:
        print(f"Current best score: {hscore}")
    else:
        print("\nNo score set.")
    
    score = 0
    number = int(randint(1,100))
    
    while True:
        
        guess = int(input("\nMake your guess: "))
        
        if guess == number:
            print(f"\nWell done you guessed the number {number}")
            break
        
        if guess > number:
            print("\nLower")
            score = score + 1
            
        
        if guess < number:
            print("\nHigher")
            score = score + 1
            
        print(f"Your score is: {score}.")
    
    print(f"\nYour final score is: {score}.")
    if score < hscore:
        hscore = score
        print("New High Score!")

    print("\n\n\nNEW ROUND:\n")
    
print(f"Current best score: {hscore}")
