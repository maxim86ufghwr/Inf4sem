import numpy as np
def MNK(x,y):
    k = (np.mean(x*y) - np.mean(x)*np.mean(y)) / (np.mean(x**2) - np.mean(x)**2)
    print(round(k, 6))
    return round(k, 6)

x = np.array(list(map(float, input().split())))
y = np.array(list(map(float, input().split())))

def test(X,Y):
    assert len(X) == len(Y), f'massive X have size: {len(X)}, Y have size: {len(Y)} not equal sizes'
    h = MNK(X, Y)
    z = np.polyfit(X, Y, 1)
    assert round(h, 6) == round(z[0], 6), "MNK isn't right"
test(x,y)
