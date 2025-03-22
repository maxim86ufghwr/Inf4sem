import matplotlib.pyplot as plt
import numpy as np
from matplotlib.gridspec import GridSpec
import math
# Посчёт всех значений по разным t
with open('эксперимент_2023-09-13_14-18-50.txt', 'r') as f:
    a = f.readlines()
b = []
for i in range(len(a)):
    if a[i][0] != '#':
        b.append(int(a[i]))
t10 = []
t20 = []
t40 = []
t80 = []
print(sum(b[0:5]))
for i in range(len(b)//10):
    t10.append(sum(b[i*10: (i+1)*10]))
    if i % 2 == 0:
        t20.append(sum(b[i * 10: (i+2)*10]))
    if i % 4 == 0:
        t40.append(sum(b[i * 10: (i + 4) * 10]))
    if i % 8 == 0:
        t80.append(sum(b[i * 10: (i + 8) * 10]))
print(b, t10, t20, t40, t80, sep='\n')

bno=0
bj=(sum(b)/len(b))/1
bjd=0
for i in range(len(b)):
    bno+=(b[i]-(sum(b)/len(b)))**2
    bjd+=(b[i]/1 - bj)**2
print(f'sred-{sum(b)/len(b):5},otkl-{np.sqrt(bno/len(b)):5},otnoh-{np.sqrt(bno/len(b))/np.sqrt(len(b)):5}')
print(f'j-{bj},jd-{np.sqrt(bjd/len(b))}')

t10no=0
t10j=(sum(t10)/len(t10))/10
t10jd=0
for i in range(len(t10)):
    t10no+=(t10[i]-(sum(t10)/len(t10)))**2
    t10jd+=(t10[i]/10 - t10j)**2
print(f'sred-{sum(t10)/len(t10):5},otkl-{np.sqrt(t10no/len(t10)):5},otnoh-{np.sqrt(t10no/len(t10))/np.sqrt(len(t10)):5}')
print(f'j-{t10j},jd-{np.sqrt(t10jd/len(b))}')

t20no=0
t20j=(sum(t20)/len(t20))/20
t20jd=0
for i in range(len(t20)):
    t20no+=(t20[i]-(sum(t20)/len(t20)))**2
    t20jd+=(t20[i]/20 - t20j)**2
print(f'sred-{sum(t20)/len(t20):5},otkl-{np.sqrt(t20no/len(t20)):5},otnoh-{np.sqrt(t20no/len(t20))/np.sqrt(len(t20)):5}')
print(f'j-{t20j},jd-{np.sqrt(t20jd/len(t20))}')

t40no=0
t40j=(sum(t40)/len(t40))/40
t40jd=0
for i in range(len(t40)):
    t40no+=(t40[i]-(sum(t40)/len(t40)))**2
    t40jd+=(t40[i]/40 - t40j)**2
print(f'sred-{sum(t40)/len(t40):5},otkl-{np.sqrt(t40no/len(t40)):5},otnoh-{np.sqrt(t40no/len(t40))/np.sqrt(len(t40)):5}')
print(f'j-{t40j},jd-{np.sqrt(t40jd/len(t40))}')

t80no=0
t80j=(sum(t80)/len(t80))/80
t80jd=0
for i in range(len(t80)):
    t80no+=(t80[i]-(sum(t80)/len(t80)))**2
    t80jd+=(t80[i]/80 - t80j)**2
print(f'sred-{sum(t80)/len(t80):5},otkl-{np.sqrt(t80no/len(t80)):5},otnoh-{np.sqrt(t80no/len(t80))/np.sqrt(len(t80)):5}')
print(f'j-{t80j},jd-{np.sqrt(t80jd/len(t80))}')

fig = plt.figure(figsize=(12, 12))
fig.suptitle('Измерение радиоактивного фона', size=24)
gs = GridSpec(ncols=1, nrows=3, figure=fig)
ax10 = plt.subplot(gs[1, 0])
x = [i for i in range(min(t10),max(t10)+1)]
y = [t10.count(i) for i in range(min(t10),max(t10)+1)]
ax10.bar(x,y,yerr=np.sqrt(y))
plt.title('t=10 c', fontdict={'fontname': 'sans-serif', 'fontsize': 20})
ty10=[]
for i in range(min(t10), max(t10)+1):
    ty10.append((sum(t10)/10 /(np.sqrt(2*np.pi)*np.std(t10)))*np.exp(-1*(i-np.mean(t10))**2/(2*(np.std(t10))**2)))
ax10.plot(x,ty10,color='black', label='Распределение Гаусса')
ty10p=[]
for i in range(min(x),max(x)+1):
    ty10p.append((sum(t10)/10)*(((np.mean(t10)**i)/math.factorial(i))*np.exp(-np.mean(t10))))
ax10.plot(x,ty10p,color='red',label='Распределение Пуассона')
ax10.grid()
ax10.legend(loc='upper right')

ax20 = plt.subplot(gs[2, 0])
x = [i for i in range(min(t20),max(t20)+1)]
y = [t20.count(i) for i in range(min(t20),max(t20)+1)]
ax20.bar(x, y, yerr=np.sqrt(y))
plt.title('t=20c', fontdict={'fontname': 'sans-serif', 'fontsize': 20})
ty20=[]
for i in range(min(t20),max(t20)+1):
    ty20.append((sum(t20)/20 / (np.sqrt(2 * np.pi) * np.std(t20))) * np.exp(-1 * (i - np.mean(t20)) ** 2 / (2 * (np.std(t20)) ** 2)))
ax20.plot(x, ty20, color='black', label='Распределение Гаусса')
ty20p=[]
for i in range(min(x),max(x)+1):
    ty20p.append((sum(t20)/20)*(((np.mean(t20)**i)/math.factorial(i))*np.exp(-np.mean(t20))))
ax20.plot(x,ty20p,color='red',label='Распределение Пуассона')
ax20.grid()
ax20.legend(loc='upper right')

ax_t = plt.subplot(gs[0, 0])
x = [i for i in range(min(b),max(b)+1)]
y = [b.count(i) for i in range(min(b),max(b)+1)]
ax_t.bar(x, y, yerr=np.sqrt(y))
plt.title('t=1c', fontdict={'fontname': 'sans-serif', 'fontsize': 20})
ty1=[]
for i in range(min(b),max(b)+1):
    ty1.append((sum(b)/(np.sqrt(2*np.pi)*np.std(b))) * np.exp(-1*(i-np.mean(b))**2/(2*(np.std(b))**2)))
ax_t.plot(x,ty1,color='black', label='Распределение Гаусса')
ty1p=[]
for i in range(min(x),max(x)+1):
    ty1p.append((sum(b)/1)*(((np.mean(b)**i)/math.factorial(i))*np.exp(-np.mean(b))))
ax_t.plot(x,ty1p,color='red',label='Распределение Пуассона')
ax_t.grid()
ax_t.legend(loc='upper right')

fig_1 = plt.figure(figsize=(12, 12))
fig_1.suptitle('Измерение радиоактивного фона', size=24)
gs1 = GridSpec(ncols=1, nrows=2, figure=fig_1)

ax40 = plt.subplot(gs1[0, 0])
x = [i for i in range(min(t40),max(t40)+1)]
y = [t40.count(i) for i in range(min(t40),max(t40)+1)]
ax40.bar(x, y, yerr=np.sqrt(y))
plt.title('t=40c', fontdict={'fontname': 'sans-serif', 'fontsize': 20})
ty40=[]
for i in range(min(t40),max(t40)+1):
    ty40.append((sum(t40)/40/(np.sqrt(2*np.pi)*np.std(t40))) * np.exp(-1*(i-np.mean(t40))**2/(2*(np.std(t40))**2)))
ax40.plot(x,ty40,color='black', label='Распределение Гаусса')
ty40p=[]
for i in range(min(x),max(x)+1):
    ty40p.append((sum(t40)/40)*(((np.mean(t40)**i)/math.factorial(i))*np.exp(-np.mean(t40))))
ax40.plot(x,ty40p,color='red',label='Распределение Пуассона')
ax40.grid()
ax40.legend(loc='upper right')

ax80 = plt.subplot(gs1[1, 0])
x = [i for i in range(min(t80),max(t80)+1)]
y = [t80.count(i) for i in range(min(t80),max(t80)+1)]
ax80.bar(x, y, yerr=np.sqrt(y))
plt.title('t=80c', fontdict={'fontname': 'sans-serif', 'fontsize': 20})
ty80=[]
for i in range(min(t80),max(t80)+1):
    ty80.append((sum(t80)/80/(np.sqrt(2*np.pi)*np.std(t80))) * np.exp(-1*(i-np.mean(t80))**2/(2*(np.std(t80))**2)))
ax80.plot(x,ty80,color='black', label='Распределение Гаусса')
ty80p=[]
for i in range(min(x),max(x)+1):
    ty80p.append((sum(t80)/80)*(((np.mean(t80)**i)/math.factorial(i))*np.exp(-np.mean(t80))))
ax80.plot(x,ty80p,color='red',label='Распределение Пуассона')
ax80.grid()
ax80.legend(loc='upper right')

fig_2 = plt.figure(figsize=(12, 9))
fig_2.suptitle('Качественное наблюдение', size=24)
gs = GridSpec(ncols=1, nrows=1, figure=fig_2)

axsr = plt.subplot(gs[0, 0])
asr=[]
sasr=[]
s=0
for i in range(len(b)):
    s += b[i]
    asr.append(s/(i+1))
    sasr.append(np.sqrt(s/(i+1)))
axsr.plot(asr, label='<n>')
axsr.plot(sasr,'g--', label='√n')
axsr.set_xlim(0, 4000)
axsr.set_xlabel('Количество измерений')
axsr.set_ylabel('Среднее значение и среднеквадратичное отклонение')

asro = []
v = 0
for i in range(len(b)):
    v += (b[i] - asr[i])**2
    asro.append(np.sqrt(v/(i+1)))
axsr.plot(asro, 'r', label='σn')
axsr.grid()
axsr.legend(loc='lower right')

fig_3 = plt.figure(figsize=(12, 12))
fig_3.suptitle('Измерение радиоактивного фона', size=24)
gs3 = GridSpec(ncols=1, nrows=2, figure=fig_3)

ax10_20 = plt.subplot(gs3[0, 0])
x10 = np.array([i for i in range(min(t10),max(t10)+1)])
y10 = np.array([t10.count(i) for i in range(min(t10),max(t10)+1)])
x20 = np.array([i for i in range(min(t20),max(t20)+1)])
y20 = np.array([t20.count(i) for i in range(min(t20),max(t20)+1)])
w = 0.3
ax10_20.bar(x10-w/2, y10, width=w, label='10 c',yerr=np.sqrt(y10))
ax10_20.bar(x20+w/2, y20, width=w, label='20 c',yerr=np.sqrt(y20))
plt.title('t=10c и 20с', fontdict={'fontname': 'sans-serif', 'fontsize': 20})
ax10_20.plot(x10,ty10,color='cyan')
ax10_20.plot(x20,ty20,color='red')
ax10_20.grid()
ax10_20.legend(loc='upper right')

ax40_80 = plt.subplot(gs3[1, 0])
x40 = np.array([i for i in range(min(t40),max(t40)+1)])
y40 = np.array([t40.count(i) for i in range(min(t40),max(t40)+1)])
x80 = np.array([i for i in range(min(t80),max(t80)+1)])
y80 = np.array([t80.count(i) for i in range(min(t80),max(t80)+1)])
w=0.8
ax40_80.bar(x40-w/2, y40, width=w, label='40 c',yerr=np.sqrt(y40))
ax40_80.bar(x80+w/2, y80, width=w, label='80 c',yerr=np.sqrt(y80))
plt.title('t=40c и 80c', fontdict={'fontname': 'sans-serif', 'fontsize': 20})
ax40_80.plot(x40,ty40,color='cyan')
ax40_80.plot(x80,ty80,color='red')
ax40_80.grid()
ax40_80.legend(loc='upper right')

plt.show()

for i in range(min(b),max(b)+1):
    print(f'значение {i} встречается {b.count(i)}')
print('t=10')
for i in range(min(t10),max(t10)+1):
    print(f'значение {i} встречается {t10.count(i)}')
print('t=20')
for i in range(min(t20),max(t20)+1):
    print(f'значение {i} встречается {t20.count(i)}')
print('t=40')
for i in range(min(t40),max(t40)+1):
    print(f'значение {i} встречается {t40.count(i)}')
print('t=80')
for i in range(min(t80),max(t80)+1):
    print(f'значение {i} встречается {t80.count(i)}')

b_r=np.array([0,0,0])
t10_r=np.array([0,0,0])
t20_r=np.array([0,0,0])
t40_r=np.array([0,0,0])
t80_r=np.array([0,0,0])
for i in range(len(b)):
    if np.abs(b[i]-np.mean(b)) < np.std(b):
        b_r[0]+=1
    if np.abs(b[i]-np.mean(b)) < 2*np.std(b):
        b_r[1]+=1
    if np.abs(b[i]-np.mean(b)) < 3*np.std(b):
        b_r[2]+=1
for i in range(len(t10)):
    if np.abs(t10[i]-np.mean(t10)) < np.std(t10):
        t10_r[0]+=1
    if np.abs(t10[i]-np.mean(t10)) < 2*np.std(t10):
        t10_r[1]+=1
    if np.abs(t10[i]-np.mean(t10)) < 3*np.std(t10):
        t10_r[2]+=1
for i in range(len(t20)):
    if np.abs(t20[i]-np.mean(t20)) < np.std(t20):
        t20_r[0]+=1
    if np.abs(t20[i]-np.mean(t20)) < 2*np.std(t20):
        t20_r[1]+=1
    if np.abs(t20[i]-np.mean(t20)) < 3*np.std(t20):
        t20_r[2]+=1
for i in range(len(t40)):
    if np.abs(t40[i]-np.mean(t40)) < np.std(t40):
        t40_r[0]+=1
    if np.abs(t40[i]-np.mean(t40)) < 2*np.std(t40):
        t40_r[1]+=1
    if np.abs(t40[i]-np.mean(t40)) < 3*np.std(t40):
        t40_r[2]+=1
for i in range(len(t80)):
    if np.abs(t80[i]-np.mean(t80)) < np.std(t80):
        t80_r[0]+=1
    if np.abs(t80[i]-np.mean(t80)) < 2*np.std(t80):
        t80_r[1]+=1
    if np.abs(t80[i]-np.mean(t80)) < 3*np.std(t80):
        t80_r[2]+=1
print(b_r/len(b),t10_r/len(t10),t20_r/len(t20),t40_r/len(t40),t80_r/len(t80),sep='\n')
