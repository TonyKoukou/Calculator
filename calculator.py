# ------------------------------------------------------
# Copyright (c) 2026 Antonis Koukoumelas. All rights reserved.
# Αυτό το project δημιουργήθηκε από Antonis Koukoumelas.
# ------------------------------------------------------

# calculator.py
import tkinter as tk

def calculate():
    try:
        result_var.set(eval(entry.get()))
    except:
        result_var.set("Error")

root = tk.Tk()
root.title("Simple Calculator")

entry = tk.Entry(root, width=20)
entry.pack()

result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var)
result_label.pack()

button = tk.Button(root, text="Calculate", command=calculate)
button.pack()

root.mainloop()
