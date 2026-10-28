import tkinter as tk

# Settings
WORK_MINUTES = 25 
BREAK_MINUTES = 5

#Colors
BG_COLOR = '#003049'
TEXT_COLOR = '#fdf0d5' 
WORK_COLOR = '#d62828'
BREAK_COLOR = '#f77f00'
QUOTE_COLOR = '#003049'

# Create the main window
window = tk.Tk()
window.title("Focus Timer")
window.geometry("300x150")

class StudyTimerApp:

    #This is the main window fo the Study Timer App.
    def __init_(self, root):
        self.root = root
        self.root.title("Study Timer")
        self.root.geometry("420x360")
        self.root.configure(bg=BG_COLOR)
        self.root.resizable(False, False)

        self.build_layout()

    def build_layout(self):
        #This is the part of the work session / break time

        self.session_label = tk.Label(
            self.root,
            text="WORK SESSION",
            font = ("Roboto", 24, "bold"),
            fg = WORK_COLOR,
            bg=BG_COLOR,
        )

if __name__ == "__main__":
    root = tk.Tk()
    app = StudyTimerApp(root)
    root.mainloop()
