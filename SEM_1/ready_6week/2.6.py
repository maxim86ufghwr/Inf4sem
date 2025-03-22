from tkinter import*
from tkinter import ttk

def helth():
    er = int(we.get()) / (int((hi.get()))/100)**2
    label_re['text'] = er
    if er<=16:
        label_re2['text'] = 'Выраженный дефицит'
    elif 16<er<=18.5:
        label_re2['text'] = 'Недостаток'
    elif 18.5<er<=25:
        label_re2['text'] = 'Норма'
    elif 25<er<=30:
        label_re2['text'] = 'Избыток'
    elif 30<er<=35:
        label_re2['text'] = 'Ожирение 1 степени'
    elif 35<er<=40:
        label_re2['text'] = 'Ожирение 2 степени'
    elif er>=40:
        label_re2['text'] = 'Ожирение 3 степени'

root = Tk()
root.title("ИМТ")
root.geometry("300x300")
root.minsize(150,150)
root.maxsize(500,500)

we = StringVar()
hi = StringVar()

label_w = ttk.Label(text='Вес в кг')
entry_w = ttk.Entry(width=20, textvariable=we)
entry_w.grid(column=1, row=1, sticky=(W, E, S, N))
label_w.grid(column=0, row=1, sticky=(W, E, S, N))

label_h = ttk.Label(text='Рост в см')
entry_h = ttk.Entry(width=20, textvariable=hi)
entry_h.grid(column=1, row=2, sticky=(W, E, S, N))
label_h.grid(column=0, row=2, sticky=(W, E, S, N))

label_re = ttk.Label(text='None')
label_re.grid(column=0, row=3, sticky=(W, E, S, N))
label_re2 = ttk.Label(text='None')
label_re2.grid(column=1, row=3, sticky=(W, E, S, N))

bu=ttk.Button(text='Посчитать', command=helth)
bu.grid(column=2, row=4, sticky=(W, E, S, N))

root.mainloop()