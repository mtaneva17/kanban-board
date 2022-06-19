# Здравейте, това е целия код. Другите са логото, помощни материали, тестове или проверки.



from tkinter import *
import winsound
import schedule
import time
import datetime
from tkinter import Spinbox
from tkinter import filedialog



# От терминала показва часа, датата и алармата в часа, в който трябва да пием вода.
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
    

# От тук го караме да пуска алармата на всеки час.
def job():
    schedule.every(60).minutes.do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)


# През tkinter въвеждаме как да изглежда приложението.
clock = Tk()
clock.title("WAP")
clock.geometry("700x600")
clock.config(bg='#8cd1fe')


# Надписът в черно с инструкцията за въвеждането на час.
time_format = Label(
    clock, 
    text = " Enter time in 24 hour format! ", 
    fg = "white", bg = "#000000", font = ("Arial", 12, "italic")
    ).place(x = 242, y = 235)


# Следващите няколко кода са надписите къде са полетата, в които да въведем часовете, 
# минутите и секундите, за които искаме да настроим алармата.
addHr = Label(
    clock, 
    text = " Hour: ",
    font = ("Arial", 18, "bold"), 
    bg = "#8cd1fe"
    ).place(x = 228, y = 100)

addMn = Label(
    clock, 
    text = " Min: ", 
    font = ("Arial", 18, "bold"), 
    bg = "#8cd1fe"
    ).place(x = 314, y = 100)

# Бяхте предложили да махнем секундите, но по някаква причина без тях 
# алармата не се активира, затова ги оставихме.
addSc = Label(
    clock, 
    text = " Sec: ", 
    font = ("Arial", 18, "bold"), 
    bg = "#8cd1fe"
    ).place(x = 392, y = 100)


# Заглавието.
setYourAlarm = Label(
    clock, 
    text = " When to drink water: ", 
    bg = '#EEFCFF', 
    fg = "black", 
    relief = "sunken", 
    font = ("Arial", 32, "bold")
    ).place(x = 125, y = 30)


# Чрез следващите няколко реда създаваме полетета, в които да записваме времето за аларма.
hour = StringVar()
min = StringVar()
sec = StringVar()


hourTime = Entry(
    clock, 
    textvariable = hour, 
    bg = "#EEFCFF", 
    width = 6,
    font= ("Arial", 16),
    ).place(x = 230, y = 132)

minTime = Entry(
    clock, 
    textvariable = min, 
    bg = "#EEFCFF", 
    width = 6,
    font= ("Arial", 16),
    ).place(x = 310, y = 132)

secTime = Entry(
    clock, 
    textvariable = sec, 
    bg = "#EEFCFF", 
    width = 6,
    font= ("Arial", 16),
    ).place(x = 390, y = 132)


# Създаваме бутон, чиято функция е да стартира отброяването на часа през терминала и да пусне алармата.
submit = Button(
    clock, 
    text = " Set Alarm ", 
    fg = "black", 
    width = 12, 
    font = ("Arial", 14), 
    command = actual_time
    ).place(x = 280, y = 178)



# Тук е долната част от приложението.


# Надпис.
checker = Label(
    clock, 
    relief = "sunken", 
    bg = "#EEFCFF",
    text = " How much did you drink? ", 
    fg = "#000000", 
    font = ("Arial", 20, "bold")
    ).place(x = 170, y = 456)

# Първоначално се опитахме да променим този код, но не ни хареса как изглежда.
# def disp_mil():
#     Label(
#         text = f'Milliliters: {var.get()}', 
#         font = ('Arial', 16),
#         bg='#ffffff'
#         ).place(x = 50, y = 511)
# var = IntVar()

# Ако бяхме променили горния, щяхме да го използваме вместо този.
mil = Label(
    clock, 
    text = " Milliliters: ", 
    bg = "#EEFCFF",
    relief = "ridge", 
    font = ("Arial", 18), 
    ).place(x = 145, y = 510)

# Отбелязваме количеството, което сме изпили в милилитри.
# Честно казано, не върши особена работа за приложението, но изглежда добре :DD
sb = Spinbox(
    clock,
    bg = "#EEFCFF",
    width = 8,
    from_ = 0,
    to = 1000,
    increment = 50,
    format = '%8.0f',
    # textvariable = var,
    # command = disp_mil,
    font = ("Arial", 18)
).place(x = 268, y = 511)


# Създаваме бутон, който ще запазва информацията в текстови файл. 
# Информацията ще трябва да се въведе през терминалa.
# Може да се въведе до 1 ред информация. Ако искате да въведете повече или създавате 
# нов файл по същия начин, или отваряте вече съществуващия и въвеждате в него.
def saveFile():
    file = filedialog.asksaveasfile(defaultextension='.txt',
                                    filetypes=[
                                        ("Text file",".txt"),
                                        ("All files", ".*"),
                                    ])
    if file is None:
        return
    filetext = input("Enter milliliters: ") # console window
    file.write(filetext)
    file.close()

sub_mil = Button(
    clock, 
    # bg = ,
    text = " Check ✔ ", 
    fg = "#000000", 
    width = 10, 
    height = 0,
    font = ("Arial", 12), 
    command = (saveFile)
    ).place(x = 455, y = 510)


# Логото.
canvas = Canvas(
    clock, 
    width = 192, 
    height = 192,
    highlightbackground = "#8cd1fe", 
    )
canvas.pack()
canvas.place(x = 250, y = 260)
img = PhotoImage(file = 'logo200.png')
canvas.create_image(0, 0, anchor = NW, image = img)   


# Бутон за изход от приложението.
# По някаква причина работи само когато алармата не е активирана.
exit_button = Button(
    clock, 
    text = " Exit ", 
    fg = "#000000", 
    width = 6, 
    height = 0,
    font = ("Arial", 12), 
    command = clock.destroy
    ).place(x = 605, y = 545)


clock.mainloop()