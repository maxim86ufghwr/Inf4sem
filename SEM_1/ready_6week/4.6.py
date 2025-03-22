from tkinter import *
from tkinter import ttk

c = '0123456789abcdef'

root = Tk()
root.title("Подбор цветов")
root.geometry("400x200")
root.minsize(150, 150)
root.maxsize(500, 500)

def color():
    colo = cll.get()
    if len(colo) == 6:
        label_a2['background'] = '#'+colo
        reo = ''
        for i in range(3):
            reo += hex(255 - int(colo[2*i:2*(i+1)], 16))[2:]
            print(hex(255 - int(colo[2*i:2*(i+1)], 16)))
            if len(reo) % 2 == 1:
                reo = '0' + reo
        label_re2['background'] = '#'+reo

cll = StringVar()

label_w = ttk.Label(text='Введёный цвет (без #)')
entry_w = ttk.Entry(width=20, textvariable=cll)
entry_w.grid(column=0, row=1)
label_w.grid(column=0, row=0)
label_a2 = ttk.Label(text='None',background='#ffffff', width=30)
label_a2.grid(column=0, row=2)

label_re = ttk.Label(text='Результат')
label_re.grid(column=1, row=0)
label_re2 = ttk.Label(text='',background='#ffffff', width=30)
label_re2.grid(column=1, row=1)

bu = ttk.Button(text='Посчитать', command=color)
bu.grid(column=0, row=3)



root.mainloop()