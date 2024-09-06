import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                messagebox.showerror("Error", "Cannot divide by zero.")
                return
        else:
            messagebox.showerror("Error", "Invalid operation.")
            return

        label_result.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")

label_num1 = tk.Label(root, text="Enter First Number:")
label_num1.pack(pady=10)
entry_num1 = tk.Entry(root)
entry_num1.pack(pady=5)

label_num2 = tk.Label(root, text="Enter Second Number:")
label_num2.pack(pady=10)
entry_num2 = tk.Entry(root)
entry_num2.pack(pady=5)

label_operation = tk.Label(root, text="Choose Operation:")
label_operation.pack(pady=10)

operation_var = tk.StringVar(value="+")
radiobutton_add = tk.Radiobutton(root, text="+", variable=operation_var, value="+")
radiobutton_add.pack()
radiobutton_subtract = tk.Radiobutton(root, text="-", variable=operation_var, value="-")
radiobutton_subtract.pack()
radiobutton_multiply = tk.Radiobutton(root, text="*", variable=operation_var, value="*")
radiobutton_multiply.pack()
radiobutton_divide = tk.Radiobutton(root, text="/", variable=operation_var, value="/")
radiobutton_divide.pack()

button_calculate = tk.Button(root, text="Calculate", command=calculate)
button_calculate.pack(pady=20)

label_result = tk.Label(root, text="Result: ")
label_result.pack(pady=10)

root.mainloop()
