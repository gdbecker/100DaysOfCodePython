# 100 Days of Code: Python
# May 7, 2022
# Caesar Cipher: encrypt and decrypt based on user input

# Functions
def encrypt(plainText, shiftAmount):
    cipherText = ""

    for letter in plainText:
        position = alphabet.index(letter)
        newPosition = position + shiftAmount

        if newPosition > (len(alphabet) - 1):
            newPosition -= len(alphabet)

        newLetter = alphabet[newPosition]
        cipherText += newLetter
    print(f"The encoded text is {cipherText}")

def decrypt(plainText, shiftAmount):
    decryptedText = ""

    for letter in plainText:
        position = alphabet.index(letter)
        newPosition = position - shiftAmount

        if newPosition < 0:
            newPosition += len(alphabet)

        newLetter = alphabet[newPosition]
        decryptedText += newLetter
    print(f"The decrypted text is {decryptedText}")


# Set up variables
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
logo = """
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88
            88             88
           ""             88
                          88
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8
8b         88 88       d8 88       88 8PP""""""" 88
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88
              88
              88
"""

# Loop through while the user wants to do something
keepGoing = True
print(logo)

while keepGoing:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == "encode":
        encrypt(plainText=text, shiftAmount=shift)
    elif direction == "decode":
        decrypt(plainText=text, shiftAmount=shift)

    ask = input("Do you want to have another go? (Y/N)\n")

    if ask == "N":
        keepGoing = False
