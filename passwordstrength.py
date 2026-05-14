password = set(input("What is your current password: "))
complexity = 0

def check(chars):
    if len(password.intersection(chars)) > 0:
        complexity += 1
        return True
    else:
        return False

digits = set("0123456789")
if check(digits): print("Your password has digits in. +1 Complexity")    
