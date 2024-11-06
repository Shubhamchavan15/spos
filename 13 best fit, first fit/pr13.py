import tkinter as tk
from tkinter import messagebox

# Function to handle fund transfer
def transfer_funds():
    sender_account = entry_sender_account.get()
    receiver_account = entry_receiver_account.get()
    amount = entry_amount.get()
    note = entry_note.get("1.0", tk.END).strip()

    # Validation
    if not sender_account or not receiver_account or not amount:
        messagebox.showwarning("Input Error", "All fields are required!")
    elif not amount.isdigit() or int(amount) <= 0:
        messagebox.showwarning("Input Error", "Enter a valid amount.")
    elif sender_account == receiver_account:
        messagebox.showwarning("Input Error", "Sender and receiver accounts must be different.")
    else:
        # Simulate successful transaction
        messagebox.showinfo("Transaction Successful", f"Transferred ${amount} from {sender_account} to {receiver_account}.")
        reset_form()

# Function to reset the form
def reset_form():
    entry_sender_account.delete(0, tk.END)
    entry_receiver_account.delete(0, tk.END)
    entry_amount.delete(0, tk.END)
    entry_note.delete("1.0", tk.END)

# Create main window
root = tk.Tk()
root.title("Fund Transfer")
root.geometry("400x400")

# Heading label
tk.Label(root, text="Fund Transfer", font=("Helvetica", 16, "bold")).pack(pady=10)

# Sender Account label and entry
tk.Label(root, text="Sender Account Number:").pack(anchor="w", padx=20)
entry_sender_account = tk.Entry(root, width=30)
entry_sender_account.pack(padx=20, pady=5)

# Receiver Account label and entry
tk.Label(root, text="Receiver Account Number:").pack(anchor="w", padx=20)
entry_receiver_account = tk.Entry(root, width=30)
entry_receiver_account.pack(padx=20, pady=5)

# Amount label and entry
tk.Label(root, text="Amount (USD):").pack(anchor="w", padx=20)
entry_amount = tk.Entry(root, width=30)
entry_amount.pack(padx=20, pady=5)

# Note label and textbox
tk.Label(root, text="Note (Optional):").pack(anchor="w", padx=20)
entry_note = tk.Text(root, width=30, height=3)
entry_note.pack(padx=20, pady=5)

# Transfer and Reset buttons
tk.Button(root, text="Transfer", command=transfer_funds).pack(side="left", padx=50, pady=20)
tk.Button(root, text="Reset", command=reset_form).pack(side="right", padx=50, pady=20)

# Run the GUI main loop
root.mainloop()
