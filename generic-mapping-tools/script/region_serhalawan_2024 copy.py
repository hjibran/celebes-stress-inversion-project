import pygmt
import pandas as pd
import geopandas as gpd

def principal_stress(lon, lat, direction, regime):
    if regime == "C":
        fill = 'red'

        pen='9p,{}'.format(fill)
        length = 2.5
        style='v1c+ba'

        fig.plot(
            x=[lon],
            y=[lat],
            style=style,
            direction=[[-(direction-360)-90], [length]],
            pen=pen,
            fill=fill,
        )

        fig.plot(
            x=[lon],
            y=[lat],
            style=style,
            direction=[[-(direction-360)-90], [-length]],
            pen=pen,
            fill=fill,
        )
    elif regime == "SS":
        fill = 'red'

        pen='9p,{}'.format(fill)
        length = 2.5
        style='v1c+ba'

        fig.plot(
            x=[lon],
            y=[lat],
            style=style,
            direction=[[-(direction-360)-90], [length]],
            pen=pen,
            fill=fill,
        )

        fig.plot(
            x=[lon],
            y=[lat],
            style=style,
            direction=[[-(direction-360)-90], [-length]],
            pen=pen,
            fill=fill,
        )

        fill = 'blue'
        
        pen='9p,{}'.format(fill)
        length = 2
        style='v1c+e'

        fig.plot(
            x=[lon-0.025],
            y=[lat+0.025],
            style=style,
            direction=[[-(direction-360)-180], [-length]],
            pen=pen,
            fill=fill,
        )

        fig.plot(
            x=[lon+0.025],
            y=[lat-0.025],
            style=style,
            direction=[[-(direction-360)-180], [length]],
            pen=pen,
            fill=fill,
        )

    elif regime == "E":
        fill = 'blue'
        
        pen='9p,{}'.format(fill)
        length = 2
        style='v1c+e'

        fig.plot(
            x=[lon-0.025],
            y=[lat-0.025],
            style=style,
            direction=[[-(direction-360)-180], [-length]],
            pen=pen,
            fill=fill,
        )

        fig.plot(
            x=[lon+0.025],
            y=[lat+0.025],
            style=style,
            direction=[[-(direction-360)-180], [length]],
            pen=pen,
            fill=fill,
        )

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

    fig.plot(data=dir+in_subduct, style='f2/0.15i+l+t', pen="{}p,{}".format(a, color), fill=color)
    fig.plot(data=dir+'strikewalane.gmt', style='f5c/0.6c+l+s45+o0.60c', pen="{}p,{}".format(c, color))
    fig.plot(data=dir+'tambahanbaru1.gmt', pen="{}p,{}".format(c, color))
    fig.plot(data=dir+'walanethrust.gmt', style='f0.6/0.1i+l+t', pen="{}p,{}".format(c, color))
    fig.plot(data=dir+'butonthrust.gmt', style='f0.6/0.1i+r+t', pen="{}p,{}".format(c, color))
    fig.plot(data=dir+in_sesar, pen="{}p,{}".format(c, color))
    fig.plot(data=dir+in_tambah, style='f4c/0.6c+l+s45+o2.25c', pen="{}p,{}".format(c, color))
    fig.plot(data=dir+'jd1.gmt', style='f4c/0.6c+r+s45+o0.90c', pen="{}p,{}".format(c, color))
    fig.plot(data=dir+in_fault1, style='f4c/1c+l+s45+o2.25c', pen="{}p,{}".format(a, color)) # Palu-Koro
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

    fig.plot(data=dir+mat, style='f4c/0.6c+l+s45+o2.25c', pen="{}p,{}".format(a1, color)) # Matano
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
    fig.plot(data=dir+'indonesiafaults.gmt', pen="{}p,{}".format(d, color))
    
fig = pygmt.Figure()
grid = pygmt.datasets.load_earth_relief(resolution="30s", # resolution of earth relief
                                        region= [117.9, 126.2, -7.2, 2.5], #[117.5, 128, -9, 6] boarder of map: [minlon, maxlon, minlat, maxlat]
                                        registration="gridline")

pygmt.makecpt(cmap='terra', series=f"{-12000}/{6000}/{1}")

fig.grdimage(grid=grid, # call grid
             frame=["a", "EWSN"],
             projection="M30c",
             cmap= 'geo',
             shading = True#"/mnt/d/celebes-stress-inversion-project/generic-mapping-tools/script/color.cpt"
)

#fig.coast(
#    water='white',
#    land='white',
#    shorelines='3p,dimgray'
#    )

""" 
kecepatan = pd.read_csv('/mnt/d/celebes-stress-inversion-project/data/Soquet2006/kecepatan_euler.csv')
plot = True
if plot == 1:
    fig.velo(
        data={
            'x': kecepatan['lon'],
            'y' :kecepatan['lat'],
            "east_velocity": kecepatan['x'],
            "north_velocity": kecepatan['y'],
            #"east_sigma": data['dVlon'],
            #"north_sigma": data['dVlon'],
            #"correlation_EN": data['Corr.']
        },
        spec="e0.075/0.001+f1",
        #uncertaintyfill="lightblue1",
        pen="2.5p,red",
        line=True,
        vector="0.75c+p1p+e+gred"
    )
 """
struktur(2.5, 'black')

#boundary = gpd.read_file("/mnt/d/celebes-stress-inversion-project/data/Soquet2006/soquet2006plateboundary(LN)disesuaikan.shp")
#fig.plot(data=boundary, pen="2.5p,red,-", label="microblock (Soquet, 2006)")

region = gpd.read_file("/mnt/d/celebes-stress-inversion-project/data/batas-lempeng-dan-patahan/segmentasiSerhalawan2024.shp")
fig.plot(data=region, pen="5p,red", label="microblock (Soquet, 2006)")

beaudouin = pd.read_csv('/mnt/d/celebes-stress-inversion-project/data/Beaudouin2003/Beaudouin-stress.csv')
#for i in range(len(beaudouin)):
    #principal_stress(beaudouin['lon'][i], beaudouin['lat'][i], beaudouin['Az1'][i], beaudouin['Regime'][i])

gempa_besar = pd.read_csv('/mnt/d/celebes-stress-inversion-project/data/gempa-besar-sulawesi-GCMT.csv', comment='#')

for i in range(len(gempa_besar)):
    fig.plot(
        x=gempa_besar['lon'][i],
        y=gempa_besar['lat'][i],
        style='a1.5c',
        fill='yellow',
        pen='2.5p,black'
    )
    fig.text(
        x=gempa_besar['lon'][i], 
        y=gempa_besar['lat'][i]-0.35,
        text=gempa_besar['ket'][i], 
        font="20p,Helvetica-Bold",
        fill='white'
    )

fig.basemap(rose="jBL+3c+lW,E,S,N+o0.3c/0.3c+f2")

fig.show()