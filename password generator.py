from tkinter import *
from tkinter import messagebox
import random
import string

# Create Window
root = Tk()
root.title("Password Generator")
root.geometry("450x400")
root.config(bg="#2C3E50")
root.resizable(False, False)

# Title
Label(
    root,
    text="🔐 Password Generator",
    font=("Arial", 20, "bold"),
    bg="#2C3E50",
    fg="white"
).pack(pady=20)

# Password Variable
password_var = StringVar()

# Password Display
Entry(
    root,
    textvariable=password_var,
    font=("Arial", 16),
    width=28,
    justify="center"
).pack(pady=10)

# Length Label
Label(
    root,
    text="Password Length",
    font=("Arial", 14),
    bg="#2C3E50",
    fg="white"
).pack()

# Length Selector
length = Scale(
    root,
    from_=6,
    to=30,
    orient=HORIZONTAL,
    length=250,
    bg="#2C3E50",
    fg="white",
    highlightthickness=0
)
length.set(12)
length.pack(pady=10)

# Generate Function
def generate_password():
    characters = (
        string.ascii_uppercase +
        string.ascii_lowercase +
        string.digits +
        "!@#$%^&*()?"
    )

    password = "".join(
        random.choice(characters)
        for _ in range(length.get())
    )

    password_var.set(password)

# Copy Function
def copy_password():
    if password_var.get() == "":
        messagebox.showwarning("Warning", "Generate a password first!")
        return

    root.clipboard_clear()
    root.clipboard_append(password_var.get())
    messagebox.showinfo("Success", "Password copied successfully!")

# Buttons
Button(
    root,
    text="Generate Password",
    font=("Arial", 13, "bold"),
    bg="#27AE60",
    fg="white",
    width=22,
    command=generate_password
).pack(pady=10)

Button(
    root,
    text="Copy Password",
    font=("Arial", 13, "bold"),
    bg="#3498DB",
    fg="white",
    width=22,
    command=copy_password
).pack(pady=10)

Button(
    root,
    text="Exit",
    font=("Arial", 13, "bold"),
    bg="#E74C3C",
    fg="white",
    width=22,
    command=root.destroy
).pack(pady=20)

root.mainloop()