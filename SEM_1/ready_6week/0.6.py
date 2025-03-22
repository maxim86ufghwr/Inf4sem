from tkinter import *

root = Tk()  # создаем корневой объект - окно
root.title("Приложение на Tkinter")  # устанавливаем заголовок окна
root.geometry("300x300")  # устанавливаем размеры окна

label = Label(text="Hello")  # создаем текстовую метку
label.pack()  # размещаем метку в окне
#root.attributes("-fullscreen", True)

#icon = PhotoImage(file = "icon.png")
#root.iconphoto(False, icon)

root.mainloop()

from tkinter import *


def finish():
    root.destroy()  # ручное закрытие окна и всего приложения. обратите внимание, что к root обращаемся как к глобальной переменной
    print("App closed")


root = Tk()
root.geometry("250x200")

root.title("Hello")
root.protocol("WM_DELETE_WINDOW", finish)

root.mainloop()

from tkinter import *


# общий вид функции чтобы рекурсивно вывести информацию обо всех виджетах
# кстати, это хороший пример полиморфизма, поскольку виджеты мы можем передавать разные
def print_info(widget, depth=0):
    widget_class = widget.winfo_class()
    widget_width = widget.winfo_width()
    widget_height = widget.winfo_height()
    widget_x = widget.winfo_x()
    widget_y = widget.winfo_y()
    print("   " * depth + f"{widget_class} width={widget_width} height={widget_height}  x={widget_x} y={widget_y}")
    for child in widget.winfo_children():
        print_info(child, depth + 1)


root = Tk()
root.title("HELLO")
root.geometry("250x250")

btn = Button(text="Click")  # кстати, можем добавить параметр state=["disabled"], что сделает кнопку выключенной, пока мы не изменим параметр 'state'
btn.pack()

root.update()  # обновляем информацию о виджетах после их размещения, иначе это произойдет только с вызовом mainloop

print_info(root)  # получаем всю инфу о root. Поскольку у root есть только один виджет, вызовется информация о нем

root.mainloop()

from tkinter import *
from tkinter import ttk

root = Tk()
root.title("HELLO")
root.geometry("250x250")

btn = ttk.Button()
btn.pack()
# устанавливаем параметр text
btn["text"] = "Send"
# получаем значение параметра text
btnText = btn["text"]
print(btnText)

root.mainloop()

root = Tk()
root.geometry("500x250")

# функция нажатия на кнопку создает новый
# *args означает, что функция может принимать любое количество переменных.
def callback(*args):
   Label(root, text="Hello World!", font=('Montserrat 20 bold')).pack(pady=4) #обратите внимание, что обращаемся к root как к глобальной переменной
'''
ВАЖНО!
Вы передаете функцию в виджет как объект -- поэтому она пишется здесь без скобок.
Если напишете со скобками, то она вызовется один раз и передаст как команду результат вызова (в нашем случае -- ничего).
Протестируйте это.
'''
btn = Button(root, text="Press Enter", command = callback)
btn.pack(ipadx=50) #ipadx задает размер кнопки по x
# делает так, чтобы при нажатии на Enter (эквивалент команды Return) тоже выполнялось callback
root.bind('<Return>', callback)
root.mainloop()

from tkinter import *
from tkinter import ttk

# Задаем функцию пересчета. обратите внимание, что к feet и meters мы обращаемся как к глобальным переменным, в общем случае так делать нехорошо
# *args означает, что функция может принимать любое количество переменных. здесь они не используется, поэтому для общности написали так
def calculate(*args):
    try:
        value = float(feet.get())
        meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass

# Создадим основное окно приложения
root = Tk()
root.title("Feet to Meters")

'''
Зададим виджет Frame с названием mainframe, который будет содержать элементы нашего интерфейса.
После того, как мы создали его, grid() помещает его в окно приложения. 
columnconfigure/rowconfigure говорит что mainframe должен также расширяться
и занимать все свободное место при изменении размеров окна
'''
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

'''
Первый виджет Entry должен принимать количество футов.

Когда мы создаем виджет, нам нужно указать его родителя.
Это виджет, внутри которого будет размещен новый виджет.
Наша запись и другие виджеты, которые мы вскоре создадим, считаются дочерними элементами mainframe.
Родительский элемент передается в качестве первого параметра при создании экземпляра объекта виджета.

Также мы задали, что наше окно ввода должно иметь ширину под 7 символов.

Также мы создали глобальную переменную feet как textvariable для Entry. 
Когда ввод поменяется, Tkinter автоматически обновит feet. 
Для задания feet используется конструктор по умолчанию для таких переменных -- StringVar()

When widgets are created, they don't automatically appear on the screen; 
Tkinter должен знать куда вы хотите поместить виджеты относительно друг друга. 
За это отвечает функция grid. Она помещает содержимое в column (1, 2, or 3) и row (also 1, 2, or 3) окна.
sticky отвечает за то, по какой стороне будет выравнивание. W (west) означает запад, то есть левую сторону ячейки
W,E (west-east) означает и левую и правую сторону одновременно, то есть выравнивание посередине.
В Python определены константы для направлений компаса, поэтому вы можете писать просто W или (W, E).
'''
feet = StringVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

'''
Дальше создаем окно вывода. 
'''
meters = StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
'''
По нажатии на кнопку будем выполнять функцию calculate. Поскольку в ней уже прописаны операции напрямую с feet и meters,
то нам не нужно задавать какие-либо аргументы, функция автоматически положит нужное значение в meters и значение в 
определенном выше Label обновится.
'''
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

# косметические подписи, обратите внимание на расположение
ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

# этот цикл позволяет "разбросать" элементы подальше друг от друга
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

# сразу помещает курсор ввода в поле feet_entry
feet_entry.focus()
# делает так, чтобы при нажатии на Enter (эквивалент команды Return) тоже выполнялось calculate
root.bind("<Return>", calculate)

# циклим наше окно
root.mainloop()

import tkinter as Tkinter
from datetime import datetime

counter = 0
running = False


def counter_label(label):
    def count():
        if running:
            global counter
            # To manage the intial delay.
            if counter == 0:
                display = 'Ready!'
            else:
                tt = datetime.utcfromtimestamp(counter)
                string = tt.strftime('%H:%M:%S')
                display = string

            label['text'] = display

            label.after(1000, count) # каждые 1000мс = 1с увеличиваем счетчик на 1
            counter += 1

    #включаем count
    count()


# стартуем
def Start(label):
    global running
    running = True
    counter_label(label)
    start['state'] = 'disabled'
    stop['state'] = 'normal'
    reset['state'] = 'normal'


# тормозим
def Stop():
    global running
    start['state'] = 'normal'
    stop['state'] = 'disabled'
    reset['state'] = 'normal'
    running = False


# перезагружаемся
def Reset(label):
    global counter
    counter = 0
    # Если reset нажат после stop.
    if not running:
        reset['state'] = 'disabled'
        label['text'] = '00:00:00'
    # Если reset нажат во время работы таймера.
    else:
        label['text'] = '00:00:00'


root = Tkinter.Tk()
root.title("Stopwatch")

# Если окно будет слишком маленьким, будет сложно нажимать на кнопки, так что зададим minsize.
root.minsize(width=250, height=70)

label = Tkinter.Label(root, text='Ready!', fg='black', font='Montserrat 30 bold')
label.pack()
#создадим Frame, на который поместим кнопки
f = Tkinter.Frame(root)

'''
Помните в предыдущем примере мы говорили, что не получится передать в command функцию с круглыми скобками?
Но как быть, если мы хотим передать функцию, которая принимает какой-то аргумент? В нашем примере это Start и Reset
В данном случае мы можем сохранить **вызов** функции с каким-либо аргументом как отдельную функцию, используя ключевое слово lambda
Таким образом, вызова функции не происходит, а saved_start и saved_reset теперь -- объекты-функции, с фиксированным принимаемым аргументом.

В общем случае лямбда-функции это более мощный инструмент, однако пока мы не будем на этом останавливаться.
'''
saved_start = lambda: Start(label)
saved_reset = lambda: Reset(label)

start = Tkinter.Button(f, text='Start', width=6, command = saved_start)
stop = Tkinter.Button(f, text='Stop', width=6, state='disabled', command = Stop)
reset = Tkinter.Button(f, text='Reset', width=6, state='disabled', command = saved_reset)

# не забываем разместить Frame и кнопки
f.pack(anchor='center', pady=5)
start.pack(side='left')
stop.pack(side='left')
reset.pack(side='left')

root.mainloop()

from random import randint

WIDTH = 300
HEIGHT = 200


class Ball:
    def __init__(self):
        self.R = randint(10, 50) #храним размер, при каждом создании объекта будет выбираться случайно
        self.x = randint(self.R, WIDTH - self.R) # храним положение по x и y
        self.y = randint(self.R, HEIGHT - self.R)
        self.dx, self.dy = (10, 10) # это по сути шаг движения шаров. если увеличить -- будут двигаться быстрее
        self.ball_id = canvas.create_oval(self.x - self.R,
                                     self.y - self.R,
                                     self.x + self.R,
                                     self.y + self.R, fill="green") # при создании шарика отрисовываем его

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.x + self.R > WIDTH or self.x - self.R <= 0: # отражение от стенок
            self.dx = -self.dx
        if self.y + self.R > HEIGHT or self.y - self.R <= 0: # отр
            self.dy = -self.dy

    def show(self):
        canvas.move(self.ball_id, self.dx, self.dy)


def click_handler(event):
    print('Hello World! x=', event.x, 'y=', event.y)

#здесь мы уже привычно обращаемся к balls как к глобальной переменной. На самом деле дело в том, что нам лень писать классы.
def tick():
    for ball in balls:
        ball.move()
        ball.show()
    root.after(50, tick)


root = Tk()
root.geometry(f'{WIDTH}x{HEIGHT}')
canvas = Canvas(root)
canvas.pack()
#сделаем так, чтобы нажатие левой кнопки на поле выводило координаты точки, в которую мы нажали
canvas.bind('<Button-1>', click_handler)
balls = [Ball() for i in range(5)]
# делаем шаг перемещения и отрисовки шаров. поскольку mainloop циклит наше приложение, это будет происходить, пока мы не закроем окно
tick()
root.mainloop()