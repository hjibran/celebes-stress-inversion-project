#!/home/haidir/celebes-stress-inversion-project/venv/bin/python3

import pygmt

grid = pygmt.datasets.load_earth_relief(
    resolution="30s", region=[117.5, 127.5, -8.5, 5.5], registration="gridline"
)

fig = pygmt.Figure()
fig.grdimage(grid=grid, 
             frame=["a", "+tPulau Sulawesi"], 
             projection="M20c", 
             cmap="vik"#"earth"#"oleron"#"geo"
)
fig.colorbar(frame=["a3000f1000", "x+lElevation", "y+lm"]
)
#fig.coast(land='gray',
#          water='blue'
#)
"""
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
"""
#fig.savefig("/mnt/d/celebes-stress-inversion-project/generic-mapping-tools/maps/basemap.pdf")
fig.show()