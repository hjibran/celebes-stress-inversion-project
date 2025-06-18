import numpy as np
import pandas as pd
import geopandas as gpd
import os

# Peruntukan 'shmax' /  'sebaran data'
untuk = 'sebaran data'
# 'A-B' / 'A-D'
quality = 'A-D'

# Membuat fungsi plot shmax
def shmax_plot(lon, lat, down, up, fill):
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
    """ 
    if 0 <= AR < 1:
        fill = "blue"
    elif 1 <= AR < 2:
        fill = "green"
    elif 2.0 <= AR < 3:
        fill = "red" """
    
    data = [[lon, lat, 360-up+90, 360-down+90], [lon, lat, 360-up1+90, 360-down1+90]]
    fig.plot(data=data, style="w3c", fill=fill, cmap=False, transparency=25, pen="black")

# Memasukkan data hasil inversi before after
table = pd.read_csv("/mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Output/eps0.40pts15/new_shmax/palukoro-with-data-kusumawati/shmax.csv", comment='#')

if quality == 'A-B':
    table1 = table.query('quality == "A-B"')
    table1 = table1.reset_index()
elif quality == 'A-D':
    table1 = table.query('quality == "A-D"')
    table1 = table1.reset_index()

FM = table1.iloc[:, [2, 3, 4, 5, 6, 7, 11]]
FM.columns = ["longitude", "latitude", "depth", "strike", "dip", "rake", "magnitude"]

# Memasukkan data sebaran kejadian gempa sebelum dan setelah Gempa palu 2018
if quality == 'A-B':
    databefore = pd.read_csv('/mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Output/eps0.40pts15/new_shmax/palukoro-with-data-kusumawati/datawithkusumawati(A-B)before.csv')
    FMbefore = databefore.iloc[:, [3, 2, 4, 6, 7, 8, 5]]
    FMbefore.columns = ["longitude", "latitude", "depth", "strike", "dip", "rake", "magnitude"]
    dataafter = pd.read_csv('/mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Output/eps0.40pts15/new_shmax/palukoro-with-data-kusumawati/datawithkusumawati(A-B)after.csv')
    FMafter = dataafter.iloc[:, [3, 2, 4, 6, 7, 8, 5]]
    FMafter.columns = ["longitude", "latitude", "depth", "strike", "dip", "rake", "magnitude"]
elif quality == 'A-D':
    databefore = pd.read_csv('/mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Output/eps0.40pts15/new_shmax/palukoro-with-data-kusumawati/datawithkusumawati(A-D)before.csv')
    FMbefore = databefore.iloc[:, [3, 2, 4, 6, 7, 8, 5]]
    FMbefore.columns = ["longitude", "latitude", "depth", "strike", "dip", "rake", "magnitude"]
    dataafter = pd.read_csv('/mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Output/eps0.40pts15/new_shmax/palukoro-with-data-kusumawati/datawithkusumawati(A-D)after.csv')
    FMafter = dataafter.iloc[:, [3, 2, 4, 6, 7, 8, 5]]
    FMafter.columns = ["longitude", "latitude", "depth", "strike", "dip", "rake", "magnitude"]

# Mulai melakukan plot
import pygmt
fig = pygmt.Figure()

# Mengimport data relief
grid = pygmt.datasets.load_earth_relief(resolution="30s", # resolution of earth relief
                                        registration="gridline",
                                        region=[120.12075806451612-1.5, 120.12075806451612+1.5, -1.1031451612903227-1.5, -1.1031451612903227+1.5],
                                        )
# Plot data relief
fig.grdimage(grid=grid,
             projection='M10c',
             frame=["a2", "EWSN"],
             cmap= "/mnt/d/celebes-stress-inversion-project/generic-mapping-tools/script/color.cpt")

# Menimpah data relief dengan laut berwarna putih
fig.coast(region=[120.12075806451612-1.5, 120.12075806451612+1.5, -1.1031451612903227-1.5, -1.1031451612903227+1.5],
          #land='lightgray',
          resolution='f',
          water='white'
          #shorelines='0.25p,black,solid'
          )

# Input data patahan
fig.plot(
    data="/mnt/d/celebes-stress-inversion-project/data/batas-lempeng-dan-patahan/indonesiafaults.gmt", 
    pen="0.6p,dimgray",
    label="Patahan"
)

# Input data Trench
fig.plot(
    data="/mnt/d/celebes-stress-inversion-project/data/batas-lempeng-dan-patahan/trench.gmt", 
    pen="0.8p,dimgray", 
    style="f1c/0.2c+l+t", 
    fill="dimgray",
    label="Subduksi"
)

# Input data buffer cluster palu
bufferpalu = gpd.read_file("/mnt/d/celebes-stress-inversion-project/Result/eps0.40min15-final/eps0.40pts15-Palu.shp")
if untuk == 'sebaran data':
    fig.plot(data=bufferpalu, pen="1.5p,black,--")#, label="ε=0.50 MinPts=15")

if untuk != 'shmax':
       #Plot Data Focal Mechanisme
    fig.meca(spec=FMbefore,
             compressionfill='red', # cmap = True,
             pen="0.5p,black,solid",
             scale ="0.25c",
             frame = True)
  
    fig.meca(spec=FMafter,
             compressionfill='black', # cmap = True,
             pen="0.5p,black,solid",
             scale ="0.25c",
             frame = True)
    
    
# Plot Shmax
if untuk == 'shmax':
    for i in range(len(table1)):

        if table1['name'][i] == 'before':
            color = 'red'
        elif table1['name'][i] == 'after':
            color = 'black'
            
        shmax_plot(table1['lon'][i], table1['lat'][i], table1['down'][i], table1['up'][i], color)

fig.basemap(rose="jBL+w1.2c+lW,E,S,N+o0.1c/0.1c+f2") 

fig.show()