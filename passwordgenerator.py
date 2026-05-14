from random import choice
password = ""

length = int(input("How many characters in the password: "))
possible = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!£$%^&*()\"@"

for i in range(length):
    password += choice(possible)
    
print(password)
