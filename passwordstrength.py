password = set(input("What is your current password: "))
complexity = 0

def check(chars):
    if len(password.intersection(chars)) > 0:
        global complexity
        complexity += 1
        return True
    else:
        return False

digits = set("0123456789")
if check(digits): print("Your password has digits in. +1 Complexity")    

capitals = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
if check(capitals): print("Your password has capitals in. +1 Complexity")    

lowercase = set("abcdefghijklmnopqrstuvwxyz")
if check(lowercase): print("Your password has lowercases in. +1 Complexity")

print(f"Your final score is {complexity}/3.")
