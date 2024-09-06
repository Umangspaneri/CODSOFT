import string
import random
import tkinter as tk
from tkinter import messagebox

def generate_password():
    try:
        length = int(entry_length.get())
        
        if length < 4:
            messagebox.showerror("Input Error", "Password length should be at least 4.")
            return
        
        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase
        digits = string.digits
        special_characters = string.punctuation

        # Ensure the password has at least one of each type of character for complexity
        password = [
            random.choice(lowercase),
            random.choice(uppercase),
            random.choice(digits),
            random.choice(special_characters),
        ]

        all_characters = lowercase + uppercase + digits + special_characters
        password += random.choices(all_characters, k=length - 4)

        random.shuffle(password)

        generated_password = ''.join(password)
        label_result.config(text=f"Generated Password: {generated_password}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number.")

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")

label_length = tk.Label(root, text="Enter Desired Password Length:")
label_length.pack(pady=10)

entry_length = tk.Entry(root, width=10)
entry_length.pack(pady=5)

button_generate = tk.Button(root, text="Generate Password", command=generate_password)
button_generate.pack(pady=20)

label_result = tk.Label(root, text="Generated Password: ", font=("Arial", 12))
label_result.pack(pady=20)

root.mainloop()