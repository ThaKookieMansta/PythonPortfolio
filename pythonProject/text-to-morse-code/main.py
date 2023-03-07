import os
import time
text = input("Type the text you want converted to morse code below\n").upper()
# We need a dictionary to hold the values of the morse code alphabet
code_translation = {
    "A": "*- ",
    "B": "-*** ",
    "C": "-*-* ",
    "D": "-** ",
    "E": "* ",
    "F": "**-* ",
    "G": "--* ",
    "H": "**** ",
    "I": "** ",
    "J": "*-- ",
    "K": "-*- ",
    "L": "*-** ",
    "M": "-- ",
    "N": "-* ",
    "O": "--- ",
    "P": "*--* ",
    "Q": "--*- ",
    "R": "*-* ",
    "S": "*** ",
    "T": "- ",
    "U": "**- ",
    "V": "***- ",
    "W": "*-- ",
    "X": "-**- ",
    "Y": "-*-- ",
    "Z": "--** ",
    "1": "*---- ",
    "2": "**--- ",
    "3": "***-- ",
    "4": "****- ",
    "5": "***** ",
    "6": "-**** ",
    "7": "--*** ",
    "8": "---** ",
    "9": "----* ",
    "0": "----- ",
}

code_translator = True
while code_translator:  # We use the while loop so that the application will run as long as the condition is true
    morse_code = ""
    for l in text:
        if l in code_translation:
            morse_code += code_translation[l]
    print(morse_code)
    time.sleep(1)
    continue_prompt = input("Do you have more text to translate?(Type n or y)\n").lower()
    if continue_prompt == "n":
        code_translator = False
    elif continue_prompt == "y":
        os.system('clear')
        text = input("Type the text you want converted to morse code below\n").upper()
    else:
        print("!!Invalid prompt!!")
