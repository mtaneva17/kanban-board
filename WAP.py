from tkinter import *
import winsound
import time
import datetime


def alarm(set_alarm_timer):

    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print("The Set Date is:", date)
        print(now)

        if now == set_alarm_timer:
            print("Time To Drink Water!")
            winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
            break

def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)

clock = Tk()
clock.title("WAP")
clock.geometry("700x500")
time_format = Label(clock, text = "Enter time in 24 hour format!", fg = "white", bg = "black", font = "Arial").place(x = 210, y = 350)
addTime = Label(clock, text = "Hour     Min     Sec", font = 60).place(x = 300, y = 160)
setYourAlarm = Label(clock, text = "When to drink water:", fg = "black", relief = "solid", font = ("Arial", 20, "bold")).place(x = 140, y = 50)

hour = StringVar()
min = StringVar()
sec = StringVar()

hourTime= Entry(clock, textvariable = hour, bg = "white", width = 30).place(x = 250, y = 200)
minTime= Entry(clock, textvariable = min, bg = "white", width = 30).place(x = 300, y = 200)
secTime = Entry(clock, textvariable = sec, bg = "white", width = 10).place(x = 350, y = 200)

submit = Button(clock, text = "Set Alarm", fg = "black", width = 10, command = actual_time).place(x = 300, y = 250)
clock.mainloop()