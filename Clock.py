import tkinter as tk
from time import strftime

# Function to update the digital clock label
def update_time():
    string_time = strftime('%H:%M:%S %p')
    digital_clock.config(text=string_time)
    digital_clock.after(1000, update_time)

# Main Tkinter window
root = tk.Tk()
root.title("Digital Clock")

# Digital clock label configuration
digital_clock = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='white')
digital_clock.pack(pady=20)

# Initial call to update_time function
update_time()

# Tkinter main loop
root.mainloop()
