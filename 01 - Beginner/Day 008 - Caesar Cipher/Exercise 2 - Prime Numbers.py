#Write your code below this line 👇
def prime_checker(number):
    numberFactors = []
    for x in range(1, number + 1):
        if number % x == 0:
            numberFactors.append(x)

    if len(numberFactors) > 2:
        print("It's not a prime number.")
    elif len(numberFactors) == 2:
        print("It's a prime number.")

#Write your code above this line 👆

#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
