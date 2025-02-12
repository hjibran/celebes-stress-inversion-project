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
   
    if 0 <= AR < 1:
        fill = "blue"
    elif 1 <= AR < 2:
        fill = "green"
    elif 2.0 <= AR < 3:
        fill = "red"
        
    data = [[lon, lat, 360-up+90, 360-down+90], [lon, lat, 360-up1+90, 360-down1+90]]
    fig.plot(data=data, style="w1c", fill=fill, cmap=False, transparency=25, pen="black")

def stress_ax(lon, lat, direction, regime):
    if regime == "C":
        fill = 'darkred'
    elif regime == "SS":
        fill = 'darkgreen'
    elif regime == "E":
        fill = 'darkblue'
    pen='2.75p,{}'.format(fill)
    length = 1
    style='v0.4c+ba'
    
    fig.plot(
        x=[lon],
        y=[lat],
        style=style,
        direction=[[-(direction-360)-90], [length]],
        pen=pen,
        fill=fill,
    )
    
    fig.plot(
        x=[lon],
        y=[lat],
        style=style,
        direction=[[-(direction-360)-90], [-length]],
        pen=pen,
        fill=fill,
    )

beaudouin = pd.read_csv('/mnt/d/celebes-stress-inversion-project/data/Beaudouin2003/Beaudouin-stress.csv')
table = pd.read_csv("/mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Output/shmax/shmax.csv")

table1 = table#table.query('name == 15.40')
table1 = table1.reset_index()

FM = table1.iloc[:, [2, 3, 4, 5, 6, 7, 11]]
FM.columns = ["longitude", "latitude", "depth", "strike", "dip", "rake", "magnitude"]

import pygmt
# begin fig object
fig = pygmt.Figure()

# download and store earth relief
grid = pygmt.datasets.load_earth_relief(resolution="30s", # resolution of earth relief
                                        region=[117.4, 129.6, -9.3, 6.7], # boarder of map: [minlon, maxlon, minlat, maxlat]
                                        registration="gridline")

# plot grid image
fig.grdimage(grid=grid, # call grid
             frame=["a", "EWSN"],#, "+tPulau Sulawesi"],
             projection="M10c",
             cmap= 'gray' #"/mnt/d/celebes-stress-inversion-project/generic-mapping-tools/script/color.cpt"
)
fig.coast(
    shorelines='1p,black'
)

os.system('gmt makecpt -Cdarkblue,blue,green,red,darkred -T0/3/0.02 -Z > /mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Output/shmax/custom.cpt')
sebaran = np.array([0,3])
pygmt.makecpt(cmap="/mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Output/shmax/custom.cpt", 
              series=[sebaran.min(), sebaran.max()])

for i in range(len(beaudouin)):
    stress_ax(beaudouin['lon'][i], beaudouin['lat'][i], beaudouin['Shmax'][i], beaudouin['Regime'][i])

for i in range(len(table1)):
    shmax_plot(table1['lon'][i], table1['lat'][i], table1['down'][i], table1['up'][i], table1['AR'][i])
    
fig.basemap(
    rose="jBR+w1.3c+lW,E,S,N+o0.3c/0.3c+f2"
) 

fig.show()