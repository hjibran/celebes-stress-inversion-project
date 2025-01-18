import numpy as np
import pandas as pd
import os

def shmax_plot(lon, lat, down, up, AR):
    if down <=180:
        down1 = down+180
    elif down > 180:
        down1 = down -180
    if up <=180:
        up1 = up+180
    elif up > 180:
        up1 = up -180
    '''
    if 0 <= AR < 0.25:
        fill = "darkblue"
    elif 0.25 <= AR < 0.75:
        fill = "blue"
    elif 0.75 <= AR < 1.25:
        fill = "green"
    elif 1.25 <= AR < 1.75:
        fill = "yellow"
    elif 1.75 <= AR < 2.25:
        fill = "orange"
    elif 2.25 <= AR < 2.75:
        fill = "red"
    else:
        fill = "darkred"
    '''
    if 0 <= AR < 1:
        fill = "blue"
    elif 1 <= AR < 2:
        fill = "green"
    elif 2.0 <= AR < 3:
        fill = "red"
    
    data = [[lon, lat, 360-up+90, 360-down+90], [lon, lat, 360-up1+90, 360-down1+90]]
    fig.plot(data=data, style="w2c", fill=fill, cmap=False, transparency=25, pen="black")

table = pd.read_csv("/mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Output/shmax/shmax_wilayah_laut_maluku.csv")

table1 = table#table.query('name == 15.40')
table1 = table1.reset_index()

FM = table1.iloc[:, [2, 3, 4, 5, 6, 7, 11]]
FM.columns = ["longitude", "latitude", "depth", "strike", "dip", "rake", "magnitude"]

import pygmt

fig = pygmt.Figure()

#grid = pygmt.datasets.load_earth_relief(resolution="30s", # resolution of earth relief
#                                        region=[117.5, 127.5, -8.5, 5.5], # boarder of map: [minlon, maxlon, minlat, maxlat]
#                                        registration="gridline")

#fig.grdimage(grid=grid, # call grid
#             frame=["a"],
#             projection="M20c",
#             cmap= "/mnt/d/celebes-stress-inversion-project/generic-mapping-tools/script/color.cpt")

fig.coast(region=[123.3, 129.5, -2.05, 5.3],
          projection='M10c',
          frame=["a1", "EWSN"],
          land='lightgray',
          resolution='f',
          #shorelines='0.25p,black,solid'
          )

fig.plot(
    data="/mnt/d/celebes-stress-inversion-project/data/batas-lempeng-dan-patahan/indonesiafaults.gmt", 
    pen="0.6p,darkgray",
    label="Patahan"
)
fig.plot(
    data="/mnt/d/celebes-stress-inversion-project/data/batas-lempeng-dan-patahan/trench.gmt", 
    pen="0.8p,darkgray", 
    style="f1c/0.2c+l+t", 
    fill="darkgray",
    label="Subduksi"
)

os.system('gmt makecpt -Cdarkblue,blue,green,red,darkred -T0/3/0.02 -Z > /mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Output/shmax/custom.cpt')
sebaran = np.array([0,3])
pygmt.makecpt(cmap="/mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Output/shmax/custom.cpt", 
              series=[sebaran.min(), sebaran.max()])

for i in range(len(table1)):
    shmax_plot(table1['lon'][i], table1['lat'][i], table1['down'][i], table1['up'][i], table1['AR'][i])

fig.basemap(rose="jBL+w1.2c+lW,E,S,N+o0.1c/0.1c+f2")

fig.show()