# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
total = 0

# Pizza size
if size == "S":
    total += 15
elif size == "M":
    total += 20
elif size == "L":
    total += 25

# Pepperoni
if size == "S" and add_pepperoni == "Y":
    total += 2
elif (size == "M" or size == "L") and add_pepperoni == "Y":
    total += 3

# Extra cheese
if extra_cheese == "Y":
    total += 1

# Results
print(f"Your final bill is ${total}.")
