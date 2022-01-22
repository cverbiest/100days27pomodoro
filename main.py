# import tkinter
from tkinter import *

FONT = ("Arial", 20, "italic bold")

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# should be 1000, use smaller values to debug
MILLISPERTICK = 1000
SECONDSPERTICK = 1

# (text, time, #checkmarks)
ACTIVITIES = [
    ('Timer', 0, ""),
    ("Work", WORK_MIN, ""),
    ("Pauze", SHORT_BREAK_MIN, "✓"),
    ("Work", WORK_MIN, "✓"),
    ("Pauze", SHORT_BREAK_MIN, "✓✓"),
    ("Work", WORK_MIN, "✓✓"),
    ("Pauze", SHORT_BREAK_MIN, "✓✓✓"),
    ("Work", WORK_MIN, "✓✓✓"),
    ("Break", LONG_BREAK_MIN, "✓✓✓✓")
]
# ---------------------------- TIMER RESET ------------------------------- #
current_activity = 0
time = 0

def reset_timer():
    next_activity(0)

# ---------------------------- TIMER MECHANISM ------------------------------- #


def next_activity(new_activity=None):
    global current_activity, time
    window.attributes('-topmost', 1)
    window.attributes('-topmost', 0)

    print(f"current act = {current_activity}, next = {new_activity}")
    if new_activity is None:
        new_activity = current_activity + 1
    current_activity = new_activity % len(ACTIVITIES)
    print(current_activity, ACTIVITIES, len(ACTIVITIES))
    print(ACTIVITIES[current_activity])
    Activity.set(ACTIVITIES[current_activity][0])
    time = ACTIVITIES[current_activity][1] * 60
    display_time()
    window.after(MILLISPERTICK, tick)
    CheckMarks.set(ACTIVITIES[current_activity][2])


def start_timer():
    #next_activity(1)
    next_activity()


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def display_time():
    seconds = time
    s = "{:02d}:{:02d}".format(seconds // 60, seconds % 60)
    print(seconds, s)
    canvas.itemconfigure(timer_text, text=s)


def tick():
    global time
    if time > 0:
        window.after(MILLISPERTICK, tick)
        time -= SECONDSPERTICK
        display_time()
        if time == 0:
            next_activity()


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro converter")
window.minsize(500, 300)
# window.maxsize(500, 300)
window.config(padx=30, pady=30, bg=YELLOW)

window.after(MILLISPERTICK, tick)

Activity = StringVar(value="Timer")
Label(textvariable=Activity, bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40, "bold")).grid(row=0, column=1)

canvas = Canvas(width=300, height=224, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(150, 112, image=image)
timer_text = canvas.create_text(150, 130, text="00:00", fill=YELLOW, font=(FONT_NAME, 40, "bold"))
canvas.grid(row=1, column=1)

Button(text="Start", command=start_timer).grid(row=2, column=0)
Button(text="Reset", command=reset_timer).grid(row=2, column=2)
CheckMarks = StringVar()
Label(textvariable=CheckMarks, bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20, "bold")).grid(row=3, column=1)
print(timer_text)

next_activity(0)

window.mainloop()
