import tkinter as tk
import math

# Function to handle button clicks
def button_click(value):
    entry.insert(tk.END, value)  # Append new character instead of replacing
    entry.xview_moveto(1)  # Auto-scroll to the right

# Function to clear the entry widget
def clear():
    entry.delete(0, tk.END)

# Function to delete the last character (backspace)
def backspace():
    current = entry.get()
    if current:  # Check if there's anything to delete
        entry.delete(len(current) - 1, tk.END)  # Corrected deletion method
        entry.xview_moveto(1)  # Auto-scroll to the right

# Function to calculate square root
def square_root():
    try:
        result = math.sqrt(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Function to calculate cube root
def cube_root():
    try:
        result = eval(entry.get()) ** (1/3)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Function to evaluate the expression
def calculate():
    try:
        result = eval(entry.get())  # Evaluates the string in the entry widget
        entry.delete(0, tk.END)
        entry.insert(0, int(result) if result == int(result) else result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Function to handle keypress events
def key_press(event):
    key = event.keysym
    char = event.char
    if char in "0123456789+-*/.%":
        button_click(char)
    elif key == "Return":
        calculate()
    elif key == "BackSpace":
        backspace()
    elif key == "Escape":
        clear()

# Set up the main window
root = tk.Tk()
root.title("Calculator")
root.configure(bg="#808080")  # Background color

# Entry widget to display the expression/result
entry = tk.Entry(root, width=20, font=("Arial", 24), borderwidth=2, relief="solid", justify="right", bg="#D4EED4", fg="#000000")
entry.grid(row=0, column=0, columnspan=4, pady=10, padx=10, sticky="we")  # Changed from `pack()` to `grid()`

# Bind keyboard events to the calculator
root.bind("<KeyPress>", key_press)

# Button layout: a list of buttons and their positions on the grid
buttons = [
    ("C", 1, 2), ("⌫", 1, 3),
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("/", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("*", 3, 3),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("-", 4, 3),
    (".", 5, 0), ("0", 5, 1), ("=", 5, 2), ("+", 5, 3),
    ("√", 1, 0), ("∛", 1, 1)
]

# Create buttons and place them on the grid
for (text, row, col) in buttons:
    button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 20), bg="#c0c0c0", fg="#000000", relief="raised", borderwidth=2)
    if text == "=":
        button.config(command=calculate)
    elif text == "C":
        button.config(command=clear)
    elif text == "⌫":
        button.config(command=backspace)
    elif text == "√":
        button.config(command=square_root)
    elif text == "∛":
        button.config(command=cube_root)
    else:
        button.config(command=lambda value=text: button_click(value))
    button.grid(row=row, column=col, padx=5, pady=5)

# Start the Tkinter event loop
root.mainloop()
