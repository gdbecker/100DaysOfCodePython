# 100 Days of Code: Python
# May 11, 2022
# Digital version of a coffee machine! Order and make drinks, print status, give change (without OOP structure)

# Coffee Machine data
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

logo = '''
        /~~~~~~~~~~~~~~~~~~~/|
       /              /######/ / |
      /              /______/ /  |
     ========================= /||
     |_______________________|/ ||
      |  \****/     \__,,__/    ||
      |===\**/       __,,__     ||
      |______________\====/%____||
      |   ___        /~~~~\ %  / |
     _|  |===|===   /      \%_/  |
    | |  |###|     |########| | /
    |____\###/______\######/__|/
    ~~~~~~~~~~~~~~~~~~~~~~~~~~
'''

menuPrint = '''
    ~~~~~~~~~~~~~~ MENU ~~~~~~~~~~~~~~
        [1] Print Status Report
        [2] Order Espresso
        [3] Order Latte :P
        [4] Order Cappuccino
        [5] Exit :(
    (Input a # for the selected option)\n
'''

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# Functions
def calculateMoney():
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))
    return round((pennies * 0.01) + (nickels * 0.05) + (dimes * 0.1) + (quarters * 0.25), 2)

# Main code to run
print(logo)

keepGoing = True
while keepGoing:
    waterLeft = resources["water"]
    milkLeft = resources["milk"]
    coffeeLeft = resources["coffee"]

    choice = int(input(menuPrint))

    if choice == 1:
        print(f'''
            ~~~ Status Report ~~~
            Water: {waterLeft}mL
            Milk: {milkLeft}mL
            Coffee: {coffeeLeft}mL
            Profit: ${profit}
        ''')
    elif choice == 2:
        money = calculateMoney()

        waterReq = MENU["espresso"]["ingredients"]["water"]
        coffeeReq = MENU["espresso"]["ingredients"]["coffee"]
        cost = MENU["espresso"]["cost"]

        if money >= cost and waterReq <= waterLeft and coffeeReq <= coffeeLeft:
            change = money - cost
            profit += cost

            resources["water"] -= waterReq
            resources["coffee"] -= coffeeReq

            if change > 0:
                print(f"Your change: ${change}")
            print("Enjoy your espresso!")
        elif waterReq > waterLeft or milkReq > milkLeft or coffeeReq > coffeeLeft:
            print("Sorry, the machine does not have enough ingredients!")
        else:
            print("Sorry, you didn't put in enough money, here's your refund.\n")
    elif choice == 3:
        money = calculateMoney()

        waterReq = MENU["latte"]["ingredients"]["water"]
        milkReq = MENU["latte"]["ingredients"]["milk"]
        coffeeReq = MENU["latte"]["ingredients"]["coffee"]
        cost = MENU["latte"]["cost"]

        if money >= cost and waterReq <= waterLeft and milkReq <= milkLeft and coffeeReq <= coffeeLeft:
            change = money - cost
            profit += cost

            resources["water"] -= waterReq
            resources["milk"] -= milkReq
            resources["coffee"] -= coffeeReq

            if change > 0:
                print(f"Your change: ${change}")
            print("Enjoy your latte! :P")
        elif waterReq > waterLeft or milkReq > milkLeft or coffeeReq > coffeeLeft:
            print("Sorry, the machine does not have enough ingredients!")
        else:
            print("Sorry, you didn't put in enough money, here's your refund.\n")
    elif choice == 4:
        money = calculateMoney()

        waterReq = MENU["cappuccino"]["ingredients"]["water"]
        milkReq = MENU["cappuccino"]["ingredients"]["milk"]
        coffeeReq = MENU["cappuccino"]["ingredients"]["coffee"]
        cost = MENU["cappuccino"]["cost"]

        if money >= cost and waterReq <= waterLeft and milkReq <= milkLeft and coffeeReq <= coffeeLeft:
            change = money - cost
            profit += cost

            resources["water"] -= waterReq
            resources["milk"] -= milkReq
            resources["coffee"] -= coffeeReq

            if change > 0:
                print(f"Your change: ${change}")
            print("Enjoy your cappuccino!")
        elif waterReq > waterLeft or milkReq > milkLeft or coffeeReq > coffeeLeft:
            print("Sorry, the machine does not have enough ingredients!")
        else:
            print("Sorry, you didn't put in enough money, here's your refund.\n")
    elif choice == 5:
        print("Goodbye!")
        keepGoing = False


