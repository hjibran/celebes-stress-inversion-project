import numpy as np
import pandas as pd
import os
import pygmt

def inset(R):
    x = [R[0], R[1], R[1], R[0], R[0]]
    y = [R[2], R[2], R[3], R[3], R[2]]
    return x, y

fig = pygmt.Figure()
region=[117.4, 129.6, -9.3, 6.7]
grid = pygmt.datasets.load_earth_relief(resolution="30s", # resolution of earth relief
                                        registration="gridline",
                                        region=region,
                                        )

fig.grdimage(grid=grid,
             projection='M10c',
             frame=["a2", "EWSN"],
             cmap= 'oleron')#"/mnt/d/celebes-stress-inversion-project/generic-mapping-tools/script/color.cpt")

#fig.coast(region=region,
#          #land='lightgray',
#          resolution='f',
#          water='white'
#          #shorelines='0.25p,black,solid'
#          )

fig.plot(
    data="/mnt/d/celebes-stress-inversion-project/data/batas-lempeng-dan-patahan/indonesiafaults.gmt", 
    pen="0.6p,black",#dimgray",
    label="Patahan"
)
fig.plot(
    data="/mnt/d/celebes-stress-inversion-project/data/batas-lempeng-dan-patahan/trench.gmt", 
    pen="0.8p,black",#dimgray", 
    style="f1c/0.2c+l+t", 
    fill="black",#dimgray",
    label="Subduksi"
)

utara=[117.5, 126, -5, 3.5]
selatan=[118.5, 123, -4.5, -1.7]
maluku=[123.3, 129.5, -2.05, 5.3]
sula=[125.5, 128, -3.5, -2.25]
sangihe=[124.4, 126.9, 4, 6.6]
ntt=[124.2, 126.8, -9.2, -7.2]

x, y = inset(ntt)
fig.plot(x=x,
         y=y,
         pen='2p,darkred'
)

fig.basemap(rose="jTL+w1.2c+lW,E,S,N+o0.1c/0.1c+f2") 

fig.show()
