import tkinter as tk
from tkinter import messagebox

# Function to display support contact information
def contact_support():
    messagebox.showinfo("Contact Support", "For further assistance, please contact:\n\nEmail: support@appname.com\nPhone: +1 123-456-7890")

# Create main window
root = tk.Tk()
root.title("Help")
root.geometry("500x500")

# Heading label
tk.Label(root, text="Help & Support", font=("Helvetica", 18, "bold")).pack(pady=10)

# Introduction label
tk.Label(root, text="Welcome to the Help Section", font=("Helvetica", 12)).pack(pady=5)
tk.Label(root, text="Here you'll find information on how to use the app, troubleshooting steps, and support details.", wraplength=450).pack(pady=5, padx=20)

# Help content in a Text widget
help_content = (
    "Getting Started:\n"
    "- Log in with your credentials or sign up if you're a new user.\n"
    "- Access different features from the main menu.\n\n"
    "Common Issues:\n"
    "- Unable to login? Ensure your credentials are correct.\n"
    "- App crashing? Restart the app and check for updates.\n"
    "- Forgot password? Use the 'Forgot Password' option on the login screen.\n\n"
    "Tips for Best Experience:\n"
    "- Keep the app updated to enjoy the latest features and fixes.\n"
    "- Use the 'Settings' menu to customize your preferences.\n\n"
    "For further assistance, click 'Contact Support' below."
)

text_help = tk.Text(root, width=60, height=18, wrap="word")
text_help.insert(tk.END, help_content)
text_help.config(state="disabled")  # Make text read-only
text_help.pack(pady=10, padx=20)

# Button to contact support
tk.Button(root, text="Contact Support", command=contact_support, font=("Helvetica", 10, "bold")).pack(pady=20)

# Run the GUI main loop
root.mainloop()
