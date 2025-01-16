#!/home/haidir/celebes-stress-inversion-project/venv/bin/python3

import pygmt
import pandas as pd
import geopandas as gpd

data = pd.read_csv("/mnt/d/celebes-stress-inversion-project/data/siap-olah/fm50km7mw.csv")
FM = data.iloc[:, [3, 2, 4, 6, 7, 8, 5]]
FM.columns = ["longitude", "latitude", "depth", "strike", "dip", "rake", "magnitude"]
buffer03515 = gpd.read_file("/mnt/d/celebes-stress-inversion-project/Result/eps0.35min15-final/eps0.35pts15-bagian-utara.shp")
buffer04015 = gpd.read_file("/mnt/d/celebes-stress-inversion-project/Result/eps0.40min15-final/eps0.40pts15-bagian-utara.shp")
buffer05015 = gpd.read_file("/mnt/d/celebes-stress-inversion-project/Result/eps0.50min15-final/eps0.50pts15-bagian-utara.shp")

# download and store earth relief
grid = pygmt.datasets.load_earth_relief(resolution="30s", # resolution of earth relief
                                        region=[117.5, 126, -3.5, 3.5],  #[118.5, 125, -2.5, 2.5], # boarder of map: [minlon, maxlon, minlat, maxlat]
                                        registration="gridline")
fig = pygmt.Figure()

# plot grid image
fig.grdimage(grid=grid, # call grid
             frame=["a2", "EWSN"],#, "+tPulau Sulawesi"],
             projection="M10c",
             cmap= "oleron")#"/mnt/d/celebes-stress-inversion-project/generic-mapping-tools/script/color.cpt")

#fig.basemap(region=[117.5, 127.5, -8.5, 5.5], frame=["WNES", "a"], projection="M20c")
#fig.coast(water="white")
fig.plot(
    data="/mnt/d/celebes-stress-inversion-project/data/batas-lempeng-dan-patahan/indonesiafaults.gmt", 
    pen="0.6p,black",
    label="Patahan"
)
fig.plot(
    data="/mnt/d/celebes-stress-inversion-project/data/batas-lempeng-dan-patahan/trench.gmt", 
    pen="0.8p,black", 
    style="f1c/0.2c+l+t", 
    fill="black",
    label="Subduksi"
)
fig.plot(x=FM.longitude, y=FM.latitude, style="c0.1c", pen="1p,black", fill='gray', label="Episenter")

fig.plot(data=buffer03515, pen="2p,purple", label="ε=0.35 MinPts=15")
fig.plot(data=buffer04015, pen="2p,yellow", label="ε=0.40 MinPts=15")
fig.plot(data=buffer05015, pen="2p,red", label="ε=0.50 MinPts=15")
"""
fill = "red"
fig.plot(x=119.4, y=-5.16, style="s0.25c", fill=fill, pen="1p,black", label="Ibukota Provinsi")
fig.plot(x=119.8, y=-0.90, style="s0.25c", fill=fill, pen="1p,black")
fig.plot(x=118.9, y=-2.68, style="s0.25c", fill=fill, pen="1p,black")
fig.plot(x=122.6, y=-3.97, style="s0.25c", fill=fill, pen="1p,black")
fig.plot(x=123.1, y=0.54, style="s0.25c", fill=fill, pen="1p,black")
fig.plot(x=124.8, y=1.49, style="s0.25c", fill=fill, pen="1p,black")

font = "10p,Helvetica-Bold,black"
fig.text(x=118.8, y=-4.7, text="Makassar", font=font)
fig.plot(x=[118.8, 119.4], y=[-4.85, -5.16], pen="1.5p,black")
fig.text(x=118.80, y=-0.53, text="Palu", font=font)
fig.plot(x=[118.95, 119.8], y=[-0.65, -0.90], pen="1.5p,black")
fig.text(x=118.0, y=-2.40, text="Mamuju", font=font)
fig.plot(x=[118.45, 118.9], y=[-2.45, -2.68], pen="1.5p,black")
fig.text(x=122.0, y=-4.31, text="Kendari", font=font)
fig.plot(x=[122.0, 122.6], y=[-4.21, -3.97], pen="1.5p,black")
fig.text(x=121.9, y=0.12, text="Gorontalo", font=font)
fig.plot(x=[122.45, 123.1], y=[0.21, 0.54], pen="1.5p,black")
fig.text(x=124.45, y=2.10, text="Manado", font=font)
fig.plot(x=[124.7, 124.8], y=[1.88, 1.49], pen="1.5p,black")
"""
fig.basemap(
    rose="jBR+w1.3c+lW,E,S,N+o0.2c/0.2c+f2",
    #map_scale="jBL+w200k+o0.45c/0.5c+f+lkm"
) 
#fig.plot(x=118.8, y=4.85, style="r4.1c/1.5c", pen="1p,black", fill="white")
#fig.legend(position="JTL+o0.5/0.5c", box=False)

#fig.savefig("/mnt/d/celebes-stress-inversion-project/generic-mapping-tools/maps/class-boundaries.png")
fig.show()