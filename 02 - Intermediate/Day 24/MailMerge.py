# 100 Days of Code: Python
# May 18, 2022
# Inserting names from a file into a letter template
# Practice using files with python!

PLACEHOLDER = "[name]"

# Grab list of names for inserting
names_list = []
names_file = open("Input/Names/invited_names.txt", "r")
names_list = names_file.readlines()
names_list = [line.rstrip() for line in names_list]
names_file.close()

# Make letter txt file with each of the names
for name in names_list:
    new_file = open(f"Output/ReadyToSend/letter_for_{name}.txt", "w")

    template_file = open("Input/Letters/starting_letter.txt", "r")
    template_lines = template_file.readlines()
    template_lines = [line.rstrip() for line in template_lines]
    template_file.close()

    # Sub in the invited name
    template_lines[0] = template_lines[0].replace(PLACEHOLDER, name)

    for line in template_lines:
        new_file.write(line + "\n")
    new_file.close()