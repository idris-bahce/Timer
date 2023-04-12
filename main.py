from tkinter import *
import math
from placeholder import Placeholder
from playsound import playsound

GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
timer = None
hours = "0"
minutes = "0"
seconds = "0"
resume_button = None


def start_timer():
    hour = hour_entry.get()
    minute = minute_entry.get()
    second = second_entry.get()
    total_seconds = (int(hour) * 3600) + (int(minute) * 60) + int(second)
    count_down(total_seconds)


def count_down(count):
    global hours
    global minutes
    global seconds
    hours = math.floor(count / 3600)
    minutes = math.floor(count / 60)
    minutes = minutes % 60
    seconds = count % 60
    if hours < 10:
        hours = f"0{hours}"
    if seconds < 10:
        seconds = f"0{seconds}"
    if minutes < 10:
        minutes = f"0{minutes}"
    time.config(text=f"{hours}:{minutes}:{seconds}")
    if count >= 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        playsound("mp3.mp3")


def continue_count_down():
    time.config(text=f"{hours}:{minutes}:{seconds}")
    count = (int(hours) * 3600) + (int(minutes) * 60) + int(seconds)
    resume_button.config(text="Stop", width=5, command=stop)
    if count >= 0:
        window.after(1000, count_down, count - 1)


def stop():
    global resume_button
    window.after_cancel(timer)
    resume_button = Button(text="Resume", width=5, command=continue_count_down)
    resume_button.grid(column=3, row=3)


window = Tk()
window.title("Timer")
window.config(pady=100, padx=100, bg=YELLOW)
window.geometry('600x400')
window.resizable(height=None, width=None)

main_writing = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 40, "bold"), bg=YELLOW)
main_writing.grid(column=1, row=0)

hour_entry = Placeholder(window, "hour", width=8)
hour_entry.grid(column=0, row=2)

minute_entry = Placeholder(window, "minute", width=8)
minute_entry.grid(column=1, row=2)

second_entry = Placeholder(window, "second", width=8)
second_entry.grid(column=2, row=2)

time = Label(text="00:00:00", fg=GREEN, font=(FONT_NAME, 40, "bold"), bg=YELLOW)
time.grid(column=1, row=4)

start_button = Button(text="Start", width=5, command=start_timer)
start_button.grid(column=0, row=6)

stop_button = Button(text="Stop", width=5, command=stop)
stop_button.grid(column=3, row=6)

window.mainloop()