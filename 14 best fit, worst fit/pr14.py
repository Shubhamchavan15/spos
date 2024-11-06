import tkinter as tk
from tkinter import messagebox

# Function to handle form submission
def submit_form():
    name = entry_name.get()
    age = entry_age.get()
    gender = gender_var.get()
    symptoms = []
    if fever_var.get(): symptoms.append("Fever")
    if cough_var.get(): symptoms.append("Cough")
    if headache_var.get(): symptoms.append("Headache")
    if fatigue_var.get(): symptoms.append("Fatigue")
    department = listbox_department.get(tk.ACTIVE)

    # Validation
    if not name or not age or not gender or not department:
        messagebox.showwarning("Input Error", "All fields are required!")
    else:
        # Display the entered information in a summary (could save to a database in a real app)
        summary = (f"Patient Registration Successful!\n\n"
                   f"Name: {name}\nAge: {age}\nGender: {gender}\n"
                   f"Symptoms: {', '.join(symptoms)}\nDepartment: {department}")
        messagebox.showinfo("Registration Successful", summary)
        reset_form()

# Function to reset the form
def reset_form():
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    gender_var.set(None)
    fever_var.set(0)
    cough_var.set(0)
    headache_var.set(0)
    fatigue_var.set(0)
    listbox_department.selection_clear(0, tk.END)

# Create main window
root = tk.Tk()
root.title("Patient Registration Form")
root.geometry("400x500")

# Heading label
tk.Label(root, text="Patient Registration Form", font=("Helvetica", 16, "bold")).pack(pady=10)

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

# Symptoms checkboxes
tk.Label(root, text="Symptoms:").pack(anchor="w", padx=20)
fever_var = tk.IntVar()
cough_var = tk.IntVar()
headache_var = tk.IntVar()
fatigue_var = tk.IntVar()
tk.Checkbutton(root, text="Fever", variable=fever_var).pack(anchor="w", padx=40)
tk.Checkbutton(root, text="Cough", variable=cough_var).pack(anchor="w", padx=40)
tk.Checkbutton(root, text="Headache", variable=headache_var).pack(anchor="w", padx=40)
tk.Checkbutton(root, text="Fatigue", variable=fatigue_var).pack(anchor="w", padx=40)

# Department label and listbox
tk.Label(root, text="Department:").pack(anchor="w", padx=20)
listbox_department = tk.Listbox(root, height=4)
departments = ["General Medicine", "Cardiology", "Neurology", "Orthopedics"]
for dept in departments:
    listbox_department.insert(tk.END, dept)
listbox_department.pack(padx=20, pady=5)

# Submit and Reset buttons
tk.Button(root, text="Submit", command=submit_form).pack(side="left", padx=50, pady=20)
tk.Button(root, text="Reset", command=reset_form).pack(side="right", padx=50, pady=20)

# Run the GUI main loop
root.mainloop()
