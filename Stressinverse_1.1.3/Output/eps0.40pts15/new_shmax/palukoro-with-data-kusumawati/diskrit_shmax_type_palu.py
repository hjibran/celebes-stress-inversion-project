import numpy as np
import pandas as pd
import geopandas as gpd
import os

# Peruntukan 'shmax' /  'sebaran data'
untuk = 'shmax'
# 'A-B' / 'A-D'
quality = 'A-B'

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
             cmap= "/mnt/d/celebes-stress-inversion-project/generic-mapping-tools/script/color.cpt",
             shading = True
)

# Menimpah data relief dengan laut berwarna putih
fig.coast(region=[120.12075806451612-1.5, 120.12075806451612+1.5, -1.1031451612903227-1.5, -1.1031451612903227+1.5],
          #land='lightgray',
          #resolution='f',
          #water='white'
          shorelines='1.5p,dimgray,solid'
          )

'''
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
)'''

def struktur(size, color):

    a = size * 2 
    a1 = size * 1.5
    b = size * 1
    c = size * 0.9
    d = size * 0.8
    e = size * 0.4

    dir='/mnt/d/celebes-stress-inversion-project/data/GMT_Seismotectonics_of_Sulawesi/'
    in_fault1='strikeslipsulawesihall.gmt'
    in_fault2='strikeslipsulawesi2.gmt'
    in_thrust='thrustsulawesi.gmt'
    in_thrust1='batuithrust.gmt'
    in_subduct='sulawesisubduksihall.gmt'
    in_normalup='mmcup.gmt'
    in_normaldown='mmcdown.gmt'
    in_sesar='sesar.gmt'
    in_tambah='jd.gmt'
    gtox='gorotaloextension.gmt'

    mat='mat.gmt'
    hf='hf.gmt'
    law1='law1.gmt'
    tolo='tolo.gmt'
    pf='pf1.gmt'
    pff='pff.gmt'
    tf='tf.gmt'
    tf1='tf1.gmt'
    tf2='tf2.gmt'
    nf='nf.gmt'
    nf1='nf1.gmt'
    sf='sf.gmt'
    pan='pann.gmt'
    pan3='pan3.gmt'
    tam='tam.gmt'

    fig.plot(data=dir+in_subduct, style='f2/0.15i+l+t', pen="{}p,{}".format(a, color), fill=color)
    fig.plot(data=dir+'strikewalane.gmt', style='f5c/0.6c+l+s45+o0.60c', pen="{}p,{}".format(c, color))
    fig.plot(data=dir+'tambahanbaru1.gmt', pen="{}p,{}".format(c, color))
    fig.plot(data=dir+'walanethrust.gmt', style='f0.6/0.1i+l+t', pen="{}p,{}".format(c, color))
    fig.plot(data=dir+'butonthrust.gmt', style='f0.6/0.1i+r+t', pen="{}p,{}".format(c, color))
    fig.plot(data=dir+in_sesar, pen="{}p,{}".format(c, color))
    fig.plot(data=dir+in_tambah, style='f4c/0.6c+l+s45+o2.25c', pen="{}p,{}".format(c, color))
    fig.plot(data=dir+'jd1.gmt', style='f4c/0.6c+r+s45+o0.90c', pen="{}p,{}".format(c, color))
    fig.plot(data=dir+in_fault1, style='f4c/1c+l+s45+o2.25c', pen="{}p,{}".format(a, color))
    fig.plot(data=dir+in_fault2, pen="{}p,{},-".format(b, color))
    fig.plot(data=dir+in_thrust, style='f1/0.1i+l+t', pen="{}p,{}".format(b, color))
    fig.plot(data=dir+tolo, style='f1/0.1i+r+t', pen="{}p,{}".format(b, color))
    fig.plot(data=dir+in_thrust1, style='f1/0.1i+r+t', pen="{}p,{}".format(b, color))
    fig.plot(data=dir+pf, pen="{}p,{},-".format(b, color))
    fig.plot(data=dir+in_normalup, style='f0.5/0.05i+l+b', pen="{}p,{}".format(d, color), fill=color)
    fig.plot(data=dir+in_normaldown, style='f0.5/0.05i+r+b', pen="{}p,{}".format(d, color), fill=color)

    fig.plot(data=dir+'weluki.gmt', style='f1/0.05i+l+t', pen="{}p,{}".format(d, color))
    fig.plot(data=dir+'hal_dip.gmt', style='f2/0.15i+l+t', pen="{}p,{}".format(a, color), fill=color)
    fig.plot(data=dir+'hal_dip1.gmt', style='f2/0.15i+r+t', pen="{}p,{}".format(a, color), fill=color)
    fig.plot(data=dir+gtox, pen="{}p,{}".format(e, color))

    fig.plot(data=dir+mat, style='f4c/0.6c+l+s45+o2.25c', pen="{}p,{}".format(a1, color))
    fig.plot(data=dir+pff, pen="{}p,{},-".format(b, color))
    fig.plot(data=dir+sf, pen="{}p,{}".format(b, color))
    fig.plot(data=dir+tf, style='f0.6/0.1i+l+t', pen="{}p,{}".format(d, color))
    fig.plot(data=dir+tf1, style='f0.6/0.1i+r+t', pen="{}p,{}".format(d, color))
    fig.plot(data=dir+tf2, style='f0.6/0.1i+r+t', pen="{}p,{}".format(d, color))
    fig.plot(data=dir+hf, style='f5c/0.6c+l+s45+o1.25c', pen="{}p,{}".format(c, color))
    fig.plot(data=dir+nf, style='f0.5/0.05i+l+b', pen="{}p,{}".format(d, color), fill=color)
    fig.plot(data=dir+law1, style='f5c/0.6c+l+s45+o0.35c', pen="{}p,{}".format(c, color))
    fig.plot(data=dir+pan, pen="{}p,{}".format(d, color))
    fig.plot(data=dir+pan3, pen="{}p,{}".format(a1, color))
    fig.plot(data=dir+tam, pen="{}p,{}".format(c, color))
    fig.plot(data=dir+'faultsulawesi1.gmt', pen="{}p,{}".format(c, color))

    fig.plot(data=dir+'trench.gmt', style='f2/0.15i+l+t', pen="{}p,{}".format(a, color), fill=color)
    fig.plot(data=dir+'indonesiafaults.gmt', pen="{}p,{}".format(d, color))

struktur(0.5, 'dimgray')

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