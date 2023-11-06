# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 09:58:06 2023

@author: Dell
"""

import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        selected_task = listbox.get(listbox.curselection())
        listbox.delete(listbox.curselection())
    except:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def clear_tasks():
    listbox.delete(0, tk.END)

root = tk.Tk()
root.title("To-Do List")

frame = tk.Frame(root)
frame.pack(pady=10)

entry = tk.Entry(frame, font=("Helvetica", 14))
entry.pack(fill=tk.BOTH, expand=True, side=tk.LEFT, padx=10)

add_button = tk.Button(frame, text="Add Task", command=add_task, font=("Helvetica", 12))
add_button.pack(side=tk.LEFT)

listbox = tk.Listbox(root, font=("Helvetica", 14))
listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

delete_button = tk.Button(root, text="Delete Task", command=delete_task, font=("Helvetica", 12))
delete_button.pack()

clear_button = tk.Button(root, text="Clear All Tasks", command=clear_tasks, font=("Helvetica", 12))
clear_button.pack()

root.mainloop()