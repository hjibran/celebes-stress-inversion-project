#!/home/haidir/celebes-stress-inversion-project/venv/bin/python3
"""
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
"""

import geopandas as gpd
import pygmt

# Read shapefile data using geopandas
gdf = gpd.read_file(
    "http://www2.census.gov/geo/tiger/TIGER2015/PRISECROADS/tl_2015_15_prisecroads.zip"
)
# The dataset contains different road types listed in the RTTYP column,
# here we select the following ones to plot:
roads_common = gdf[gdf.RTTYP == "M"]  # Common name roads
roads_state = gdf[gdf.RTTYP == "S"]  # State recognized roads
roads_interstate = gdf[gdf.RTTYP == "I"]  # Interstate roads

fig = pygmt.Figure()

# Define target region around Oʻahu (Hawaiʻi)
region = [-158.3, -157.6, 21.2, 21.75]  # xmin, xmax, ymin, ymax

title = "Main roads of O`ahu (Hawai`i)"  # Approximating the Okina letter ʻ with `
fig.basemap(region=region, projection="M12c", frame=["af", f"WSne+t{title}"])
fig.coast(land="gray", water="dodgerblue4", shorelines="1p,black")

# Plot the individual road types with different pen settings and assign labels
# which are displayed in the legend
fig.plot(data=roads_common, pen="5p,dodgerblue", label="CommonName")
fig.plot(data=roads_state, pen="2p,gold", label="StateRecognized")
fig.plot(data=roads_interstate, pen="2p,red", label="Interstate")

# Add legend
fig.legend()

fig.show()