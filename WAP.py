from tkinter import *
import winsound
import schedule
import time
import datetime


def alarm(set_alarm_timer):

    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print("The set time is:", date)
        print(now)

        if now == set_alarm_timer:
            print("Time To Drink Water!")
            winsound.PlaySound("sound.wav",winsound.SND_ASYNC)

  
def job():
    schedule.every(45).minutes.do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)


def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)


clock = Tk()
clock.title("WAP")
clock.geometry("700x500")
clock.config(bg='#8cd1fe')

time_format = Label(clock, text = " Enter time in 24 hour format! ", fg = "white", bg = "black", font = ("Arial", 12, "italic")).place(x = 250, y = 300)
addTime = Label(clock, text = " Hour: " + "      " + "Min: " + "      " + "Sec: ", font = ("Arial", 14, "bold"), bg = "#8cd1fe").place(x = 240, y = 160)
setYourAlarm = Label(clock, text = " When to drink water: ", fg = "black", relief = "sunken", font = ("Arial", 28, "bold")).place(x = 160, y = 60)

hour = StringVar()
min = StringVar()
sec = StringVar()

hourTime= Entry(clock, textvariable = hour, bg = "white", width = 11).place(x = 240, y = 190)
minTime= Entry(clock, textvariable = min, bg = "white", width = 11).place(x = 320, y = 190)
secTime = Entry(clock, textvariable = sec, bg = "white", width = 11).place(x = 400, y = 190)

submit = Button(clock, text = " Set Alarm ", fg = "black", width = 11, font = ("Arial", 12), command = actual_time).place(x = 300, y = 240)
clock.mainloop()


