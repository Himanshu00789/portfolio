from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
reps  = 0
timer = None
marks=""

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    heading.config(text="Timer", fg = GREEN , font=(FONT_NAME,30,"bold"))
    check_marks.config(text="")
    global reps
    reps = 0
 # ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        heading.config(text="Break", fg=RED, font=(FONT_NAME, 30, "bold"))
        count_down(long_break_sec)
    elif reps % 2 == 0:
        heading.config(text="Break", fg=PINK, font=(FONT_NAME, 30, "bold"))
        count_down(short_break_sec)
    else:
        count_down(work_sec)
        heading.config(text="Work", fg=RED, bg=PINK, font=(FONT_NAME, 30, "bold"))



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/ 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count >0:
        global timer
        timer=window.after(1000, count_down, count - 1)
    else:
        start_timer()
        global marks
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("pomodoro")
window.config(padx = 100,pady = 50, bg=YELLOW)


canvas =  Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
photo_image = PhotoImage(file = "tomato1.png",)
canvas.create_image(100, 112, image=photo_image)
timer_text = canvas.create_text(100,130,text = "00:00",fill = "white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1, row=1)


heading=Label(text="Timer", fg = GREEN , font=(FONT_NAME,30,"bold"))
heading.grid(column = 1,row = 0)


start_button = Button(text = "start",command=start_timer)
start_button.grid(column = 0,row=3)

reset_button = Button(text = "reset",command=reset_timer)
reset_button.grid(column = 2,row = 3)



check_marks = Label(fg=GREEN,font=(FONT_NAME,10,"bold"))
check_marks.grid(column=1,row=3)



window.mainloop()