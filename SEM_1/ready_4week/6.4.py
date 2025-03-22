import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.ticker import FixedFormatter

df = pd.read_csv('BTC_data.csv')
time = list(df['time'])
close = list(map(int,df['close']))
fig = plt.figure(figsize=(16,9))
a = fig.add_subplot()
x = [i for i in range(len(time))]
r=[time[i][:10] for i in range(0, max(x), 200)]
a.set_xlabel('Время', size=24)
a.set_ylabel('Стоимость', size=24)
a.set_xlim(0, max(x))
a.plot(x, close,label='График цены')
a.xaxis.set_major_formatter(FixedFormatter(r))
a.grid()
z = np.polyfit(x, close, 3)
p = np.poly1d(z)
y = [p(i) for i in x]
a.plot(x, y, 'r',label='аппроксимированная функция полиномом 3 степени')
z1 = np.polyfit(x, close, 10)
p1 = np.poly1d(z1)
y1 = [p1(i) for i in x]
a.plot(x, y1, 'g',label='аппроксимированная функция полиномом 10 степени')
z2 = np.polyfit(x, close, 30)
p2 = np.poly1d(z2)
y2 = [p2(i) for i in x]
a.plot(x, y2, 'b',label='аппроксимированная функция полиномом 30 степени')
a.legend(loc='upper left')


fig.show()