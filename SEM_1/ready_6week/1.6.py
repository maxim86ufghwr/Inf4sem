from tkinter import*
from tkinter import ttk
def calculate():
    label['text'] = (eval(form.get()))

root = Tk()
root.title("Calculator")
root.geometry("150x150")
root.minsize(100,100)
root.maxsize(200,200)

form = StringVar()
entry = ttk.Entry(width=20, textvariable=form)
entry.grid(column=0, row=1, sticky=(W, E, S, N))
button = ttk.Button(text='Посчитать', command=calculate)
button.grid(column=0, row=3, sticky=(W, E))
label = ttk.Label(text='None')
label.grid(column=0, row=2, sticky=(W, E))

root.mainloop()