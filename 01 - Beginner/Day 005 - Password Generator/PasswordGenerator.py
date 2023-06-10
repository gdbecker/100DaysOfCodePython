# 100 Days of Code: Python
# May 5, 2022
# Generate a random password based on number of letters, symbols, and numbers needed

import random

# Variable sets
letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
symbols = list("!#$%&\()*+,-./:;<=>?@")
numbers = list("0123456789")

# Get input
print("Welcome to the Password Generator!!")
numL = int(input("How many letters would you like in your password?\n"))
numS = int(input("How many symbols would you like?\n"))
numN = int(input("How many numbers would you like?\n"))

# Make password
password = []

for l in range(0,numL):
    index = random.randint(0,len(letters) - 1)
    char = letters[index]
    password.append(char)

for s in range(0,numS):
    index = random.randint(0,len(symbols) - 1)
    char = symbols[index]
    password.append(char)

for l in range(0,numN):
    index = random.randint(0,len(numbers) - 1)
    char = numbers[index]
    password.append(char)

random.shuffle(password)

password = ''.join(password)

print(f"Here is your password: {password}")
