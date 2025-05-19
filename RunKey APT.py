import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()

# Hide the main window (we only want the message box)
root.withdraw()

# Show the message box
messagebox.showinfo("Hello", "Hello! This is the RunKey APT")

# Close the application after the message box is closed
root.quit()
