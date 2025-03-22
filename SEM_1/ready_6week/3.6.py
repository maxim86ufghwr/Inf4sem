from tkinter import *
from tkinter import ttk
import pandas as pd
import random as rd
films = pd.read_csv('imdb_top_250.csv')
film_genres_list = list(films['Genre'])

complex_genres = []
for film_genre in film_genres_list:
    genres = film_genre.split(' | ')
    if len(genres) > 1:
        for genre in genres:
            film_genres_list.append(genre)
        complex_genres.append(film_genre)

for genre in complex_genres:
    film_genres_list.remove(genre)

genres_set = set(film_genres_list)

root = Tk()
root.title("Случайный фильм")
root.geometry("400x200")
root.minsize(400, 200)
root.maxsize(400, 200)

def film():
    cor_f = genre_f.get()
    films_n = list(films['Title'])
    film_genres = list(films['Genre'])
    listr = []
    for i in range(len(film_genres)):
        if cor_f in film_genres[i]:
            listr.append(films_n[i])
    label['text'] = listr[rd.randint(0, len(listr)-1)]
    print(listr[rd.randint(0, len(listr)-1)],sep='\n')

genre_f = StringVar()

label = ttk.Label(text='', width=60)
entry = ttk.Entry(width=60, textvariable = genre_f)
label.grid(column=0, row=2)
entry.grid(column=0, row=0)

bu = ttk.Button(text='Выбрать фильм', command = film, width=60)
bu.grid(column=0, row=1)

root.mainloop()
