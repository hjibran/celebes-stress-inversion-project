#!/home/haidir/celebes-stress-inversion-project/venv/bin/python3
import pandas as pd
from sklearn.cluster import DBSCAN
import numpy as np
import os
import sys
import re
import pygmt
eps = 0.5
min = 15

data = pd.read_csv("/mnt/d/celebes-stress-inversion-project/data/siap-olah/fm50km7mw.csv") #data-tanpa-laut-maluku.csv")

x = data.iloc[:, [3, 2]]
clustering = DBSCAN(eps=eps, min_samples=min).fit(x)
data["cluster"] = clustering.labels_

fig = pygmt.Figure()
fig.basemap(region=[117.5, 127.5, -8.5, 5.5],
            frame=["a", "+teps{}min{}".format(eps, min)],
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
FM = data.iloc[:, [3, 2, 4, 6, 7, 8, 5]]
FM.columns = ["longitude", "latitude", "depth", "strike", "dip", "rake", "magnitude"]
pygmt.makecpt(cmap="seis", series=[FM.depth.min(), FM.depth.max()], output= "pallet.cpt")
fig.meca(
        spec=FM,
        compressionfill="black",
        cmap="pallet.cpt",
        scale="0.2c",
        extensionfill="white"
    )
fig.colorbar(frame=True)
fig.show()