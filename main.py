import tkinter as tk
from tkinter import messagebox
from words import get_random_word

# Settings
WORK_MINUTES = 1 
BREAK_MINUTES = 5

#Colors
BG_COLOR = '#003049'
TEXT_COLOR = '#fdf0d5' 
WORK_COLOR = '#d62828'
BREAK_COLOR = '#f77f00'
HEADING_COLOR = '#fcbf49'
WORD_COLOR = '#eae2b7'
DEFINITION_COLOR = '#8ac926'

class StudyTimerApp:
    #This is the main window fo the Study Timer App.
    
    def __init__(self, root):
        self.root = root
        self.root.title("Study Timer")
        self.root.geometry("420x360")
        self.root.configure(bg = BG_COLOR)
        self.root.resizable(False, False)

        #timer state
        self.remaining_seconds = WORK_MINUTES * 60
        self.is_running = False
        self.timer_id = None
        self.is_work_session = True
        self.sessions_completed = 0

        self.build_layout()
        self.show_new_word()

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

        #word of the session
        word_heading = tk.Label(
            self.root,
            text = "WORD OF THE DAY",
            font = ("Roboto", 14, "bold"),
            fg =  HEADING_COLOR,
            bg = BG_COLOR,
        )
        word_heading.pack(pady = (20,0))

        self.word_label = tk.Label(
            self.root,
            text = "WORD OF THE SESSION",
            font = ("Roboto", 10, "italic"),
            fg = WORD_COLOR,
            bg = BG_COLOR,
        )
        self.word_label.pack()

        #the definition filled in by show_new_word
        self.definition_label = tk.Label(
            self.root,
            text = "Definition will be displayed here.",
            font = ("Roboto", 10),
            fg = DEFINITION_COLOR,
            bg = BG_COLOR,
            wraplength = 400,
            justify = "center",
        )
        self.definition_label.pack(pady = (4,15))

        #Row of buttons
        button_frame = tk.Frame(self.root, bg=BG_COLOR)
        button_frame.pack(pady = 10)

        #button for starting the timer
        self.start_button = tk.Button(button_frame, text="Start", width = 8, font=("Roboto", 12), command = self.start_timer)
        self.start_button.grid(row = 0, column = 0, padx = 5)

        #button for the pause function
        self.pause_button = tk.Button(button_frame, text="Pause", width = 8, font=("Roboto", 12), command = self.pause_timer)
        self.pause_button.grid(row = 0, column = 1, padx = 5)

        #button for the reset function
        self.reset_button = tk.Button(button_frame, text="Reset", width = 8, font=("Roboto", 12), command = self.reset_timer)
        self.reset_button.grid(row = 0, column = 2, padx = 5)

        #complete session counter
        self.sessions_label = tk.Label(
            self.root,
            text = "Sessions completed: 0",
            font = ("Roboto", 12),
            fg = TEXT_COLOR,
            bg = BG_COLOR,
        )
        self.sessions_label.pack(pady = (15,0))

    #timer functions
    def update_time_display(self):
        #showing the remaining time as MM:SS
        minutes, seconds = divmod(self.remaining_seconds, 60)
        self.time_label.config(text = f"{minutes:02d}: {seconds:02d}")

    #state of the timer
    def start_timer(self):
        if not self.is_running and self.remaining_seconds > 0:
            self.is_running = True
            self.timer_id = self.root.after(1000, self.count_down)

    #countdown function
    def count_down(self):
        self.remaining_seconds -= 1
        self.update_time_display()

        if self.remaining_seconds > 0:
            self.timer_id = self.root.after(1000, self.count_down)
        else:
            self.finish_session()

    #pause function
    def pause_timer(self):
        if self.timer_id is not  None:
            self.root.after_cancel(self.timer_id)
            self.timer_id = None
            self.is_running = False

    #reset function
    def reset_timer(self):
        self.pause_timer() 
        self.set_session(self.is_work_session)

    #switch the screeen and timer to a work or break session
    def set_session(self, is_work):
        self.is_work_session = is_work

        if is_work:
            self.remaining_seconds = WORK_MINUTES * 60
            self.session_label.config(text = "WORK SESSION", fg = WORK_COLOR)
            self.show_new_word()
        else:
            self.remaining_seconds = BREAK_MINUTES * 60
            self.session_label.config(text = "BREAK TIME", fg = BREAK_COLOR)

        self.update_time_display()

    def show_reminder(self, title, message):
        self.root.bell()
        self.root.lift()
        self.root.attributes("-topmost", True)
        messagebox.showinfo(title, message)
        self.root.attributes("-topmost", False)

    #handle the end of a session and switch to the next one
    def finish_session(self):
        self.is_running = False
        self.timer_id = None

        if self.is_work_session:
            self.sessions_completed += 1
            self.session_label.config(text=f"Sessions completed: {self.sessions_completed}")
            self.show_reminder(
                "Time for a break!",
                f"Great work! You finished session {self.sessions_completed} .\n\n"
                f"Stand up, stretch, drink some water, and rest your eyes "
                f"Stand up, stretch, drink some water, and rest your eyes "
                f"for {BREAK_MINUTES} minutes.",
            )
            self.set_session(is_work = False)
        else:
            self.show_reminder(
                "Break is over"
                "Feeling refreshed? Let's get back to work. You've got this!",
            )
            self.set_session(is_work = True)
        self.start_timer()

    def show_new_word(self):
        try:
            word, word_type, definition = get_random_word()
            self.word_label.config(text=f"{word} ({word_type})")
            self.definition_label.config(text=definition)
        except LookupError:
            self.word_label.config(text="No word found.")
            self.definition_label.config(text="The dictionary could not be loded.")


if __name__ == "__main__":
    root = tk.Tk()
    app = StudyTimerApp(root)
    root.mainloop()
