# 100 Days of Code: Python
# May 9, 2022
# Calculator app with four main operations to select from

# One function to handle four main operations
def calculate(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2

# Set up variables and loop through as long as they want to keep calculating
keepGoing = True
startOver = True

print('''
             _____________________
            |  _________________  |
            | |              0. | |
            | |_________________| |
            |  ___ ___ ___   ___  |
            | | 7 | 8 | 9 | | + | |
            | |___|___|___| |___| |
            | | 4 | 5 | 6 | | - | |
            | |___|___|___| |___| |
            | | 1 | 2 | 3 | | x | |
            | |___|___|___| |___| |
            | | . | 0 | = | | / | |
            | |___|___|___| |___| |
            |_____________________|
''')
print("*/-+ Welcome to the CALCULATOR +-\*")

while keepGoing:
    if startOver == True:
        num1 = float(input("What is the first number? "))
    print("+\n-\n*\n/")
    operation = input("Select an operation: ")
    num2 = float(input("What is the second number? "))

    result = calculate(num1, num2, operation)

    print(f"{num1} {operation} {num2} = {result}")

    answer = input(f"Type 'y' to continue calculating with {result}, 'n' to start a new calculation, 'leave' to exit the app. ")

    if answer == "y":
        startOver = False
        num1 = result
    elif answer == "n":
        startOver = True
    elif answer == "leave":
        keepGoing = False
