"""
Write a Python program that asks the user for two numbers. The program should
display the sum of the two numbers.

In this program we will just give you the comments for what you need to do. Look
at the comments and the code snippets in the previous lessons, like
03_My_Ages.py, to figure out how to complete the program.


"""

from tkinter import messagebox, simpledialog, Tk #

window = Tk()   
window.withdraw()  

a = simpledialog.askinteger("Input number", "Input the first number") 

b = simpledialog.askinteger("Input number", "Input the second number") 

messagebox.showinfo("Answer", a+b)
# Keep the window open

