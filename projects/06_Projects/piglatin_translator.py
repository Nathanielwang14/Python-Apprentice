# colin gave me this stupid projectr to make sure i knew how to code in python
# before i started hotel manager 
import string
from tkinter import simpledialog, Tk
window = Tk()
window.withdraw()


vowel_set = 'aeiouAEIOU'
vowels = [ch for ch in string.ascii_letters if ch in vowel_set]

import string

vowels = 'aeiouAEIOU'
consonants = [ch for ch in string.ascii_letters if ch not in vowels]

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
consonants = [
    'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 
    'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z',
    'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 
    'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z'
]

def ask_word(prompt):
    #prompt to ask 
    while True:
        try:
            return str(simpledialog.askstring("Textbox", prompt))
        except ValueError:
            print("Please enter a actual word!")
        
def ask_phrase(prompt):
      while True:
        try:
            return str(simpledialog.askstring("Textbox", prompt))
        except ValueError:
            print("Please enter a actual word!")
    
def entered_word(value):
    for word in value.split():
        if word[0] in vowels:
            print(word + "yay", end=" ") 
        else:
            print(word[1:] + word[0] + "ay", end=" ") 
 
entered_word(ask_word("Enter Word"))