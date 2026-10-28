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
    
    def __init__(self, root):
        self.root = root
        self.root.title("Study Timer")
        self.root.geometry("420x360")
        self.root.configure(bg=BG_COLOR)
        self.root.resizable(False, False)

        self.build_layout()

    #layout of the app
    def build_layout(self):
        
        #This is the part of the work session / break time
        self.session_label = tk.Label(
            self.root,
            text="WORK SESSION",
            font = ("Roboto", 24, "bold"),
            fg = WORK_COLOR,
            bg = BG_COLOR,
        )
        self.session_label.pack(pady=(25,5))

        # countdown display
        self.time_label = tk.Label(
            self.root,
            text = f'{WORK_MINUTES:02d}:00',
            font = ("Roboto", 48, "bold"),
            fg = TEXT_COLOR,
            bg = BG_COLOR,
        )
        self.time_label.pack()

        #Motivational qoute display
        self.qoute_label = tk.Label(
            self.root,
            text = "The motivational qoute will displayed here.",
            font = ("Roboto", 12, "italic"),
            fg = QUOTE_COLOR,
            bg = BG_COLOR,
            wraplength=350,
            justify = "center"
        )
        self.qoute_label.pack(pady = 15)

        #Row of buttons
        button_frame = tk.Frame(self.root, bg=BG_COLOR)
        button_frame.pack(pady = 10)

        #button for starting the timer
        self.start_button = tk.Button(button_frame, text="Start", width = 8, font=("Roboto", 12, "bold"))
        self.start_button.grid(row = 0, column = 0, padx = 5)

        #button for the pause function
        self.pause_button = tk.Button(button_frame, text="Pause", width = 8, font=("Roboto", 12, "bold"))
        self.pause_button.grid(row = 0, column = 1, padx = 5)

        #button for the reset function
        self.reset_button = tk.Button(button_frame, text="Reset", width = 8, font=("Roboto", 12, "bold"))
        self.reset_button.grid(row = 0, column = 2, padx = 5)

        #complete session counter
        self.sessios_label = tk.Label(
            self.root,
            text = "Sessions completed: 0",
            font = ("Roboto", 12),
            fg = TEXT_COLOR,
            bg = BG_COLOR,
        )
        self.sessios_label.pack(pady = (15,0))


if __name__ == "__main__":
    root = tk.Tk()
    app = StudyTimerApp(root)
    root.mainloop()
