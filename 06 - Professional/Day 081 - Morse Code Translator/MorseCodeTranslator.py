# 100 Days of Code: Python
# July 6, 2022
# Morse Code translator scripting app
# Input text, outputs Morse Code equivalent

# Morse Code static dictionary
decode_alpha_to_morse = {"A": ".-",
          "B": "-...",
          "C": "-.-.",
          "D": "-..",
          "E": ".",
          "F": "..-.",
          "G": "--.",
          "H": "....",
          "I": "..",
          "J": ".---",
          "K": "-.-",
          "L": ".-..",
          "M": "--",
          "N": "-.",
          "O": "---",
          "P": ".--.",
          "Q": "--.-",
          "R": ".-.",
          "S": "...",
          "T": "-",
          "U": "..-",
          "V": "...-",
          "W": ".--",
          "X": "-..-",
          "Y": "-.--",
          "Z": "--..",
          "0": "-----",
          "1": ".----",
          "2": "..---",
          "3": "...--",
          "4": "....-",
          "5": ".....",
          "6": "-....",
          "7": "--...",
          "8": "---..",
          "9":"----."}

decode_morse_to_alpha = {".-": "A",
          "-...": "B",
          "-.-.": "C",
          "-..": "D",
          ".": "E",
          "..-.": "F",
          "--.": "G",
          "....": "H",
          "..": "I",
          ".---": "J",
          "-.-": "K",
          ".-..": "L",
          "--": "M",
          "-.": "N",
          "---": "O",
          ".--.": "P",
          "--.-": "Q",
          ".-.": "R",
          "...": "S",
          "-": "T",
          "..-": "U",
          "...-": "V",
          ".--": "W",
          "-..-": "X",
          "-.--": "Y",
          "--..": "Z",
          "-----": "0",
          ".----": "1",
          "..---": "2",
          "...--": "3",
          "....-": "4",
          ".....": "5",
          "-....": "6",
          "--...": "7",
          "---..": "8",
          "----.": "9"}

# Ask user for text to translate
print("-.-.-.-.- MORSE CODE TRANSLATOR -.-.-.-.-")
text_raw = input("\nEnter text to translate: ").upper()

# Translate
translated_chars = []
for letter in text_raw:
    translated_chars.append(decode_alpha_to_morse[letter])

# Output translation
print(f"\nMorse Code Translation: {' '.join(translated_chars)}")