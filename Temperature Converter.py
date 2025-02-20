import tkinter as tk
from tkinter import ttk

def convert_temperature():
    temp = float(entry_temperature.get())
    from_unit = combo_from.get()
    to_unit = combo_to.get()
    
    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            result = (temp * 9/5) + 32
        elif to_unit == "Kelvin":
            result = temp + 273.15
        else:
            result = temp
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            result = (temp - 32) * 5/9
        elif to_unit == "Kelvin":
            result = (temp - 32) * 5/9 + 273.15
        else:
            result = temp
    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            result = temp - 273.15
        elif to_unit == "Fahrenheit":
            result = (temp - 273.15) * 9/5 + 32
        else:
            result = temp
    
    label_result.config(text=f"Result: {int(result)} {to_unit}")

# Create the main window
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("300x300")
root.configure(bg="#c2c1c2")

# Create widgets
label_temperature = tk.Label(root, text="Enter Temperature:", bg="#c2c1c2")
entry_temperature = tk.Entry(root)

label_from = tk.Label(root, text="From:", bg="#c2c1c2")
combo_from = ttk.Combobox(root, values=["Celsius", "Fahrenheit", "Kelvin"])
combo_from.set("Celsius")

label_to = tk.Label(root, text="To:", bg="#c2c1c2")
combo_to = ttk.Combobox(root, values=["Celsius", "Fahrenheit", "Kelvin"])
combo_to.set("Fahrenheit")

button_convert = tk.Button(root, text="Convert", command=convert_temperature)
label_result = tk.Label(root, text="Result:", bg="#c2c1c2")

# Place widgets on the window
label_temperature.pack(pady=5)
entry_temperature.pack(pady=5)
label_from.pack(pady=5)
combo_from.pack(pady=5)
label_to.pack(pady=5)
combo_to.pack(pady=5)
button_convert.pack(pady=10)
label_result.pack(pady=5)

# Run the application
root.mainloop()
