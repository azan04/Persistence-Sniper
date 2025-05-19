import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
import subprocess

# Function to run the PowerShell command
def run_find_all_persistence():
    try:
        # Running the PowerShell command and capturing output
        result = subprocess.run(['powershell', '-Command', 'Find-AllPersistence'], capture_output=True, text=True)
        
        # Check for any errors from stderr
        if result.stderr:
            output_text.delete(1.0, tk.END)  # Clear any existing text
            output_text.insert(tk.END, f"Error: {result.stderr}\n\n")  # Insert error output with formatting
        else:
            # Format the result for better readability
            formatted_output = format_output(result.stdout)
            # Display the formatted result in the text box
            output_text.delete(1.0, tk.END)  # Clear any existing text
            output_text.insert(tk.END, formatted_output)  # Insert the new formatted output
    except Exception as e:
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, f"Error: {e}\n\n")

# Function to clear the output
def clear_output():
    output_text.delete(1.0, tk.END)  # Clear the text box

# Function to close the application
def exit_application():
    root.quit()  # Close the window

# Function to format the output text
def format_output(text):
    formatted_text = ""
    lines = text.split("\n")
    for line in lines:
        if "Error" in line:
            formatted_text += f"⚠ {line}\n"
        else:
            formatted_text += f"{line}\n"
    return formatted_text

# Create the main window
root = tk.Tk()
root.title("Persistence Sniper - Find All Persistence")
root.geometry("800x400")  # Set a wider window size

# Create a frame for the heading
header_frame = ttk.Frame(root, padding="5 5 5 5")
header_frame.grid(row=0, column=0, columnspan=3, sticky="ew")

# Create a heading label
heading_label = tk.Label(header_frame, text="Persistence Sniper", font=("Arial", 18, "bold"), bg="#212121", fg="#FF9800")
heading_label.grid(row=0, column=0, padx=10, sticky="n")

# Set a modern theme
style = ttk.Style(root)
style.theme_use('clam')

# Apply some custom styles for colors
style.configure('TButton', background='#FF5722', foreground='white', padding=5, font=('Arial', 10, 'bold'))
style.map('TButton',
          foreground=[('active', 'white')],
          background=[('active', '#FF3D00')])

style.configure('TFrame', background='#212121')
style.configure('TLabel', background='#212121', foreground='white')
style.configure('TEntry', background='#424242', foreground='white')
style.configure('TText', background='#424242', foreground='white')
style.configure('TScrollbar', background='#616161')

# Create a frame for the buttons
button_frame = ttk.Frame(root, padding="5 5 5 5")
button_frame.grid(row=1, column=0, columnspan=3, pady=5)

# Create a button to trigger the command
run_button = ttk.Button(button_frame, text="Run", command=run_find_all_persistence, style='TButton')
run_button.grid(row=0, column=0, padx=5)

# Create a button to clear the output
clear_button = ttk.Button(button_frame, text="Clear", command=clear_output, style='TButton')
clear_button.grid(row=0, column=1, padx=5)

# Create an exit button
exit_button = ttk.Button(button_frame, text="Exit", command=exit_application, style='TButton')
exit_button.grid(row=0, column=2, padx=5)

# Create a scrolled text widget to display the output
output_text = scrolledtext.ScrolledText(root, width=85, height=15, font=("Consolas", 12), bg='#212121', fg='#FF9800')
output_text.grid(row=2, column=0, columnspan=3, pady=5)

# Run the main loop
root.mainloop()
