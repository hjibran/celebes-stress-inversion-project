import os
import numpy as np
import pandas as pd
import pygmt
import statistics as sts
epsilon = "0.50"

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

fig = pygmt.Figure()

grid = pygmt.datasets.load_earth_relief(resolution="30s", # resolution of earth relief
                                        region=[117.5, 127.5, -8.5, 5.5], # boarder of map: [minlon, maxlon, minlat, maxlat]
                                        registration="gridline")

fig.grdimage(grid=grid, # call grid
             frame=["a2", "EWSN"],
             projection="M10c",
             cmap= "/mnt/d/celebes-stress-inversion-project/generic-mapping-tools/script/color.cpt")

fig.coast(#region=[117.5, 127.5, -8.5, 5.5],
          #projection='M10c',
          #frame=["a", "EWSN"],
          #land='lightgray',
          water="white",
          #resolution='f',
          #shorelines='0.25p,black,solid'
          )

os.system('gmt makecpt -Cdarkblue,blue,green,red,darkred -T0/3/0.02 -Z > /mnt/d/celebes-stress-inversion-project/generic-mapping-tools/custom.cpt')
sebaran = np.array([0,3])
pygmt.makecpt(cmap="/mnt/d/celebes-stress-inversion-project/generic-mapping-tools/custom.cpt", 
              series=[sebaran.min(), sebaran.max()])

for i in range(10):
    data_cluster = pd.read_csv("/mnt/d/celebes-stress-inversion-project/Result/eps{}min15-final/clustered/cls{}.csv".format(epsilon, i))
    data_origin = pd.read_csv("/mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Output/eps{}pts15/cls{}/output_origin.csv".format(epsilon, i))
    data_bootstrap = pd.read_csv("/mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Output/eps{}pts15/cls{}/output_bootstarap.csv".format(epsilon, i))
    data_error = pd.read_csv("/mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Output/eps{}pts15/cls{}/output_error.csv".format(epsilon, i))

    lon = data_cluster["lon"];mean_longitude = np.mean(lon)
    lat = data_cluster["lat"];mean_latitude = np.mean(lat)

    min_shmax = data_error["2.5%"][6]; max_shmax = data_error["97.5%"][6]

    #simpson_index = data_origin["simpson index"][0]
    simpson_index = sts.mode(data_bootstrap['simpson index'])

    shmax_plot(mean_longitude, mean_latitude, min_shmax, max_shmax, simpson_index)

#fig.colorbar(frame=["x"],#"af+l'Depth (km)'", 
#             position="JMR+w10/0.5+o3/0c+mn+")#+w-3/0.25+o0.3/0.3c+mn+")


fig.show()