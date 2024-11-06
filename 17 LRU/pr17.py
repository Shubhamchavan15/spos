import tkinter as tk
from tkinter import messagebox

# Function to handle form submission
def submit_form():
    name = entry_name.get()
    age = entry_age.get()
    gender = gender_var.get()
    selected_sport = listbox_sport.get(tk.ACTIVE)
    skill_level = skill_var.get()
    prior_experience = "Yes" if experience_var.get() else "No"

    # Validation
    if not name or not age or not gender or not selected_sport or not skill_level:
        messagebox.showwarning("Input Error", "All fields are required!")
    else:
        # Display the entered information in a summary (could save to a database in a real app)
        summary = (f"Registration Successful!\n\n"
                   f"Name: {name}\nAge: {age}\nGender: {gender}\n"
                   f"Sport: {selected_sport}\nSkill Level: {skill_level}\n"
                   f"Prior Experience: {prior_experience}")
        messagebox.showinfo("Registration Summary", summary)
        reset_form()

# Function to reset the form
def reset_form():
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    gender_var.set(None)
    listbox_sport.selection_clear(0, tk.END)
    skill_var.set(None)
    experience_var.set(0)

# Create main window
root = tk.Tk()
root.title("Sports Academy Registration Form")
root.geometry("500x600")

# Heading label
tk.Label(root, text="Sports Academy Registration Form", font=("Helvetica", 16, "bold")).pack(pady=10)

# Name label and entry
tk.Label(root, text="Name:").pack(anchor="w", padx=20)
entry_name = tk.Entry(root, width=40)
entry_name.pack(padx=20, pady=5)

# Age label and entry
tk.Label(root, text="Age:").pack(anchor="w", padx=20)
entry_age = tk.Entry(root, width=40)
entry_age.pack(padx=20, pady=5)

# Gender label and radio buttons
tk.Label(root, text="Gender:").pack(anchor="w", padx=20)
gender_var = tk.StringVar()
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").pack(anchor="w", padx=40)
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").pack(anchor="w", padx=40)
tk.Radiobutton(root, text="Other", variable=gender_var, value="Other").pack(anchor="w", padx=40)

# Sport label and listbox
tk.Label(root, text="Sport:").pack(anchor="w", padx=20)
listbox_sport = tk.Listbox(root, height=5)
sports = ["Soccer", "Basketball", "Tennis", "Swimming", "Martial Arts"]
for sport in sports:
    listbox_sport.insert(tk.END, sport)
listbox_sport.pack(padx=20, pady=5)

# Skill Level label and radio buttons
tk.Label(root, text="Skill Level:").pack(anchor="w", padx=20)
skill_var = tk.StringVar()
tk.Radiobutton(root, text="Beginner", variable=skill_var, value="Beginner").pack(anchor="w", padx=40)
tk.Radiobutton(root, text="Intermediate", variable=skill_var, value="Intermediate").pack(anchor="w", padx=40)
tk.Radiobutton(root, text="Advanced", variable=skill_var, value="Advanced").pack(anchor="w", padx=40)

# Prior Experience checkbox
experience_var = tk.IntVar()
tk.Checkbutton(root, text="I have prior experience in this sport", variable=experience_var).pack(anchor="w", padx=20, pady=5)

# Submit and Reset buttons
tk.Button(root, text="Submit", command=submit_form, width=15).pack(side="left", padx=50, pady=20)
tk.Button(root, text="Reset", command=reset_form, width=15).pack(side="right", padx=50, pady=20)

# Run the GUI main loop
root.mainloop()
