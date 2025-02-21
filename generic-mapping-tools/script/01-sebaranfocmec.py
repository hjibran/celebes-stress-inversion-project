#!/home/haidir/celebes-stress-inversion-project/venv/bin/python3


# import module
import pygmt
import numpy as np
import geopandas as gpd
import pandas as pd

# download and store earth relief
grid = pygmt.datasets.load_earth_relief(resolution="30s", # resolution of earth relief
                                        region=[117.5, 127.5, -8.5, 5.5], # boarder of map: [minlon, maxlon, minlat, maxlat]
                                        registration="gridline")
# begin fig object
fig = pygmt.Figure()

# plot grid image
fig.grdimage(grid=grid, # call grid
             frame=["a", "EWSN"],#, "+tPulau Sulawesi"],
             projection="M10c",
             cmap= 'gray'#"/mnt/d/celebes-stress-inversion-project/generic-mapping-tools/script/color.cpt"
)
fig.coast(shorelines='1p,black'

)

# display color bar from grid image
#fig.colorbar(frame=["a3000f1000", "x+lElevation", "y+lm"],
#             position="JBL+w6+o2/1.6c+h")

# plot fault
fig.plot(data="/mnt/d/celebes-stress-inversion-project/data/batas-lempeng-dan-patahan/indonesiafaults.gmt",
         pen="0.75p,black")

# plot trench
fig.plot(data="/mnt/d/celebes-stress-inversion-project/data/batas-lempeng-dan-patahan/trench.gmt",
         pen="0.75p,black",
         style="f1c/0.1c+l+t",
         fill="black")


fill = "black"
fig.plot(x=119.4, y=-5.16, style="s0.175c", fill=fill, pen="1p,black")
fig.plot(x=119.8, y=-0.90, style="s0.175c", fill=fill, pen="1p,black")
fig.plot(x=118.9, y=-2.68, style="s0.175c", fill=fill, pen="1p,black")
fig.plot(x=122.6, y=-3.97, style="s0.175c", fill=fill, pen="1p,black")
fig.plot(x=123.1, y=0.54, style="s0.175c", fill=fill, pen="1p,black")
fig.plot(x=124.8, y=1.49, style="s0.175c", fill=fill, pen="1p,black")

font = "6.5p,Helvetica-Bold,black"
fig.text(x=118.8, y=-4.7, text="Makassar", font=font)
fig.plot(x=[118.8, 119.4], y=[-4.85, -5.16], pen="0.75p,black")
fig.text(x=118.70, y=-0.65, text="Palu", font=font)
fig.plot(x=[118.95, 119.8], y=[-0.65, -0.90], pen="0.75p,black")
fig.text(x=118.0, y=-2.30, text="Mamuju", font=font)
fig.plot(x=[118.45, 118.9], y=[-2.30, -2.68], pen="0.75p,black")
fig.text(x=122.0, y=-4.49, text="Kendari", font=font)
fig.plot(x=[122.0, 122.6], y=[-4.39, -3.97], pen="0.75p,black")
fig.text(x=122.1, y=0, text="Gorontalo", font=font)
fig.plot(x=[122.65, 123.1], y=[0, 0.54], pen="0.75p,black")
fig.text(x=124.7, y=2, text="Manado", font=font)
fig.plot(x=[124.7, 124.8], y=[1.88, 1.49], pen="0.75p,black")

# plot focal mecanism
fm = pd.read_csv("/mnt/d/celebes-stress-inversion-project/data/siap-olah/fm50km7mw.csv")
FM = fm.iloc[:, [3, 2, 4, 6, 7, 8, 5]]
FM.columns = ["longitude", "latitude", "depth", "strike", "dip", "rake", "magnitude"]


#make color ramp for depth
#depth_group = []
#for i in range(len(FM)):
#    if 0 <= FM['depth'][i] < 10:
#        group = '0-10'
#    elif 10 <= FM['depth'][i] < 20:
#        group = '10-20'
#    elif 20 <= FM['depth'][i] < 30:
#        group = '20-30'
#    elif 30 <= FM['depth'][i] < 40:
#        group = '30-40'
#    elif 40 <= FM['depth'][i] <= 50:
#        group = '40-50'
#    depth_group.append(group)
#depth_group = pd.DataFrame(np.array(depth_group), columns=['group'])

pygmt.makecpt(cmap="seis", 
              reverse = True, 
              series=[FM.depth.min(),FM.depth.max(), 10],
              #color_model="+c0-10,10-20,20-30,30-40,40-50",
)
#Plot erathquake based on depth
fig.plot(x = FM.longitude,
         y = FM.latitude,
         size = 0.001 * (2**FM.magnitude),
         pen ="faint",
         style ="c0.15",
         fill = FM.depth,
         cmap = True)

#Plot Data Focal Mechanisme
fig.meca(spec=FM,
         cmap = True,
         pen="0.2p,black,solid",
         scale ="0.2c",
         frame = True)

#fig.colorbar(
#    cmap=True,  # Use colormap set up above
#    # Colorbar placed inside the plot bounding box (j) in the Bottom Left (BL) corner,
#    # with an offset (+o) by 0.5 cm horizontally and 0.8 cm vertically from the anchor
#    # point, and plotted horizontally (+h)
#    position="JBL+o0.5c/0.4c+w-10c/1.75c",
#    #box='white',
#    # Divide colorbar into equal-sized rectangles
#    equalsize=0.5,
#)

fig.basemap(rose="jTL+w0.9c+lW,E,S,N+o0.3c/0.3c+f2",
             #map_scale="jTL+w200k+o0.45c/0.5c+f+lkm",
             ) 
#fig.legend(position="jTL+o0.2/1.6c", box=True)

# Plot colorbar
#fig.colorbar(frame=["x+lDepth (km)"],#"af+l'Depth (km)'", 
#             position="JMR+w-10/0.5+o3/0c+mn+")#+w-3/0.25+o0.3/0.3c+mn+")

# show picture
fig.show()
#fig.savefig("/mnt/d/celebes-stress-inversion-project/generic-mapping-tools/maps/basemap.pdf")
#plate_boundary = gpd.read_file("/mnt/d/celebes-stress-inversion-project/data/batas-lempeng-dan-patahan/bird2003/PB2002_steps.shp")
#fig.plot(data=plate_boundary, pen="0.25p,black,-", label="Plate Boundary")