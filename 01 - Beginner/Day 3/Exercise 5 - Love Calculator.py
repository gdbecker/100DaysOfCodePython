# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1 = name1.upper()
name2 = name2.upper()

trueLetters = 0
loveLetters = 0

for c in name1:
    if c == 'T' or c == 'R' or c == 'U' or c == 'E':
        trueLetters += 1

for d in name2:
    if d == 'T' or d == 'R' or d == 'U' or d == 'E':
        trueLetters += 1

for e in name1:
    if e == 'L' or e == 'O' or e == 'V' or e == 'E':
        loveLetters += 1

for f in name2:
    if f == 'L' or f == 'O' or f == 'V' or f == 'E':
        loveLetters += 1

score = str(trueLetters) + str(loveLetters)

if int(score) < 10 or int(score) > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif int(score) >= 40 and int(score) <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
