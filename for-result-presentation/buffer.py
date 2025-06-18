#!/home/haidir/celebes-stress-inversion-project/venv/bin/python3

import pygmt
import pandas as pd
import geopandas as gpd

data = pd.read_csv("/mnt/d/celebes-stress-inversion-project/data/siap-olah/fm50km7mw.csv")
FM = data.iloc[:, [3, 2, 4, 6, 7, 8, 5]]
FM.columns = ["longitude", "latitude", "depth", "strike", "dip", "rake", "magnitude"]
buffer03515 = gpd.read_file("/mnt/d/celebes-stress-inversion-project/Result/eps0.35min15-final/eps0.35pts15.shp")
buffer04015 = gpd.read_file("/mnt/d/celebes-stress-inversion-project/Result/eps0.40min15-final/eps0.40pts15.shp")
buffer05015 = gpd.read_file("/mnt/d/celebes-stress-inversion-project/Result/eps0.50min15-final/eps0.50pts15.shp")

# download and store earth relief
grid = pygmt.datasets.load_earth_relief(resolution="30s", # resolution of earth relief
                                        region=[117.4, 129.6, -9.3, 6.7], #[117.5, 128, -9, 6] boarder of map: [minlon, maxlon, minlat, maxlat]
                                        registration="gridline")
fig = pygmt.Figure()

# plot grid image
fig.grdimage(grid=grid, # call grid
             frame=["a", "EWSN"],#, "+tPulau Sulawesi"],
             projection="M75c",
             cmap= "/mnt/d/celebes-stress-inversion-project/generic-mapping-tools/script/color.cpt")

#fig.basemap(region=[117.5, 127.5, -8.5, 5.5], frame=["WNES", "a"], projection="M20c")
fig.coast(water="white")
fig.plot(
    data="/mnt/d/celebes-stress-inversion-project/data/batas-lempeng-dan-patahan/indonesiafaults.gmt", 
    pen="3.75p,black",
    label='Fault'
)
fig.plot(
    data="/mnt/d/celebes-stress-inversion-project/data/batas-lempeng-dan-patahan/trench.gmt", 
    pen="4.5p,black", 
    style="f3.75c/0.75c+l+t", 
    fill="black",
    label='Subduction'
)

utara=[117.5, 126, -3.55, 3.5]
selatan=[118.5, 123, -4.5, -1.7]
maluku=[123.3, 129.5, -2.05, 5.3]
sula=[125.5, 128, -3.5, -2.25]
sangihe=[124.4, 126.9, 4, 6.6]
ntt=[124.2, 126.8, -9.2, -7.2]

def inset(R):
    x = [R[0], R[1], R[1], R[0], R[0]]
    y = [R[2], R[2], R[3], R[3], R[2]]
    return x, y

for i in [utara, selatan, maluku, sula, sangihe, ntt]:
    x, y = inset(i)
    fig.plot(x=x,
             y=y,
             pen='4p,black'
    )

fig.plot(x=FM.longitude, y=FM.latitude, style="c0.375c", fill='darkgray', pen='black', label='Epicenter')

fig.plot(data=buffer03515, pen="7.5p,springgreen3", label="ε=0.35 MinPts=15")
fig.plot(data=buffer04015, pen="7.5p,gold2", label="ε=0.40 MinPts=15")
fig.plot(data=buffer05015, pen="7.5p,tomato", label="ε=0.50 MinPts=15")

fill = "red"
fig.plot(x=119.4, y=-5.16, style="s0.9375c", fill=fill, pen="3.75p,black", label="Provincial capital")
fig.plot(x=119.8, y=-0.90, style="s0.9375c", fill=fill, pen="3.75p,black")
fig.plot(x=118.9, y=-2.68, style="s0.9375c", fill=fill, pen="3.75p,black")
fig.plot(x=122.6, y=-3.97, style="s0.9375c", fill=fill, pen="3.75p,black")
fig.plot(x=123.1, y=0.54, style="s0.9375c", fill=fill, pen="3.75p,black")
fig.plot(x=124.8, y=1.49, style="s0.9375c", fill=fill, pen="3.75p,black")

font = "48.75p,Helvetica-Bold,black"
fig.text(x=118.8, y=-4.7, text="Makassar", font=font)
fig.plot(x=[118.8, 119.4], y=[-4.85, -5.16], pen="5.625p,black")
fig.text(x=118.70, y=-0.65, text="Palu", font=font)
fig.plot(x=[118.95, 119.8], y=[-0.65, -0.90], pen="5.625p,black")
fig.text(x=118.0, y=-2.40, text="Mamuju", font=font)
fig.plot(x=[118.45, 118.9], y=[-2.45, -2.68], pen="5.625p,black")
fig.text(x=122.0, y=-4.31, text="Kendari", font=font)
fig.plot(x=[122.0, 122.6], y=[-4.21, -3.97], pen="5.625p,black")
fig.text(x=122.1, y=0.38, text="Gorontalo", font=font)
fig.plot(x=[122.65, 123.1], y=[0.38, 0.54], pen="5.625p,black")
fig.text(x=124.7, y=2, text="Manado", font=font)
fig.plot(x=[124.7, 124.8], y=[1.88, 1.49], pen="5.625p,black")

fig.basemap(
    rose="jBL+w6.75c+lW,E,S,N+o5c/10+f2",
    #map_scale="JBL+w200k+o0.45c/0.5c+f+lkm"
) 
#fig.plot(x=118.85, y=5.34, style="r4.1c/5", pen="1p,black", fill="white")
#fig.legend(position="JTL+o10/15c+w30c", box='+gwhite+p4p')
#with pygmt.config(FONT_ANNOT_PRIMARY="45p"):
#    fig.legend(position="JTR+jTR+o0.2c", box="+gwhite+pblack")

fig.savefig("/mnt/d/class-boundaries.png")
fig.show()