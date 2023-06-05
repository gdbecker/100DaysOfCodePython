# 100 Days of Code: Python
# May 20, 2022
# Output NATO phonetic alphabet based on user input

# Import and set up data
import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
alpha = {row.letter:row.code for (index, row) in data.iterrows()}

# Ask user for their name
user_name = input("Enter a word: ").upper()

# Get phonetic words for each letter
# phon = []
# for letter in user_name:
#     for (key, value) in alpha.items():
#         if key == letter:
#             phon.append(value)

# my attempt and then Angela's
phon = [value for letter in user_name for (key, value) in alpha.items() if key == letter]
phon2 = [alpha[letter] for letter in user_name]

# Show results
print(phon)
print(phon2)