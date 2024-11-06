import tkinter as tk
from tkinter import messagebox

# Function to handle login
def login():
    username = entry_username.get()
    password = entry_password.get()
    
    # Simple validation logic for demonstration
    if username == "admin" and password == "password":
        messagebox.showinfo("Login Successful", "Welcome to the system!")
    else:
        messagebox.showwarning("Login Failed", "Incorrect username or password.")

# Function to reset the form
def reset_form():
    entry_username.delete(0, tk.END)
    entry_password.delete(0, tk.END)

# Create main window
root = tk.Tk()
root.title("Login Window")
root.geometry("300x200")

# Heading label
tk.Label(root, text="Login", font=("Helvetica", 16, "bold")).pack(pady=10)

# Username label and entry
tk.Label(root, text="Username:").pack(anchor="w", padx=20)
entry_username = tk.Entry(root, width=30)
entry_username.pack(padx=20, pady=5)

# Password label and entry
tk.Label(root, text="Password:").pack(anchor="w", padx=20)
entry_password = tk.Entry(root, width=30, show="*")
entry_password.pack(padx=20, pady=5)

# Login and Reset buttons
tk.Button(root, text="Login", command=login).pack(side="left", padx=30, pady=20)
tk.Button(root, text="Reset", command=reset_form).pack(side="right", padx=30, pady=20)

# Run the GUI main loop
root.mainloop()
