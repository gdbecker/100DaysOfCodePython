#Write your code below this row 👇

for n in range(1,101):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
        continue
    elif n % 3 == 0:
        print("Fizz")
        continue
    elif n % 5 == 0:
        print("Buzz")
        continue
    else:
        print(n)
