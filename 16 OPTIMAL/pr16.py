import tkinter as tk
from tkinter import messagebox

# Function to handle button clicks
def open_login():
    messagebox.showinfo("Login", "Navigating to Login Screen...")

def open_register():
    messagebox.showinfo("Register", "Navigating to Register Screen...")

# Create main window
root = tk.Tk()
root.title("Welcome Screen")
root.geometry("500x400")

# App Title
tk.Label(root, text="Welcome to MyApp", font=("Helvetica", 20, "bold")).pack(pady=20)

# Welcome Message
tk.Label(root, text="Your Gateway to an Incredible Experience!", font=("Helvetica", 14), fg="grey").pack(pady=10)

# Description
description = (
    "MyApp is your personal assistant, here to make your life easier. "
    "Log in to access personalized features, or sign up if you're new! "
    "Let's get started on a journey to simplify your daily tasks and enhance your productivity."
)
tk.Label(root, text=description, wraplength=450, justify="center").pack(pady=20)

# Button for Login
tk.Button(root, text="Login", font=("Helvetica", 12), width=15, command=open_login).pack(pady=10)

# Button for Register
tk.Button(root, text="Register", font=("Helvetica", 12), width=15, command=open_register).pack(pady=10)

# Footer
tk.Label(root, text="Thank you for choosing MyApp!", font=("Helvetica", 10), fg="blue").pack(side="bottom", pady=20)

# Run the GUI main loop
root.mainloop()
