# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI = round((weight)/(height ** 2))

meaning = ""

if BMI <= 18.5:
    meaning = "you are underweight."
elif BMI > 18.5 and BMI <= 25:
    meaning = "you have a normal weight."
elif BMI > 25 and BMI <= 30:
    meaning = "you are slightly overweight."
elif BMI > 30 and BMI <= 35:
    meaning = "you are obese."
elif BMI > 35:
    meaning = "you are clinically obese."

print(f"Your BMI is {BMI}, {meaning}")
