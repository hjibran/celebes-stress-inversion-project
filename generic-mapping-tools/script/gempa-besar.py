#!/home/haidir/celebes-stress-inversion-project/venv/bin/python3

import pygmt
import pandas as pd
import numpy as np

grid = pygmt.datasets.load_earth_relief(
    resolution="30s", region=[117.5, 127.5, -8.5, 5.5], registration="gridline"
)

fig = pygmt.Figure()
fig.basemap(
    frame=["a", "+tMw > 7.5"],
    projection="M20c"
)
#fig.grdimage(grid=grid, 
#             cmap="oleron"
#)
#fig.colorbar(
#    frame=["a3000f1000", "x+lElevation", "y+lm"]
#)
fig.coast(
    shorelines = "1p,grey"
)
fig.plot(
    data="/mnt/d/celebes-stress-inversion-project/data/batas-lempeng-dan-patahan/indonesiafaults.gmt", 
    pen="0.85p,grey"
)
fig.plot(
    data="/mnt/d/celebes-stress-inversion-project/data/batas-lempeng-dan-patahan/trench.gmt", 
    pen="1p,grey", 
    style="f1c/0.2c+l+t"
)

data = pd.read_csv('/mnt/d/celebes-stress-inversion-project/data/siap-olah/gempa-diatas-7.5.csv')
x = np.array(data.lon)
y = np.array(data.lat)
Mw = np.array(data.mw)
date = np.array(data.date)
atas = [0, 1, 3, 4, 6, 7, 9, 12, 13]
atas_kanan = [10]
atas_tengah = [5]
bawah = [2, 8, 11]
i = 0

while i < len(data):
    if i in atas:
        fig.plot(
            x = x[i],
            y = y[i],
            style = "a0.5c",
            fill= "red"
            )
        fig.text(
            x = x[i],
            y = y[i]+0.25,
            text = "Mw {} ({})".format(Mw[i], date[i]),
            font = "black"
            )
    elif i in atas_kanan:
        fig.plot(
            x = x[i],
            y = y[i],
            style = "a0.5c",
            fill= "red"
            )
        fig.text(
            x = x[i]-0.2,
            y = y[i]+0.25,
            text = "Mw {} ({})".format(Mw[i], date[i]),
            font = "black"
            )
    elif i in atas_tengah:
        fig.plot(
            x = x[i],
            y = y[i],
            style = "a0.5c",
            fill= "red"
            )
        fig.text(
            x = x[i]+0.25,
            y = y[i]+0.25,
            text = "Mw {} ({})".format(Mw[i], date[i]),
            font = "black"
            )
    elif i in bawah:
        fig.plot(
            x = x[i],
            y = y[i],
            style = "a0.5c",
            fill= "red"
            )
        fig.text(
            x = x[i],
            y = y[i]-0.2,
            text = "Mw {} ({})".format(Mw[i], date[i]),
            font = "black"
            )
    i += 1
    
    

fig.savefig("/mnt/d/celebes-stress-inversion-project/generic-mapping-tools/maps/gempa-besar.png")
