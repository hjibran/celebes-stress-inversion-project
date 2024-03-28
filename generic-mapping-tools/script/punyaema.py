#!/home/haidir/celebes-stress-inversion-project/venv/bin/python3

import pygmt
import pandas as pd

grid = pygmt.datasets.load_earth_relief(
    resolution="30s", region=[118, 126, -11, -4.5], registration="gridline"
)

fig = pygmt.Figure()

fig.basemap(frame=["a"],
            projection="M20c"
)

fig.grdimage(grid=grid, 
             cmap="oleron"
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

fig.plot(
    x=122.23,
    y=-7.67,
    style="a0.8c",
    fill="red"
)
fig.text(x=122.23,
         y=-7.87,
         text="Mw 7.3 mainshock (14 Dec 2021)",
         font='red'
         )

#with fig.inset(position="jBR+o0.1c", box="+gwhite+p1p", region= [114, 130, -12, 5], projection="U51M/3c"):
#    fig.coast( dcw="ID+glightgreen+p0.2p", area_thresh=10000)
#    rectangle = [118, 126, -11, -4.5]
    #fig.plot(data=rectangle, style="r+s", pen="2p,blue")

fig.savefig("punyaema.png")              

fig.show()