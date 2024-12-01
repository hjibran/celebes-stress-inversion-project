#!/home/haidir/celebes-stress-inversion-project/venv/bin/python3


# import module
import pygmt
import geopandas as gpd

# download and store earth relief
grid = pygmt.datasets.load_earth_relief(resolution="30s", # resolution of earth relief
                                        region=[117.5, 127.5, -8.5, 5.5], # boarder of map: [minlon, maxlon, minlat, maxlat]
                                        registration="gridline")
# begin fig object
fig = pygmt.Figure()

# plot grid image
fig.grdimage(grid=grid, # call grid
             frame=["a", "+tPulau Sulawesi"],
             projection="M20c",
             cmap=  "/mnt/d/celebes-stress-inversion-project/generic-mapping-tools/script/color.cpt")
# display color bar from grid image
fig.colorbar(frame=["a3000f1000", "x+lElevation", "y+lm"])

# plot fault
fig.plot(data="/mnt/d/celebes-stress-inversion-project/data/batas-lempeng-dan-patahan/indonesiafaults.gmt",
         pen="0.5p,black")

# plot trench
fig.plot(data="/mnt/d/celebes-stress-inversion-project/data/batas-lempeng-dan-patahan/trench.gmt",
         pen="1p",
         style="f1c/0.2c+l+t",
         fill="black")

# show picture
fig.show()



#fig.savefig("/mnt/d/celebes-stress-inversion-project/generic-mapping-tools/maps/basemap.pdf")
#plate_boundary = gpd.read_file("/mnt/d/celebes-stress-inversion-project/data/batas-lempeng-dan-patahan/bird2003/PB2002_steps.shp")
#fig.plot(data=plate_boundary, pen="0.25p,black,-", label="Plate Boundary")