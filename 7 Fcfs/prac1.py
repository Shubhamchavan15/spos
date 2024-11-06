import tkinter as tk
from tkinter import messagebox

# Function to handle form submission
def submit_form():
    name = entry_name.get()
    age = entry_age.get()
    gender = gender_var.get()
    course = listbox_course.get(tk.ACTIVE)
    terms_accepted = terms_var.get()
    
    if not name or not age or not gender or not course:
        messagebox.showwarning("Input Error", "All fields are required!")
    elif not terms_accepted:
        messagebox.showwarning("Input Error", "Please accept the terms and conditions.")
    else:
        messagebox.showinfo("Success", f"Registration Successful for {name}!")
        reset_form()

# Function to reset the form
def reset_form():
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    gender_var.set(None)
    listbox_course.selection_clear(0, tk.END)
    terms_var.set(0)

# Create main window
root = tk.Tk()
root.title("Student Registration Form")
root.geometry("400x400")

# Heading label
tk.Label(root, text="Student Registration Form", font=("Helvetica", 16, "bold")).pack(pady=10)

# Name label and entry
tk.Label(root, text="Name:").pack(anchor="w", padx=20)
entry_name = tk.Entry(root, width=30)
entry_name.pack(padx=20, pady=5)

# Age label and entry
tk.Label(root, text="Age:").pack(anchor="w", padx=20)
entry_age = tk.Entry(root, width=30)
entry_age.pack(padx=20, pady=5)

# Gender label and radio buttons
tk.Label(root, text="Gender:").pack(anchor="w", padx=20)
gender_var = tk.StringVar()
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").pack(anchor="w", padx=40)
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").pack(anchor="w", padx=40)
tk.Radiobutton(root, text="Other", variable=gender_var, value="Other").pack(anchor="w", padx=40)

# Course label and listbox
tk.Label(root, text="Select Course:").pack(anchor="w", padx=20)
listbox_course = tk.Listbox(root, height=4)
courses = ["Computer Science", "Electronics", "Mechanical", "Civil"]
for course in courses:
    listbox_course.insert(tk.END, course)
listbox_course.pack(padx=20, pady=5)

# Terms and conditions checkbox
terms_var = tk.IntVar()
tk.Checkbutton(root, text="I accept the terms and conditions", variable=terms_var).pack(padx=20, pady=5)

# Submit and Reset buttons
tk.Button(root, text="Submit", command=submit_form).pack(side="left", padx=50, pady=20)
tk.Button(root, text="Reset", command=reset_form).pack(side="right", padx=50, pady=20)

# Run the GUI main loop
root.mainloop()
