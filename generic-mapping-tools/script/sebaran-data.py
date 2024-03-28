#!/home/haidir/celebes-stress-inversion-project/venv/bin/python3

import pygmt
import pandas as pd

data = pd.read_csv("/mnt/d/celebes-stress-inversion-project/data/siap-olah/fm50km7mw.csv")
FM = data.iloc[:, [3, 2, 4, 6, 7, 8, 5]]
FM.columns = ["longitude", "latitude", "depth", "strike", "dip", "rake", "magnitude"]

grid = pygmt.datasets.load_earth_relief(
    resolution="30s", region=[117.5, 127.5, -8.5, 5.5], registration="gridline"
)

fig = pygmt.Figure()

fig.basemap(frame=["a"],#, "+tSebaran Mekanisme Fokus Pulau Sulawesi"],
            projection="M20c"
)

#fig.grdimage(grid=grid, 
#             cmap="oleron"
#)
#fig.colorbar(frame=["a3000f1000", "x+lElevation", "y+lm"]
#)
fig.coast(land='gray',
#          water='blue'
)
fig.plot(
    data="/mnt/d/celebes-stress-inversion-project/data/batas-lempeng-dan-patahan/indonesiafaults.gmt", 
    pen="0.85p"
)
fig.plot(
    data="/mnt/d/celebes-stress-inversion-project/data/batas-lempeng-dan-patahan/trench.gmt", 
    pen="1p", 
    style="f1c/0.2c+l+t", 
    fill="black"
)

fig.meca(
    spec=FM,
    compressionfill="red",
    cmap="palet-warna.cpt",
    scale="0.3c",
    extensionfill="white",
)

fig.colorbar(position="jBL+o0.2/1.6c", box=True)

fill = "red"
fig.plot(x=119.4, y=-5.16, style="s0.25c", fill=fill, pen="1p,black")
fig.plot(x=119.8, y=-0.90, style="s0.25c", fill=fill, pen="1p,black")
fig.plot(x=118.9, y=-2.68, style="s0.25c", fill=fill, pen="1p,black")
fig.plot(x=122.6, y=-3.97, style="s0.25c", fill=fill, pen="1p,black")
fig.plot(x=123.1, y=0.54, style="s0.25c", fill=fill, pen="1p,black")
fig.plot(x=124.8, y=1.49, style="s0.25c", fill=fill, pen="1p,black")

font = "13p,Helvetica-Bold,black"
fig.text(x=118.8, y=-4.7, text="Makassar", font=font)
fig.plot(x=[118.8, 119.4], y=[-4.85, -5.16], pen="1.5p,black")
fig.text(x=118.70, y=-0.65, text="Palu", font=font)
fig.plot(x=[118.95, 119.8], y=[-0.65, -0.90], pen="1.5p,black")
fig.text(x=118.0, y=-2.40, text="Mamuju", font=font)
fig.plot(x=[118.45, 118.9], y=[-2.45, -2.68], pen="1.5p,black")
fig.text(x=122.0, y=-4.31, text="Kendari", font=font)
fig.plot(x=[122.0, 122.6], y=[-4.21, -3.97], pen="1.5p,black")
fig.text(x=122.1, y=0.38, text="Gorontalo", font=font)
fig.plot(x=[122.65, 123.1], y=[0.38, 0.54], pen="1.5p,black")
fig.text(x=124.7, y=2, text="Manado", font=font)
fig.plot(x=[124.7, 124.8], y=[1.88, 1.49], pen="1.5p,black")

fig.basemap(
    rose="jTL+w1.8c+lW,E,S,N+o0.25c/0.25c+f2",
    map_scale="jBR+w200k+o0.5c/0.5c+f+lkm"
) 

#fig.savefig("/mnt/d/celebes-stress-inversion-project/generic-mapping-tools/maps/sebaran-data-a.pdf")
fig.savefig("/mnt/d/celebes-stress-inversion-project/generic-mapping-tools/maps/sebaran-data-c.png")
#fig.show()