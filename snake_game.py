import tkinter as tk
from tkinter import messagebox

# Initialize the main application window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("400x500")

# Global variable to keep the input string
input_text = tk.StringVar()

# Display area
display_frame = tk.Frame(root)
display_frame.pack()

display = tk.Entry(display_frame, textvar=input_text, font=("Arial", 18), width=24, bd=8, insertwidth=4, bg="powder blue", justify="right")
display.grid(row=0, column=0, columnspan=4)

# Button press function
def button_click(item):
    current = input_text.get()
    input_text.set(current + str(item))

# Clear display function
def clear_display():
    input_text.set("")

# Calculate result function
def calculate():
    try:
        result = str(eval(input_text.get()))
        input_text.set(result)
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")
        input_text.set("")

# Buttons
button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row, col = 0, 0
for button in buttons:
    if button == "=":
        btn = tk.Button(button_frame, text=button, width=10, height=3, command=calculate)
    elif button == "C":
        btn = tk.Button(button_frame, text=button, width=10, height=3, command=clear_display)
    else:
        btn = tk.Button(button_frame, text=button, width=10, height=3, command=lambda b=button: button_click(b))
    
    btn.grid(row=row, column=col, padx=5, pady=5)
    
    col += 1
    if col > 3:
        col = 0
        row += 1

# Run the application
root.mainloop()
