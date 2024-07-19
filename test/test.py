import numpy as np
import random
from random import choice
import matplotlib.pyplot as plt
import plotly

banyak_data = 10
banyak_sebaran_hasil=250


def print_random():
    for i in range(banyak_data):
        print(random.randint(0, banyak_data))


def bootstrap(banyak_data, banyak_sebaran_hasil):
    rerata = []
    for i in range(banyak_sebaran_hasil):
        idxs_boot = np.array([random.randint(180, 275) for i in range(banyak_data)])
        rerata.append(sum(idxs_boot)/len(idxs_boot))
    return rerata

hasil_bootstrap = bootstrap(banyak_data, banyak_sebaran_hasil)

radians = np.linspace(0, ((2*np.pi)-(np.pi/180)), 360)
banyak = [random.randint(0, 15) for i in range(360)]

tinggi = []
for i in range(360):
    if i == 0:
        temp1 = [x for x in hasil_bootstrap if x < 0.5]
        temp2 = [x for x in hasil_bootstrap if 359.5 < x]
        n = len(temp1)+len(temp2)
    else:
        temp = [x for x in hasil_bootstrap if i-0.5 < x < i+0.5]
        n = len(temp)
    tinggi.append(n)

print(tinggi)
    

ax = plt.subplot(projection='polar')
ax.bar(radians, tinggi, width = np.pi/180)

plt.show()