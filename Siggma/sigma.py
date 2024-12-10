import tkinter as tk
import sys

def close_application():
    root.destroy()
    sys.exit()

# Create the main window
root = tk.Tk()
root.title("Sigma Alert")

# Set window to be always on top
root.attributes('-topmost', True)

# Create a label with the sigma message
label = tk.Label(root, text="I'm the sigma", font=("Arial", 24))
label.pack(padx=20, pady=20)

# Configure the window close behavior to exit the entire process
root.protocol("WM_DELETE_WINDOW", close_application)

# Center the window on the screen
window_width = 300
window_height = 200
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f'{window_width}x{window_height}+{x}+{y}')

# Start the application
root.mainloop()