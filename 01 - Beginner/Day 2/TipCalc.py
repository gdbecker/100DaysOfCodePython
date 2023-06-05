# 100 Days of Code: Python
# May 3, 2022
# Caclculate how much each person pays for dinner, tip included

# Grab info
print("Welcome to the tip calculator!")
totalBill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15 "))
ppl = int(input("How many people to split the bill? "))

# Math
tip /= 100
tip += 1
totalBill *= tip
amt = round(totalBill / ppl, 2)

# Results
print(f"Each person should pay: ${amt}")
