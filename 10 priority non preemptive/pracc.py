import tkinter as tk
from tkinter import messagebox

# Quiz Questions and Answers
questions = [
    ("What is the capital of France?", ["Berlin", "London", "Paris", "Madrid"], "Paris"),
    ("What is the smallest prime number?", ["0", "1", "2", "3"], "2"),
    ("What is the chemical symbol for water?", ["H2O", "CO2", "NaCl", "O2"], "H2O")
]

# Current Question Index
current_question = 0
user_answers = []

# Function to handle answer submission and move to next question
def submit_answer():
    global current_question, user_answers
    
    # Get selected answer
    selected_answer = answer_var.get()
    if selected_answer == "":
        messagebox.showwarning("No Selection", "Please select an answer.")
        return

    user_answers.append(selected_answer)
    
    # If there are more questions, show the next question
    if current_question < len(questions) - 1:
        current_question += 1
        show_question()
    else:
        show_result()

# Function to show each question
def show_question():
    question, options, _ = questions[current_question]
    question_label.config(text=question)
    
    # Clear previous options
    for button in option_buttons:
        button.pack_forget()
    
    # Display new options
    for i, option in enumerate(options):
        option_buttons[i].config(text=option, value=option)
        option_buttons[i].pack(anchor="w")

    # Clear selection
    answer_var.set("")

# Function to calculate and show the result
def show_result():
    score = 0
    for i, answer in enumerate(user_answers):
        if answer == questions[i][2]:  # Compare with correct answer
            score += 1
    messagebox.showinfo("Quiz Completed", f"Your Score: {score}/{len(questions)}")
    root.destroy()

# Initialize main window
root = tk.Tk()
root.title("Online Quiz")
root.geometry("400x300")

# Quiz Header
tk.Label(root, text="Online Quiz", font=("Helvetica", 16, "bold")).pack(pady=10)

# Question Label
question_label = tk.Label(root, text="", font=("Helvetica", 12), wraplength=300)
question_label.pack(pady=10)

# Variable to store the selected answer
answer_var = tk.StringVar()

# Answer options as radio buttons
option_buttons = [tk.Radiobutton(root, variable=answer_var, font=("Helvetica", 10)) for _ in range(4)]

# Submit Button
submit_button = tk.Button(root, text="Submit Answer", command=submit_answer)
submit_button.pack(pady=20)

# Show the first question
show_question()

# Run the GUI main loop
root.mainloop()
