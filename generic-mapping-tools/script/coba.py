#!/home/haidir/celebes-stress-inversion-project/venv/bin/python3

import pygmt
import pandas as pd
import geopandas as gpd

FM = pd.read_csv("/mnt/d/Data/data-bang-ronal/belakang_cave_b.csv")
cave = gpd.read_file("/mnt/d/Data/data-bang-ronal/cave_gbc_crs.shp")

print(cave)
fig = pygmt.Figure()
fig.basemap(region=[FM.longitude.min()-0.0008, FM.longitude.max()+0.0008, FM.latitude.min()-0.0008, FM.latitude.max()+0.0008], frame=["WNES", "a"], projection="M20c")
fig.coast(shorelines="lightgrey", land="lightgrey")

fig.meca(
    spec=FM,
    compressionfill="black",
    scale="0.6c",
    extensionfill="white"
)


fig.plot(data=cave, pen="3p,red", label="ε=0.50 MinPts=15")

#fig.savefig("hasil2.png")
fig.show()