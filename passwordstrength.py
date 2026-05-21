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
capitals = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
lowercase = set("abcdefghijklmnopqrstuvwxyz")
special = set("!£$%^&*?/>.,<#@';:-_")

if check(digits): print("Your password has digits in. +1 Complexity")    
if check(capitals): print("Your password has capitals in. +1 Complexity")    
if check(lowercase): print("Your password has lowercases in. +1 Complexity")
if check(special): print("Your password has Special characters in. +1 Complexity")

print(f"Your final score is {complexity}/4.")
