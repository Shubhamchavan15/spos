import tkinter as tk
from tkinter import messagebox

# Function to handle sign-up submission
def sign_up():
    username = entry_username.get()
    email = entry_email.get()
    password = entry_password.get()
    confirm_password = entry_confirm_password.get()

    # Basic validation
    if not username or not email or not password or not confirm_password:
        messagebox.showwarning("Input Error", "All fields are required!")
    elif password != confirm_password:
        messagebox.showwarning("Password Mismatch", "Passwords do not match!")
    else:
        # Success message
        messagebox.showinfo("Success", f"Sign-up Successful! Welcome, {username}!")
        reset_form()

# Function to reset the form
def reset_form():
    entry_username.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_password.delete(0, tk.END)
    entry_confirm_password.delete(0, tk.END)

# Create main window
root = tk.Tk()
root.title("Sign-Up Window")
root.geometry("400x350")

# Heading label
tk.Label(root, text="Sign-Up", font=("Helvetica", 16, "bold")).pack(pady=10)

# Username label and entry
tk.Label(root, text="Username:").pack(anchor="w", padx=20)
entry_username = tk.Entry(root, width=30)
entry_username.pack(padx=20, pady=5)

# Email label and entry
tk.Label(root, text="Email:").pack(anchor="w", padx=20)
entry_email = tk.Entry(root, width=30)
entry_email.pack(padx=20, pady=5)

# Password label and entry
tk.Label(root, text="Password:").pack(anchor="w", padx=20)
entry_password = tk.Entry(root, width=30, show="*")
entry_password.pack(padx=20, pady=5)

# Confirm Password label and entry
tk.Label(root, text="Confirm Password:").pack(anchor="w", padx=20)
entry_confirm_password = tk.Entry(root, width=30, show="*")
entry_confirm_password.pack(padx=20, pady=5)

# Sign-Up and Reset buttons
tk.Button(root, text="Sign Up", command=sign_up).pack(side="left", padx=40, pady=20)
tk.Button(root, text="Reset", command=reset_form).pack(side="right", padx=40, pady=20)

# Run the GUI main loop
root.mainloop()
