# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 09:59:40 2023

@author: Dell
"""


import tkinter as tk
from tkinter import Entry, Label, Button
import random
import string



def generate_password():
    password_length = int(length_entry.get())

    if password_length <= 0:
        result_label.config(text="Password length must be greater than 0")
        return
   
    use_letters = var_letters.get()
    use_digits = var_digits.get()
    use_special_chars = var_special_chars.get()

    if not (use_letters or use_digits or use_special_chars):
        result_label.config(text="Select at least one option")
        return

    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    if len(characters) == 0:
        result_label.config(text="No character set selected")
        return

    password = ''.join(random.choice(characters) for i in range(password_length))
    result_label.config(text="Generated Password: " + password, fg= '#0000FF')

root = tk.Tk()
root.title("Password Generator")


font_style = ("Arial", 12)

# Change background color
root.configure(bg='#87CEEB')

length_label = Label(root, text="Password Length:")
length_label.pack()

length_entry = Entry(root)
length_entry.pack()

var_letters = tk.IntVar()
letters_check = tk.Checkbutton(root, text="Include Letters", variable=var_letters)
letters_check.pack()

var_digits = tk.IntVar()
digits_check = tk.Checkbutton(root, text="Include Digits", variable=var_digits)
digits_check.pack()

var_special_chars = tk.IntVar()
special_chars_check = tk.Checkbutton(root, text="Include Special Characters", variable=var_special_chars)
special_chars_check.pack()

generate_button = Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

result_label = Label(root, text="")
result_label.pack()

root.mainloop()