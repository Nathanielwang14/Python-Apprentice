# colin gave me this stupid projectr to make sure i knew how to code in python
# before i started hotel manager 

import string

vowel_set = 'aeiouAEIOU'
vowels = [ch for ch in string.ascii_letters if ch in vowel_set]

import string

vowels = 'aeiouAEIOU'
consonants = [ch for ch in string.ascii_letters if ch not in vowels]



def ask_word(prompt):
    #prompt to ask 
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a actual word!")




i= ask_word("enter word")
x= input
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
consonants = [
    'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 
    'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z',
    'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 
    'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z'
]


while True:
        print(i)
        if x in vowels:
             
             
             





