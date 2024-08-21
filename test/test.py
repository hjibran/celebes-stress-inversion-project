import numpy as np
import pandas as pd
'''
data = pd.read_csv("/mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Output/output_error.csv")

mini = np.min(data["stdev"])
print(np.max(data["stdev"]))
index = np.where(data["stdev"] == mini)[0][0]
print(index)

lo = data.query('stdev == {}'.format(mini))

print(lo)
'''

'''
store = np.array([[1, 0, 0.3], [1, 1, 0.2], [1, 2, .7]])
print(store)
def mini(store):
    mini = np.min(store, axis=0)
    print(mini[2])
    where = np.where(store == mini[2])
    print(where)
    index = where[0][0]
    print(index)
    minim = store[index]
    print(minim)
    return minim

y = mini(store)
print(y)

x = np.zeros([4, 3])


x[2] = y
print(x)

df = pd.DataFrame(x, columns=["cluster", "best seed", "stdev"])
print(df)
'''

'''
import sys
import os

strinv_dir = '/mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Programs_PYTHON'
if not strinv_dir in sys.path:
    sys.path.append(strinv_dir)

import pandas as pd
data = pd.read_csv("/mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Output/output_bootstarap.csv")
data = data["azimuth sigma 3"]

import numpy as np
import unify_direction as ud

dat, tempo = ud.unifying_direction(data)
# calculate error
mean_of_all_data = np.mean(tempo)
stdev = np.std(tempo)
percentil = ud.percentil(tempo)
half_of_95_percentil = np.float64((np.percentile(tempo, 97.5)-np.percentile(tempo, 2.5))/2)
data_in_percentil_range = [x for x in tempo if np.percentile(tempo, 2.5) <= x <= np.percentile(tempo, 97.5)]
mean_of_ci95_data = np.mean(data_in_percentil_range)
stdev_of_ci95 = np.std(data_in_percentil_range)
#result = pd.DataFrame(np.array([[mean_of_all_data, stdev, mean_of_ci95_data, stdev_of_ci95, np.float64(percentil[0]), np.float64(percentil[1]), half_of_95_percentil]]),
#                        columns=["mean of all data","stdev","mean of ci95 data","stdev of ci95","2.5%","97.5%","half width 95% percentil"])
print(np.percentile(tempo, [2.5, 97.5]))
print(data)
'''

"""
import pygmt

fig = pygmt.Figure()
fig.basemap(region=[0, 2, 0, 2], projection="x3c", frame=["xa1f0.2", "ya0.5f0.1"])

def shmax_plot(down, up):
    if down <=180:
        down1 = down+180
    elif down > 180:
        down1 = down -180
    if up <=180:
        up1 = up+180
    elif up > 180:
        up1 = up -180

    def project(azimuth):
        degree = 360-azimuth+90
        return degree

    data = [[1, 1, 2, 360-up+90, 360-down+90], [1, 1, 2, 360-up1+90, 360-down1+90]]
    fig.plot(data=data, style="w", fill="red", pen="1p, red")

shmax_plot(350,40)
fig.show()
"""

"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

arc1 = np.arange(-44,45, 1)
tan1 = np.tan(2*np.radians(arc1))
back_arc1 = np.degrees(np.arctan(tan1))/2

arc2 = np.arange(46,135, 1)
tan2 = np.tan(2*np.radians(arc2))
back_arc2 = np.degrees(np.arctan(tan2))/2

arc3 = np.arange(136,225, 1)
tan3 = np.tan(2*np.radians(arc3))
back_arc3 = np.degrees(np.arctan(tan3))/2

arc4 = np.arange(226,315, 1)
tan4 = np.tan(2*np.radians(arc4))
back_arc4 = np.degrees(np.arctan(tan4))/2

arc5 = np.arange(316,360.1, 1)
tan5 = np.tan(2*np.radians(arc5))
back_arc5 = np.degrees(np.arctan(tan5))/2
#data = np.array([arc, tan, back_arc])
#data = data.transpose()
#resutl = pd.DataFrame(data, columns=['arc', 'tan', 'back arc'])
#print(resutl)

plt.plot(arc1, tan1, "red")
plt.plot(arc2, tan2, "red")
plt.plot(arc3, tan3, "red")
plt.plot(arc4, tan4, "red")
plt.plot(arc5, tan5, "red")
plt.grid(True)
plt.show()

plt.plot(tan1, arc1, "red")
plt.plot(tan2, arc2, "red")
plt.plot(tan3, arc3, "red")
plt.plot(tan4, arc4, "red")
plt.plot(tan5, arc5, "red")
plt.grid(True)
plt.show()

plt.plot(arc1, back_arc1, "red")
plt.plot(arc2, back_arc2, "red")
plt.plot(arc3, back_arc3, "red")
plt.plot(arc4, back_arc4, "red")
plt.plot(arc5, back_arc5, "red")
plt.grid(True)
plt.show()
"""

color = ['navy', 'dodgerblue', 'deepskyblue', 'darkslategray',
         'darkgreen', 'red', 'chocolate', 'yellow', 'green',
         'darkbrown', 'orangered', 'black', 'magenta', 'gold4',
         'yellow4', 'chartreuse1', 'lightskyblue4', 'olivedrab1', 'springgreen4',
         'khaki1', 'khaki4', 'purple', 'cyan', 'firebrick2']

import random
print(type(random.choice(color)))