# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
leapYear = False

if year % 4 == 0:
    leapYear = True

    if year % 100 == 0:
        leapYear = False

        if year % 400 == 0:
            leapYear = True
        elif year % 400 != 0:
            leapYear = False

    elif year % 100 != 0:
        leapYear = True

elif year % 4 != 0:
    leapYear = False

if leapYear:
    print("Leap year.")
elif not leapYear:
    print("Not leap year.")
