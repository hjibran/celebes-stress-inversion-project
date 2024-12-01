#!/home/haidir/celebes-stress-inversion-project/venv/bin/python3

import pygmt
import pandas as pd
import geopandas as gpd

FM = pd.read_csv("/mnt/d/celebes-stress-inversion-project/data/siap-olah/aki.csv")
buffer05015 = gpd.read_file("/mnt/d/celebes-stress-inversion-project/Result/shp-buffer/buffer04015.shp")

fig = pygmt.Figure()
fig.basemap(region=[117.5, 127.5, -8.5, 5.5], frame=["WNES", "a"], projection="M20c")
fig.coast(shorelines="lightgrey", land="lightgrey")
fig.plot(
    data="/mnt/d/celebes-stress-inversion-project/data/batas-lempeng-dan-patahan/indonesiafaults.gmt", 
    pen="1p,lightgrey"
)
fig.plot(
    data="/mnt/d/celebes-stress-inversion-project/data/batas-lempeng-dan-patahan/trench.gmt", 
    pen="1.2p,lightgrey", 
    style="f1c/0.2c+l+t", 
    fill="lightgrey"
)
fig.plot(x=FM.longitude, y=FM.latitude, style="c0.1c", fill='grey')

fig.plot(data=buffer05015, pen="1p,blue", label="ε=0.50 MinPts=15")

urut=[9, 0, 3, 6, 7, 8, 5, 2, 4, 1]
i=0
while i < len(urut):
    data = pd.read_csv("/mnt/d/celebes-stress-inversion-project/Result/eps0.4min15/clustered/cls{}.csv".format(urut[i]))
    fig.text(
            x=sum(data.lon)/len(data.lon),
            y=sum(data.lat)/len(data.lat),
            text=str(i+1),
            font="20p,black"
    )
    i+=1

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
    rose="jBL+w1.8c+lW,E,S,N+o4.5c/0.5c+f2",
    map_scale="jBL+w200k+o0.45c/0.5c+f+lkm"
) 
fig.legend(position="jBL+o0.2/1.6c", box=True)

#fig.savefig("pictures/cluster0.4015.png")
print(buffer05015)
fig.show()
