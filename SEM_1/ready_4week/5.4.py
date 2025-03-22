import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import FixedFormatter

df=pd.read_csv('BTC_data.csv')
time = list(df['time'])
close = list(map(int,df['close']))
fig = plt.figure(figsize=(16,9))
a = fig.add_subplot()
x = [i for i in range(len(time))]
r=[time[i][:10] for i in range(0, max(x), 200)]
a.set_xlabel('Время', size=24)
a.set_ylabel('Стоимость', size=24)
a.set_xlim(0, max(x))
a.plot(x,close)
a.xaxis.set_major_formatter(FixedFormatter(r))
a.grid()
fig.show()