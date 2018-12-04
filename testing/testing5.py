import numpy as np

def dice():
    x, y = np.random.randint(1,7,size = 2)
    eq = x + y > 10
    #print(eq)
    return eq

r = []
for i in np.arange(100000):
    re = dice()
    r.append(re)

ra = np.array(r)

print(ra.mean())
print(1/12)