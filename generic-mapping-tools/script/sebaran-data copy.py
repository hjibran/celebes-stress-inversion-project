#!/home/haidir/celebes-stress-inversion-project/venv/bin/python3

import pygmt
import pandas as pd
import os
import  re

fig = pygmt.Figure()
fig.basemap(region=[117.5, 127.5, -8.5, 5.5],
            frame=["a", "+tSebaran Mekanisme Fokus Pulau Sulawesi"],
            projection="M20c"
)
fig.coast(shorelines='1p'
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

color = ['lightgrey','moccasin','navy','steelblue','paleturquoise','lightgreen','limegreen','darkyellow','sandybrown','darkorange','palevioletred','darkviolet','lightgrey','seashell4','peachpuff4','cornsilk4','lavenderblush4','slateblue4','dodgerblue4','skyblue4','lightsteelblue4','paleturquoise4','cyan4','darkseagreen4','springgreen4','olivedrab4','lightgoldenrod4','gold4','rosybrown4','burlywood4','chocolate4','salmon4','darkorange4','orangered4','hotpink4','palevioletred4','magenta4','mediumorchid4','mediumpurple4','lightgrey']
file = []
c = 0
for filename in os.listdir("/mnt/d/celebes-stress-inversion-project/data/hasil-dbscan/eps0.3min7"):
    x = re.search("(cls[-]*[0-9]+)", filename)
    fm = pd.read_csv("/mnt/d/celebes-stress-inversion-project/data/hasil-dbscan/eps0.3min7/{}.csv".format(x[1]))
    FM = fm.iloc[:, [3, 2, 4, 6, 7, 8, 5]]
    FM.columns = ["longitude", "latitude", "depth", "strike", "dip", "rake", "magnitude"]
    fig.meca(
        spec=FM,
        compressionfill=color[c],
        scale="0.2c",
        extensionfill="cornsilk",
    )
    c += 1

fig.savefig("/mnt/d/celebes-stress-inversion-project/data/hasil-dbscan/eps0.3min7/sebaran.jpg")


#fig.show()