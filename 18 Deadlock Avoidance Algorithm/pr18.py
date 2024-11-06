import tkinter as tk
from tkinter import messagebox

# Function to handle booking submission
def book_ride():
    pickup = entry_pickup.get()
    dropoff = entry_dropoff.get()
    vehicle_type = vehicle_var.get()
    booking_type = booking_var.get()
    
    # Validation
    if not pickup or not dropoff or not vehicle_type or not booking_type:
        messagebox.showwarning("Input Error", "All fields are required!")
    else:
        messagebox.showinfo("Booking Confirmation", f"Booking Confirmed!\n\n"
                                                    f"Pickup: {pickup}\n"
                                                    f"Drop-off: {dropoff}\n"
                                                    f"Vehicle: {vehicle_type}\n"
                                                    f"Booking Type: {booking_type}")
        reset_form()

# Function to reset the form
def reset_form():
    entry_pickup.delete(0, tk.END)
    entry_dropoff.delete(0, tk.END)
    vehicle_var.set(None)
    booking_var.set(None)

# Create main window
root = tk.Tk()
root.title("Cab/Auto Booking App")
root.geometry("400x450")

# Heading label
tk.Label(root, text="Cab/Auto Booking", font=("Helvetica", 16, "bold")).pack(pady=10)

# Pickup Location label and entry
tk.Label(root, text="Pickup Location:").pack(anchor="w", padx=20)
entry_pickup = tk.Entry(root, width=40)
entry_pickup.pack(padx=20, pady=5)

# Drop-off Location label and entry
tk.Label(root, text="Drop-off Location:").pack(anchor="w", padx=20)
entry_dropoff = tk.Entry(root, width=40)
entry_dropoff.pack(padx=20, pady=5)

# Vehicle Type label and radio buttons
tk.Label(root, text="Select Vehicle Type:").pack(anchor="w", padx=20)
vehicle_var = tk.StringVar()
tk.Radiobutton(root, text="Cab", variable=vehicle_var, value="Cab").pack(anchor="w", padx=40)
tk.Radiobutton(root, text="Auto", variable=vehicle_var, value="Auto").pack(anchor="w", padx=40)

# Booking Type label and radio buttons
tk.Label(root, text="Select Booking Type:").pack(anchor="w", padx=20)
booking_var = tk.StringVar()
tk.Radiobutton(root, text="Immediate", variable=booking_var, value="Immediate").pack(anchor="w", padx=40)
tk.Radiobutton(root, text="Scheduled", variable=booking_var, value="Scheduled").pack(anchor="w", padx=40)

# Submit and Reset buttons
tk.Button(root, text="Book Ride", command=book_ride, width=15).pack(side="left", padx=50, pady=20)
tk.Button(root, text="Reset", command=reset_form, width=15).pack(side="right", padx=50, pady=20)

# Run the GUI main loop
root.mainloop()
