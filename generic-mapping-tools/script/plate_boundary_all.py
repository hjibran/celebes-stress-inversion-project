#!/home/haidir/celebes-stress-inversion-project/venv/bin/python3

import pygmt
import pandas as pd
import geopandas as gpd
import numpy as np

# -------------------------------------------------------------------------------- #

# import data
data = pd.read_csv("/mnt/d/celebes-stress-inversion-project/data/siap-olah/fm50km7mw.csv")
FM = data.iloc[:, [3, 2, 4, 6, 7, 8, 5]]
FM.columns = ["longitude", "latitude", "depth", "strike", "dip", "rake", "magnitude"]
buffer03515 = gpd.read_file("/mnt/d/celebes-stress-inversion-project/Result/eps0.35min15-final/eps0.35pts15.shp")
buffer04015 = gpd.read_file("/mnt/d/celebes-stress-inversion-project/Result/eps0.40min15-final/eps0.40pts15.shp")
buffer05015 = gpd.read_file("/mnt/d/celebes-stress-inversion-project/Result/eps0.50min15-final/eps0.50pts15.shp")
plate_boundary = gpd.read_file("/mnt/d/celebes-stress-inversion-project/data/batas-lempeng-dan-patahan/bird2003/PB2002_steps.shp")

# -------------------------------------------------------------------------------- #

# defenisikan fig
fig = pygmt.Figure()

# -------------------------------------------------------------------------------- #

# download and store earth relief
grid = pygmt.datasets.load_earth_relief(resolution="30s", # resolution of earth relief
                                        region=[117.5, 127.5, -8.5, 5.5], # boarder of map: [minlon, maxlon, minlat, maxlat]
                                        registration="gridline")

# plot grid image
fig.grdimage(grid=grid, # call grid
             frame=["a", "EWSN"],#, "+tPulau Sulawesi"],
             projection="M20c",
             cmap= 'gray')#"/mnt/d/celebes-stress-inversion-project/generic-mapping-tools/script/color.cpt")
fig.coast(shorelines="1p,black"
    #water="white"
)

# -------------------------------------------------------------------------------- #

# Plot batas lempeng dan patahan
#fig.basemap(region=[117.5, 127.5, -8.5, 5.5], frame=["WNES", "a"], projection="M20c")
#fig.coast(shorelines="lightgrey", land="lightgrey")
#fig.plot(
#    data="/mnt/d/celebes-stress-inversion-project/data/batas-lempeng-dan-patahan/indonesiafaults.gmt", 
#    pen="1p,gray"
#)

#fig.plot(
#    data="/mnt/d/celebes-stress-inversion-project/data/batas-lempeng-dan-patahan/trench.gmt", 
#    pen="1.5p,gray", 
#    style="f1c/0.2c+l+t", 
#    fill="gray"
#)

#fig.plot(
#    data=plate_boundary,
#    pen='1p,black,-',
#    #label='Boundary Plat'
#)

# -------------------------------------------------------------------------------- #

# plot epicenter events
#fig.plot(x=FM.longitude, y=FM.latitude, style="c0.1c", fill='gray')

# -------------------------------------------------------------------------------- #

# plot batas cluster
#cluster_boundary = gpd.read_file("/mnt/d/celebes-stress-inversion-project/Result/eps0.40min15-final/eps0.40pts15.shp")
#fig.plot(data=cluster_boundary, pen="1p,blue,-", label="ε=0.40 MinPts=15")

#fig.plot(data=buffer03515, pen="1p,green", label="ε=0.35 MinPts=15")
#fig.plot(data=buffer04015, pen="1p,blue", label="ε=0.40 MinPts=15")
#fig.plot(data=buffer05015, pen="1p,red", label="ε=0.50 MinPts=15")

# -------------------------------------------------------------------------------- #
 
# plot plate motion velocity
#df1 = pd.read_csv("/mnt/d/socquet_2006_plate_motion copy.csv")#("/mnt/d/celebes-stress-inversion-project/data/batas-lempeng-dan-patahan/motion_plate_v2.csv")
#fig.velo(
#    data=df1,
#    spec="e0.075/0.075z+f12",
#    uncertaintyfill="navy",
#    pen="4p,navy",
#    line=True,
#    vector="0.75c+p.2p+e+gnavy"
#)

#df2 = pd.read_csv("/mnt/d/simons2007data.csv")#("/mnt/d/celebes-stress-inversion-project/data/batas-lempeng-dan-patahan/motion_plate_v2.csv")
#fig.velo(
#    data=df2,
#    spec="e0.075/0.075+f12",
#    uncertaintyfill="darkred",
#    pen="4p,darkred",
#    line=True,
#    vector="0.75c+p.2p+e+gdarkred"
#)

#dfa = pd.read_csv("/mnt/d/socquet2006makassardatasundarelative.csv")#("/mnt/d/celebes-stress-inversion-project/data/batas-lempeng-dan-patahan/motion_plate_v2.csv")
#fig.velo(
#    data=dfa,
#    spec="e0.0015/0.0015+f12",
#    uncertaintyfill="darkblue",
#    pen="3p,darkblue",
#    line=True,
#    vector="0.75c+p.2p+e+gdarkblue"
#)

#dfb = pd.read_csv("/mnt/d/socquet_2006_plate_motion copy.csv")#("/mnt/d/celebes-stress-inversion-project/data/batas-lempeng-dan-patahan/motion_plate_v2.csv")
#fig.velo(
#    data=dfb,
#    spec="e0.075/0.075+f12",
#    uncertaintyfill="darkblue",
#    pen="3p,darkblue",
#    line=True,
#    vector="0.75c+p.2p+e+gdarkblue"
#)

dfc = pd.read_csv("/mnt/d/socquet2006makassardatasundarelative.csv")#("/mnt/d/celebes-stress-inversion-project/data/batas-lempeng-dan-patahan/motion_plate_v2.csv")
fig.velo(
    data=dfc,
    spec="e0.0075/0.0075+f12",
    uncertaintyfill="darkblue",
    pen="3p,darkblue",
    line=True,
    vector="0.75c+p.2p+e+gdarkblue"
)

# -------------------------------------------------------------------------------- #

# lokasi kota-kota besar
#fill = "black" #"darkred"
#fig.plot(x=119.4, y=-5.16, style="s0.25c", fill=fill, pen="1p,gray")
#fig.plot(x=119.8, y=-0.90, style="s0.25c", fill=fill, pen="1p,gray")
#fig.plot(x=118.9, y=-2.68, style="s0.25c", fill=fill, pen="1p,gray")
#fig.plot(x=122.6, y=-3.97, style="s0.25c", fill=fill, pen="1p,gray")
#fig.plot(x=123.1, y=0.54, style="s0.25c", fill=fill, pen="1p,gray")
#fig.plot(x=124.8, y=1.49, style="s0.25c", fill=fill, pen="1p,gray")
#
#font = "13p,Helvetica-Bold,gray"
#fig.text(x=118.8, y=-4.7, text="Makassar", font=font)
#fig.plot(x=[118.8, 119.4], y=[-4.85, -5.16], pen="1.5p,gray")
#fig.text(x=118.70, y=-0.65, text="Palu", font=font)
#fig.plot(x=[118.95, 119.8], y=[-0.65, -0.90], pen="1.5p,gray")
#fig.text(x=118.0, y=-2.40, text="Mamuju", font=font)
#fig.plot(x=[118.45, 118.9], y=[-2.45, -2.68], pen="1.5p,gray")
#fig.text(x=122.0, y=-4.31, text="Kendari", font=font)
#fig.plot(x=[122.0, 122.6], y=[-4.21, -3.97], pen="1.5p,gray")
#fig.text(x=122.1, y=0.38, text="Gorontalo", font=font)
#fig.plot(x=[122.65, 123.1], y=[0.38, 0.54], pen="1.5p,gray")
#fig.text(x=124.7, y=2, text="Manado", font=font)
#fig.plot(x=[124.7, 124.8], y=[1.88, 1.49], pen="1.5p,gray")

# -------------------------------------------------------------------------------- #


fig.basemap(
    rose="jBL+w1.8c+lW,E,S,N+o0.5c/0.5c+f2",
    #map_scale="jBL+w200k+o0.45c/0.5c+f+lkm"
) 
#fig.plot(x=118.8, y=4.85, style="r4.1c/1.5c", pen="1p,gray", fill="white")
#fig.legend(position="jTL+o0.5/0.5c", box=False)

#fig.savefig("/mnt/d/celebes-stress-inversion-project/generic-mapping-tools/maps/class-boundaries.png")
fig.show()