import numpy as np
import pandas as pd
import os

def shmax_plot(lon, lat, down, up, fill):
    if down <=180:
        down1 = down+180
    elif down > 180:
        down1 = down -180
    if up <=180:
        up1 = up+180
    elif up > 180:
        up1 = up -180

    data = [[lon, lat, fill, 360-up+90, 360-down+90], [lon, lat, fill, 360-up1+90, 360-down1+90]]
    fig.plot(data=data, style="w1c", fill=fill, cmap=True)

table = pd.read_csv("/mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Output/shmax.csv")

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

fig.coast(region=[117.5, 127.5, -8.5, 5.5],
          projection='M10c',
          frame=["a", "EWSN"],
          land='lightgray',
          resolution='f',
          #shorelines='0.25p,black,solid'
          )

os.system('gmt makecpt -Cdarkblue,blue,green,red,darkred -T0/3/0.02 -Z > /mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Output/custom.cpt')
sebaran = np.array([0,3])
pygmt.makecpt(cmap="/mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Output/custom.cpt", 
              series=[sebaran.min(), sebaran.max()])

for i in range(len(table1)):
    shmax_plot(table1['lon'][i], table1['lat'][i], table1['down'][i], table1['up'][i], table1['AR'][i])

#fig.colorbar(frame=["x"],#"af+l'Depth (km)'", 
#             position="JMR+w10/0.5+o3/0c+mn+")#+w-3/0.25+o0.3/0.3c+mn+")


fig.show()