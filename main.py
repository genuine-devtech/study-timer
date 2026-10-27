import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Focus Timer")
window.geometry("300x150")

# Add a text label to the window
label = tk.Label(window, text="Setup works! 🎉", font=("Arial", 16))
label.pack(pady=40)

# Keep the window open and responding
window.mainloop()