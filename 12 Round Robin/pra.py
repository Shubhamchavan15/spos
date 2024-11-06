import tkinter as tk
from tkinter import messagebox

# Function to handle form submission
def submit_feedback():
    name = entry_name.get()
    rating = rating_var.get()
    feedback = text_feedback.get("1.0", tk.END).strip()
    
    # Selected food quality aspects
    aspects = []
    if taste_var.get(): aspects.append("Taste")
    if presentation_var.get(): aspects.append("Presentation")
    if service_var.get(): aspects.append("Service Quality")
    if hygiene_var.get(): aspects.append("Hygiene")

    if not name or not rating:
        messagebox.showwarning("Input Error", "Name and Rating are required fields!")
    else:
        # Display the feedback information (could be saved to a database in a real application)
        summary = f"Thank you, {name}!\n\nRating: {rating}\nAspects: {', '.join(aspects)}\nFeedback: {feedback}"
        messagebox.showinfo("Feedback Submitted", summary)
        reset_form()

# Function to reset the form
def reset_form():
    entry_name.delete(0, tk.END)
    rating_var.set("")
    text_feedback.delete("1.0", tk.END)
    taste_var.set(0)
    presentation_var.set(0)
    service_var.set(0)
    hygiene_var.set(0)

# Create main window
root = tk.Tk()
root.title("Customer Feedback Form")
root.geometry("400x450")

# Heading label
tk.Label(root, text="Customer Feedback Form", font=("Helvetica", 16, "bold")).pack(pady=10)

# Name label and entry
tk.Label(root, text="Name:").pack(anchor="w", padx=20)
entry_name = tk.Entry(root, width=30)
entry_name.pack(padx=20, pady=5)

# Rating label and options
tk.Label(root, text="Rating (1 to 5):").pack(anchor="w", padx=20)
rating_var = tk.StringVar()
rating_options = ["1", "2", "3", "4", "5"]
for rating in rating_options:
    tk.Radiobutton(root, text=rating, variable=rating_var, value=rating).pack(anchor="w", padx=40)

# Checkbox options for food quality aspects
tk.Label(root, text="Select Food Aspects:").pack(anchor="w", padx=20)
taste_var = tk.IntVar()
presentation_var = tk.IntVar()
service_var = tk.IntVar()
hygiene_var = tk.IntVar()
tk.Checkbutton(root, text="Taste", variable=taste_var).pack(anchor="w", padx=40)
tk.Checkbutton(root, text="Presentation", variable=presentation_var).pack(anchor="w", padx=40)
tk.Checkbutton(root, text="Service Quality", variable=service_var).pack(anchor="w", padx=40)
tk.Checkbutton(root, text="Hygiene", variable=hygiene_var).pack(anchor="w", padx=40)

# Textbox for additional feedback
tk.Label(root, text="Additional Comments:").pack(anchor="w", padx=20)
text_feedback = tk.Text(root, width=35, height=5)
text_feedback.pack(padx=20, pady=5)

# Submit and Reset buttons
tk.Button(root, text="Submit", command=submit_feedback).pack(side="left", padx=50, pady=20)
tk.Button(root, text="Reset", command=reset_form).pack(side="right", padx=50, pady=20)

# Run the GUI main loop
root.mainloop()
