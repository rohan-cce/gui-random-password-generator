from tkinter import *
# importing the tkinter module

import pyperclip
# importing the pyperclip module to use it to copy our generated password to clipboard

import random
# random module will be used in generating the random password

root = Tk()
# initializing the tkinter

root.geometry("400x200")
# setting the width and height of the gui

passstr = StringVar()
#this variable(passstr) will be used to store the password generated

passlen = IntVar()
# declaring a variable of integer type which will be used to store the length of the password entered by the user

passlen.set(0)
# setting the length of the password to zero initially

def generate():
    # function to generate the password
     
    pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
            'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
            'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
            'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 
            'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', 
            '9', '0', ' ', '!', '@', '#', '$', '%', '^', '&', 
            '*', '(', ')']
    # storing the keys in a list which will be used to generate the password

    password = ""
    #declaring the empty string

    
    for x in range(passlen.get()):
        # loop to generate the random password of the length entered by the user
        password = password + random.choice(pass1)

    
    passstr.set(password)
    # setting the password to the entry widget

def copytoclipboard():
    # function to copy the password to the clipboard
    random_password = passstr.get()
    pyperclip.copy(random_password)
    print("Password Copied to Clipboard")

Label(root, text="Password Generator Application", font="calibri 20 bold").pack()
# Creating a text label widget

Label(root, text="Enter password length").pack(pady=3)
# Creating a text label widget

Entry(root, textvariable=passlen).pack(pady=3)
# Creating a entry widget to take password length entered by the user

Button(root, text="Generate Password", command=generate).pack(pady=7)
# button to call the generate function

Entry(root, textvariable=passstr).pack(pady=3)
# entry widget to show the generated password

Button(root, text="Copy to clipboard", command=copytoclipboard).pack()
# button to call the copytoclipboard function

root.mainloop()
# mainloop() is an infinite loop used to run the application when 
# it's in ready state 
