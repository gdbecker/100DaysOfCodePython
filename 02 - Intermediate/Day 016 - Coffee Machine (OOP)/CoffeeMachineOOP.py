# 100 Days of Code: Python
# May 12, 2022
# Digital version of a coffee machine! Order and make drinks, print status, give change
# OOP version of Day 15's project

import menu
import money_machine
import coffee_maker

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

# Set up initial objects
myMenu = menu.Menu()
myMoneyMachine = money_machine.MoneyMachine()
myCoffeeMaker = coffee_maker.CoffeeMaker()

# Set up loop for using the coffee maker
keepGoing = True
print(logo)

while keepGoing:
    choice = int(input(menuPrint))

    if choice == 1:
        myCoffeeMaker.report()
        myMoneyMachine.report()
    elif choice == 2:
        espressoDrink = myMenu.find_drink("espresso")
        canMake = myCoffeeMaker.is_resource_sufficient(espressoDrink)

        if canMake:
            enoughMoney = myMoneyMachine.make_payment(espressoDrink.cost)

            if enoughMoney:
                change = myMoneyMachine.money_received - espressoDrink.cost
                myMoneyMachine.profit += espressoDrink.cost
                myCoffeeMaker.make_coffee(espressoDrink)
    elif choice == 3:
        latteDrink = myMenu.find_drink("latte")
        canMake = myCoffeeMaker.is_resource_sufficient(latteDrink)

        if canMake:
            enoughMoney = myMoneyMachine.make_payment(latteDrink.cost)

            if enoughMoney:
                change = myMoneyMachine.money_received - latteDrink.cost
                myMoneyMachine.profit += latteDrink.cost
                myCoffeeMaker.make_coffee(latteDrink)
    elif choice == 4:
        cappuccinoDrink = myMenu.find_drink("cappuccino")
        canMake = myCoffeeMaker.is_resource_sufficient(cappuccinoDrink)

        if canMake:
            enoughMoney = myMoneyMachine.make_payment(cappuccinoDrink.cost)

            if enoughMoney:
                change = myMoneyMachine.money_received - cappuccinoDrink.cost
                myMoneyMachine.profit += cappuccinoDrink.cost
                myCoffeeMaker.make_coffee(cappuccinoDrink)
    elif choice == 5:
        print("Goodbye!")
        keepGoing = False

