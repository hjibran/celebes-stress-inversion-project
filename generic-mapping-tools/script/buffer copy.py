#!/home/haidir/celebes-stress-inversion-project/venv/bin/python3

import pygmt
import pandas as pd
import geopandas as gpd

def buat_peta(cls, gambar):

    Data = pd.read_csv("/mnt/d/celebes-stress-inversion-project/data/siap-olah/fm50km7mw.csv")
    FM = Data.iloc[:, [3, 2, 4, 6, 7, 8, 5]]
    FM.columns = ["longitude", "latitude", "depth", "strike", "dip", "rake", "magnitude"]
    buffer = gpd.read_file("/mnt/d/celebes-stress-inversion-project/Result/tanpa-gempa-diatas-7-mw-diurut-berdasarkan-waktu/batas-cluster/cls{}.shp".format(cls))

    data = pd.read_csv("/mnt/d/celebes-stress-inversion-project/Result/tanpa-gempa-diatas-7-mw-diurut-berdasarkan-waktu/eps0.40min15/clustered/cls{}.csv".format(cls))
    fm = data.iloc[:, [3, 2, 4, 6, 7, 8, 5]]
    fm.columns = ["longitude", "latitude", "depth", "strike", "dip", "rake", "magnitude"]

    west = fm.longitude.min()
    east = fm. longitude.max()
    south = fm.latitude.min()
    north = fm.latitude.max()
    lon_avr = (west + east)/2
    lat_avr = (south + north)/2
    if east-lon_avr > lon_avr-west:
        jarak_lon = east-lon_avr
    else:
        jarak_lon = lon_avr-west
   
    if north-lat_avr > lat_avr-south:
        jarak_lat = north-lat_avr
    else:
        jarak_lat = lat_avr-south

    if jarak_lon > jarak_lat:
        left = lon_avr - jarak_lon - 0.5
        right = lon_avr + jarak_lon + 0.5
        down = lat_avr - jarak_lon - 0.5
        up = lat_avr + jarak_lon + 0.5
    else:
        left = lon_avr - jarak_lat - 0.5
        right = lon_avr + jarak_lat + 0.5
        down = lat_avr - jarak_lat - 0.5
        up = lat_avr + jarak_lat + 0.5

    fig = pygmt.Figure()
    fig.basemap(region=[left, right, down, up], frame=["WNES", "a"], projection="M20c")
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
    fig.meca(
        spec=FM,
        compressionfill="grey",
        scale="0.5c",
        extensionfill="white",
    )
    fig.meca(
        spec=fm,
        compressionfill="black",
        scale="0.5c",
        extensionfill="white",
    )
    fig.plot(data=buffer, pen="1p,black", label="ε=0.40 MinPts=15")

    fill = "red"
    fig.plot(x=119.4, y=-5.16, style="s0.25c", fill=fill, pen="1p,black")
    fig.plot(x=119.8, y=-0.90, style="s0.25c", fill=fill, pen="1p,black")
    fig.plot(x=118.9, y=-2.68, style="s0.25c", fill=fill, pen="1p,black")
    fig.plot(x=122.6, y=-3.97, style="s0.25c", fill=fill, pen="1p,black")
    #fig.plot(x=123.1, y=0.54, style="s0.25c", fill=fill, pen="1p,black")
    fig.plot(x=124.8, y=1.49, style="s0.25c", fill=fill, pen="1p,black")

    font = "20p,Helvetica-Bold,black"
    fig.text(x=118.8, y=-4.7, text="Makassar", font=font)
    fig.plot(x=[118.8, 119.4], y=[-4.85, -5.16], pen="1.5p,black")
    fig.text(x=119.20, y=-0.65, text="Palu", font=font)
    fig.plot(x=[119.32, 119.8], y=[-0.65, -0.90], pen="2.5p,black")
    fig.text(x=118.0, y=-2.40, text="Mamuju", font=font)
    fig.plot(x=[118.45, 118.9], y=[-2.45, -2.68], pen="1.5p,black")
    fig.text(x=122.0, y=-4.31, text="Kendari", font=font)
    fig.plot(x=[122.0, 122.6], y=[-4.21, -3.97], pen="1.5p,black")
    #fig.text(x=122.1, y=0.38, text="Gorontalo", font=font)
    #fig.plot(x=[122.65, 123.1], y=[0.38, 0.54], pen="1.5p,black")
    fig.text(x=124.7, y=2, text="Manado", font=font)
    fig.plot(x=[124.7, 124.8], y=[1.88, 1.49], pen="2.5p,black")

    #fig.basemap(
    #    rose="jBL+w1.8c+lW,E,S,N+o4.5c/0.5c+f2",
    #    map_scale="jBL+w200k+o0.45c/0.5c+f+lkm"
    #) 
    #fig.legend(position="jBL+o0.2/1.6c", box=True)

    if gambar == 1:
        fig.savefig("/mnt/d/celebes-stress-inversion-project/generic-mapping-tools/maps/class{}.png".format(cls))
    elif gambar == 0:
        fig.show()



    #jika gambar 0 maka hanya ditampilkan
    #jika gambar 1 akan di simpan
buat_peta(0,1)