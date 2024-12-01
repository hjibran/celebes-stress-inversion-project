#!/home/haidir/celebes-stress-inversion-project/venv/bin/python3
import pandas as pd
from sklearn.cluster import DBSCAN
import numpy as np
import os
import sys
import re
import pygmt
'''
10    10.0  1.10          0.475461
11    10.0  1.15          0.475058
32    15.0  1.35          0.475058
33    15.0  1.40          0.475058
'''

eps = 1.4
min = 4

data = pd.read_csv("/mnt/d/celebes-stress-inversion-project/data/siap-olah/fm50km7mw.csv") #data-tanpa-laut-maluku.csv")

x = data.iloc[:, [3, 2]]
clustering = DBSCAN(eps=eps, min_samples=min).fit(x)
data["cluster"] = clustering.labels_

fig = pygmt.Figure()
fig.basemap(region=[117.5, 127.5, -8.5, 5.5],
            frame=["a", "+teps{}min{}".format(eps, min)],
            projection="M20c"
)
fig.coast(shorelines='1p'
)
fig.plot(
    data="/mnt/d/celebes-stress-inversion-project/data/batas-lempeng-dan-patahan/indonesiafaults.gmt",
    pen="0.85p"
)
fig.plot(
    data="/mnt/d/celebes-stress-inversion-project/data/batas-lempeng-dan-patahan/trench.gmt",
    pen="1p",
    style="f1c/0.2c+l+t",
    fill="black"
)
color = ['gray', 'navy', 'dodgerblue', 'deepskyblue', 'darkslategray',
         'darkgreen', 'red', 'chocolate', 'yellow', 'green',
         'darkbrown', 'orangered', 'black', 'magenta', 'gold4',
         'yellow4', 'chartreuse1', 'lightskyblue4', 'olivedrab1', 'springgreen4',
         'khaki1', 'khaki4', 'purple', 'cyan', 'firebrick2',
         'navy', 'dodgerblue', 'deepskyblue', 'darkslategray',
         'darkgreen', 'red', 'chocolate', 'yellow', 'green',
         'darkbrown', 'orangered', 'black', 'magenta', 'gold4',
         'yellow4', 'chartreuse1', 'lightskyblue4', 'olivedrab1', 'springgreen4',
         'khaki1', 'khaki4', 'purple', 'cyan', 'firebrick2',
         'navy', 'dodgerblue', 'deepskyblue', 'darkslategray',
         'darkgreen', 'red', 'chocolate', 'yellow', 'green',
         'darkbrown', 'orangered', 'black', 'magenta', 'gold4',
         'yellow4', 'chartreuse1', 'lightskyblue4', 'olivedrab1', 'springgreen4',
         'khaki1', 'khaki4', 'purple', 'cyan', 'firebrick2',
         'navy', 'dodgerblue', 'deepskyblue', 'darkslategray',
         'darkgreen', 'red', 'chocolate', 'yellow', 'green',
         'darkbrown', 'orangered', 'black', 'magenta', 'gold4',
         'yellow4', 'chartreuse1', 'lightskyblue4', 'olivedrab1', 'springgreen4',
         'khaki1', 'khaki4', 'purple', 'cyan', 'firebrick2',
         'navy', 'dodgerblue', 'deepskyblue', 'darkslategray',
         'darkgreen', 'red', 'chocolate', 'yellow', 'green',
         'darkbrown', 'orangered', 'black', 'magenta', 'gold4',
         'yellow4', 'chartreuse1', 'lightskyblue4', 'olivedrab1', 'springgreen4',
         'khaki1', 'khaki4', 'purple', 'cyan', 'firebrick2'
]

file = []
c = 0
proses = 0
banyak_cluster = data["cluster"].max()
for kelas in range(-1, banyak_cluster+1):
    hasil = data[data["cluster"]==kelas]

    FM = hasil.iloc[:, [3, 2, 4, 6, 7, 8, 5]]
    FM.columns = ["longitude", "latitude", "depth", "strike", "dip", "rake", "magnitude"]
    fig.meca(
        spec=FM,
        compressionfill=color[c],
        scale="0.2c",
        extensionfill="white"
    )
    if kelas != -1:
        fig.text(
            x=sum(FM.longitude)/len(FM.longitude),
            y=sum(FM.latitude)/len(FM.latitude),
            text=kelas,#str(len(FM)),
            font="20p,red"
        )
    c += 1
    print(proses)
    proses += 1

fig.show()