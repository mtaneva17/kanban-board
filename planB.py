from timeit import repeat
from tkinter import *
import winsound
import schedule
import time
import datetime
from tkinter import Spinbox


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
            winsound.PlaySound("sound.wav", winsound.SND_ASYNC)


def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)
    

def job():
    schedule.every(45).minutes.do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)


clock = Tk()
clock.title("WAP")
clock.geometry("700x550")
clock.config(bg='#8cd1fe')

time_format = Label(
    clock, 
    text = " Enter time in 24 hour format! ", 
    fg = "white", bg = "#000000", font = ("Arial", 12, "italic")
    ).place(x = 242, y = 300)

addHr = Label(
    clock, 
    text = " Hour: ",
    font = ("Arial", 18, "bold"), 
    bg = "#8cd1fe"
    ).place(x = 228, y = 158)
addMn = Label(
    clock, 
    text = " Min: ", 
    font = ("Arial", 18, "bold"), 
    bg = "#8cd1fe"
    ).place(x = 314, y = 158)
addSc = Label(
    clock, 
    text = " Sec: ", 
    font = ("Arial", 18, "bold"), 
    bg = "#8cd1fe"
    ).place(x = 392, y = 158)

setYourAlarm = Label(
    clock, 
    text = " When to drink water: ", 
    bg = '#EEFCFF', 
    fg = "black", 
    relief = "sunken", 
    font = ("Arial", 32, "bold")
    ).place(x = 125, y = 60)


hour = StringVar()
min = StringVar()
sec = StringVar()


hourTime = Entry(
    clock, 
    textvariable = hour, 
    bg = "#EEFCFF", 
    width = 6,
    font= ("Arial", 16),
    ).place(x = 230, y = 190)

minTime = Entry(
    clock, 
    textvariable = min, 
    bg = "#EEFCFF", 
    width = 6,
    font= ("Arial", 16),
    ).place(x = 310, y = 190)

secTime = Entry(
    clock, 
    textvariable = sec, 
    bg = "#EEFCFF", 
    width = 6,
    font= ("Arial", 16),
    ).place(x = 390, y = 190)


submit = Button(
    clock, 
    text = " Set Alarm ", 
    fg = "black", 
    width = 12, 
    font = ("Arial", 14), 
    command = actual_time
    ).place(x = 280, y = 240)


checker = Label(
    clock, 
    relief = "sunken", 
    bg = "#EEFCFF",
    text = " How much did you drink? ", 
    fg = "#000000", 
    font = ("Arial", 20, "bold")
    ).place(x = 170, y = 380)

sb = Spinbox(
    clock,
    bg = "#EEFCFF",
    width = 8,
    from_ = 0,
    to = 1000,
    increment = 50,
    format = '%8.0f',
    font = ("Arial", 18)
).place(x = 268, y = 435)


mil = Label(
    clock, 
    text = " Milliliters: ", 
    bg = "#EEFCFF",
    relief = "ridge", 
    font = ("Arial", 18), 
    ).place(x = 145, y = 434)

sub_mil = Button(
    clock, 
    # bg = ,
    text = " Checked ✔ ", 
    fg = "#000000", 
    width = 10, 
    height = 0,
    font = ("Arial", 12), 
    command = ()
    ).place(x = 455, y = 434)


# from tkinter import *      
# root = Tk()      
canvas = Canvas(
    clock, 
    width = 192, 
    height = 192
    )
canvas.pack()
canvas.place(x = 20, y = 20)
img = PhotoImage(file = 'logo200.png')
canvas.create_image(0, 0, anchor = NW, image = img)   

exit_button = Button(
    clock, 
    # bg = ,
    text = " Exit ", 
    fg = "#000000", 
    width = 5, 
    height = 0,
    font = ("Arial", 12, "bold"), 
    command = clock.destroy
    ).place(x = 600, y = 490)

clock.mainloop()

