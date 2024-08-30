# ----------------------------------------------------------------#
#                                                                 #
# this code was created plot final shmax                          #
#                                                                 #
# ----------------------------------------------------------------#
import pygmt
import pandas as pd
import numpy as np
import geopandas as gpd

fig = pygmt.Figure()
fig.basemap(region=[117.5, 127.5, -8.5, 5.5], frame=["WNES", "a"], projection="M20c")
fig.coast(shorelines="lightgrey", land="lightgrey")
fig.plot(data="/mnt/d/celebes-stress-inversion-project/data/batas-lempeng-dan-patahan/indonesiafaults.gmt", 
         pen="1p,lightgrey")
fig.plot(data="/mnt/d/celebes-stress-inversion-project/data/batas-lempeng-dan-patahan/trench.gmt",
         pen="1.2p,lightgrey",
         style="f1c/0.2c+l+t",
         fill="lightgrey")
plate_boundary = gpd.read_file("/mnt/d/celebes-stress-inversion-project/data/batas-lempeng-dan-patahan/bird2003/PB2002_steps.shp")
fig.plot(data=plate_boundary, pen="1p,grey", label="Plate Boundary")

"""
df = pd.DataFrame(
    data={
        "x": [120,120],
        "y": [3,1],
        "east_velocity": [31.39/2],
        "north_velocity": [-12.88/2],
        "east_sigma": [0],
        "north_sigma": [0],
        "correlation_EN": [0],
        "SITE": ["SU(MS)"],
    }
)
fig.velo(
    data=df,
    spec="e0.2/0.39+f18",
    uncertaintyfill="lightblue1",
    pen="1p,red",
    line=True,
    vector="1c+p1p+e+gred",
)"""

cluster_boundary = gpd.read_file("/mnt/d/celebes-stress-inversion-project/Result/eps0.50min15-final/eps0.50pts15.shp")
fig.plot(data=cluster_boundary, pen="1p,black,-", label="ε=0.50 MinPts=15")

def shmax_plot(lon, lat, down, up):
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

    data = [[lon, lat, 1.5, 360-up+90, 360-down+90], [lon, lat, 1.5, 360-up1+90, 360-down1+90]]
    fig.plot(data=data, style="w", fill="red")#, pen="1p, red")

for i in range(10):
    data_cluster = pd.read_csv("/mnt/d/celebes-stress-inversion-project/Result/eps0.50min15-final/clustered/cls{}.csv".format(i))
    lon = data_cluster["lon"];mean_longitude = np.mean(lon)
    lat = data_cluster["lat"];mean_latitude = np.mean(lat)
    data_shmax = pd.read_csv("/mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Output/eps0.50pts15/cls{}/output_error.csv".format(i))
    min_shmax = data_shmax["2.5%"][6]; max_shmax = data_shmax["97.5%"][6]

    shmax_plot(mean_longitude, mean_latitude, min_shmax, max_shmax)

fig.savefig("/mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Output/shmax.png")
#fig.show()