#!/home/haidir/celebes-stress-inversion-project/venv/bin/python3

import pygmt
import pandas as pd
import geopandas as gpd

data = pd.read_csv("/mnt/d/celebes-stress-inversion-project/data/siap-olah/fm50km7mw.csv")
FM = data.iloc[:, [3, 2, 4, 6, 7, 8, 5]]
FM.columns = ["longitude", "latitude", "depth", "strike", "dip", "rake", "magnitude"]
buffer03515 = gpd.read_file("/mnt/d/celebes-stress-inversion-project/Result/eps0.35min15-final/eps0.35pts15.shp")
buffer04015 = gpd.read_file("/mnt/d/celebes-stress-inversion-project/Result/eps0.40min15-final/eps0.40pts15.shp")
buffer05015 = gpd.read_file("/mnt/d/celebes-stress-inversion-project/Result/eps0.50min15-final/eps0.50pts15.shp")

# download and store earth relief
grid = pygmt.datasets.load_earth_relief(resolution="30s", # resolution of earth relief
                                        region=[117.4, 129.6, -9.3, 6.7], #[117.5, 128, -9, 6] boarder of map: [minlon, maxlon, minlat, maxlat]
                                        registration="gridline")
fig = pygmt.Figure()

# plot grid image
fig.grdimage(grid=grid, # call grid
             frame=["a", "EWSN"],#, "+tPulau Sulawesi"],
             projection="M75c",
             cmap= "/mnt/d/celebes-stress-inversion-project/generic-mapping-tools/script/color.cpt")
fig.coast(water="white")

def struktur(size, color):

    a = size * 2 
    a1 = size * 1.5
    b = size * 1
    c = size * 0.9
    d = size * 0.8
    e = size * 0.4

    dir='/mnt/d/celebes-stress-inversion-project/data/GMT_Seismotectonics_of_Sulawesi/'
    in_fault1='strikeslipsulawesihall.gmt'
    in_fault2='strikeslipsulawesi2.gmt'
    in_thrust='thrustsulawesi.gmt'
    in_thrust1='batuithrust.gmt'
    in_subduct='sulawesisubduksihall.gmt'
    in_normalup='mmcup.gmt'
    in_normaldown='mmcdown.gmt'
    in_sesar='sesar.gmt'
    in_tambah='jd.gmt'
    gtox='gorotaloextension.gmt'

    mat='mat.gmt'
    hf='hf.gmt'
    law1='law1.gmt'
    tolo='tolo.gmt'
    pf='pf1.gmt'
    pff='pff.gmt'
    tf='tf.gmt'
    tf1='tf1.gmt'
    tf2='tf2.gmt'
    nf='nf.gmt'
    nf1='nf1.gmt'
    sf='sf.gmt'
    pan='pann.gmt'
    pan3='pan3.gmt'
    tam='tam.gmt'
    blocks='newblocks.gmt'
    regions='new.gmt'
    volcano = 'volcano.txt'

    fig.plot(data=dir+in_subduct, style='f2/0.15i+l+t', pen="{}p,{}".format(a, color), fill=color)
    fig.plot(data=dir+'strikewalane.gmt', style='f5c/0.6c+l+s45+o0.60c', pen="{}p,{}".format(c, color))
    fig.plot(data=dir+'tambahanbaru1.gmt', pen="{}p,{}".format(c, color))
    fig.plot(data=dir+'walanethrust.gmt', style='f0.6/0.1i+l+t', pen="{}p,{}".format(c, color))
    fig.plot(data=dir+'butonthrust.gmt', style='f0.6/0.1i+r+t', pen="{}p,{}".format(c, color))
    fig.plot(data=dir+in_sesar, pen="{}p,{}".format(c, color))
    fig.plot(data=dir+in_tambah, style='f4c/0.6c+l+s45+o2.25c', pen="{}p,{}".format(c, color))
    fig.plot(data=dir+'jd1.gmt', style='f4c/0.6c+r+s45+o0.90c', pen="{}p,{}".format(c, color))
    fig.plot(data=dir+in_fault1, style='f4c/1c+l+s45+o2.25c', pen="{}p,{}".format(a, color))
    fig.plot(data=dir+in_fault2, pen="{}p,{},-".format(b, color))
    fig.plot(data=dir+in_thrust, style='f1/0.1i+l+t', pen="{}p,{}".format(b, color))
    fig.plot(data=dir+tolo, style='f1/0.1i+r+t', pen="{}p,{}".format(b, color))
    fig.plot(data=dir+in_thrust1, style='f1/0.1i+r+t', pen="{}p,{}".format(b, color))
    fig.plot(data=dir+pf, pen="{}p,{},-".format(b, color))
    fig.plot(data=dir+in_normalup, style='f0.5/0.05i+l+b', pen="{}p,{}".format(d, color), fill=color)
    fig.plot(data=dir+in_normaldown, style='f0.5/0.05i+r+b', pen="{}p,{}".format(d, color), fill=color)

    fig.plot(data=dir+'weluki.gmt', style='f1/0.05i+l+t', pen="{}p,{}".format(d, color))
    fig.plot(data=dir+'hal_dip.gmt', style='f2/0.15i+l+t', pen="{}p,{}".format(a, color), fill=color)
    fig.plot(data=dir+'hal_dip1.gmt', style='f2/0.15i+r+t', pen="{}p,{}".format(a, color), fill=color)
    fig.plot(data=dir+gtox, pen="{}p,{}".format(e, color))

    fig.plot(data=dir+mat, style='f4c/0.6c+l+s45+o2.25c', pen="{}p,{}".format(a1, color))
    fig.plot(data=dir+pff, pen="{}p,{},-".format(b, color))
    fig.plot(data=dir+sf, pen="{}p,{}".format(b, color))
    fig.plot(data=dir+tf, style='f0.6/0.1i+l+t', pen="{}p,{}".format(d, color))
    fig.plot(data=dir+tf1, style='f0.6/0.1i+r+t', pen="{}p,{}".format(d, color))
    fig.plot(data=dir+tf2, style='f0.6/0.1i+r+t', pen="{}p,{}".format(d, color))
    fig.plot(data=dir+hf, style='f5c/0.6c+l+s45+o1.25c', pen="{}p,{}".format(c, color))
    fig.plot(data=dir+nf, style='f0.5/0.05i+l+b', pen="{}p,{}".format(d, color), fill=color)
    fig.plot(data=dir+law1, style='f5c/0.6c+l+s45+o0.35c', pen="{}p,{}".format(c, color))
    fig.plot(data=dir+pan, pen="{}p,{}".format(d, color))
    fig.plot(data=dir+pan3, pen="{}p,{}".format(a1, color))
    fig.plot(data=dir+tam, pen="{}p,{}".format(c, color))
    fig.plot(data=dir+'faultsulawesi1.gmt', pen="{}p,{}".format(c, color))

    fig.plot(data=dir+'trench.gmt', style='f2/0.15i+l+t', pen="{}p,{}".format(a, color), fill=color)
    fig.plot(data=dir+'indonesiafaults.gmt', pen="{}p,{}".format(c, color))

struktur(3, 'black')

fig.plot(x=FM.longitude, y=FM.latitude, style="c0.375c", fill='darkgray', pen='black', label='Epicenter')

fig.plot(data=buffer03515, pen="7.5p,springgreen3", label="ε=0.35 MinPts=15")
fig.plot(data=buffer04015, pen="7.5p,gold2", label="ε=0.40 MinPts=15")
fig.plot(data=buffer05015, pen="7.5p,tomato", label="ε=0.50 MinPts=15")

utara=[117.5, 126, -3.55, 3.5]
selatan=[118.5, 123, -4.5, -1.7]
maluku=[123.3, 129.5, -2.05, 5.3]
sula=[125.5, 128, -3.5, -2.25]
sangihe=[124.4, 126.9, 4, 6.6]
ntt=[124.2, 126.8, -9.2, -7.2]
def inset(R):
    x = [R[0], R[1], R[1], R[0], R[0]]
    y = [R[2], R[2], R[3], R[3], R[2]]
    return x, y
for i in [utara, selatan, maluku, sula, sangihe, ntt]:
    x, y = inset(i)
    fig.plot(x=x,
             y=y,
             pen='4p,black'
    )


fill = "red"
fig.plot(x=119.4, y=-5.16, style="s0.9375c", fill=fill, pen="3.75p,black", label="Provincial capital")
fig.plot(x=119.8, y=-0.90, style="s0.9375c", fill=fill, pen="3.75p,black")
fig.plot(x=118.9, y=-2.68, style="s0.9375c", fill=fill, pen="3.75p,black")
fig.plot(x=122.6, y=-3.97, style="s0.9375c", fill=fill, pen="3.75p,black")
fig.plot(x=123.1, y=0.54, style="s0.9375c", fill=fill, pen="3.75p,black")
fig.plot(x=124.8, y=1.49, style="s0.9375c", fill=fill, pen="3.75p,black")

font = "48.75p,Helvetica-Bold,black"
fig.text(x=118.8, y=-4.7, text="Makassar", font=font)
fig.plot(x=[118.8, 119.4], y=[-4.85, -5.16], pen="5.625p,black")
fig.text(x=118.70, y=-0.65, text="Palu", font=font)
fig.plot(x=[118.95, 119.8], y=[-0.65, -0.90], pen="5.625p,black")
fig.text(x=118.0, y=-2.40, text="Mamuju", font=font)
fig.plot(x=[118.45, 118.9], y=[-2.45, -2.68], pen="5.625p,black")
fig.text(x=122.0, y=-4.31, text="Kendari", font=font)
fig.plot(x=[122.0, 122.6], y=[-4.21, -3.97], pen="5.625p,black")
fig.text(x=122.1, y=0.38, text="Gorontalo", font=font)
fig.plot(x=[122.65, 123.1], y=[0.38, 0.54], pen="5.625p,black")
fig.text(x=124.7, y=2, text="Manado", font=font)
fig.plot(x=[124.7, 124.8], y=[1.88, 1.49], pen="5.625p,black")

fig.basemap(
    rose="jBL+w6.75c+lW,E,S,N+o5c/10+f2"
) 

fig.show()