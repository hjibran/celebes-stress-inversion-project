import os
import pygmt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
   

def plot(path, region, ukuran, lokasirose):
    fig = pygmt.Figure()
    #sebaran = np.array([0,3])
    #os.system('gmt makecpt -Cdarkblue,blue,green,red,darkred -T0/3/0.02 -Z > /mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Output/shmax/custom.cpt')
    #pygmt.makecpt(cmap="/mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Output/shmax/custom.cpt", 
    #              series=[sebaran.min(), sebaran.max()])


    grid = pygmt.datasets.load_earth_relief(resolution="30s", # resolution of earth relief
                                            registration="gridline",
                                            region=region,
                                            )

    fig.grdimage(grid=grid,
                 projection='M10c',
                 frame=["a1", "EWSN"],
                 cmap= "/mnt/d/celebes-stress-inversion-project/generic-mapping-tools/script/color.cpt")
    fig.coast(region=region,
              resolution='f',
              water='white'
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
    
        fig.plot(data=dir+in_subduct, style='f2/0.075i+l+t', pen="{}p,{}".format(a, color), fill=color)
        fig.plot(data=dir+'strikewalane.gmt', style='f5c/0.3c+l+s45+o0.60c', pen="{}p,{}".format(c, color))
        fig.plot(data=dir+'tambahanbaru1.gmt', pen="{}p,{}".format(c, color))
        fig.plot(data=dir+'walanethrust.gmt', style='f0.6/0.05i+l+t', pen="{}p,{}".format(c, color))
        fig.plot(data=dir+'butonthrust.gmt', style='f0.6/0.05i+r+t', pen="{}p,{}".format(c, color))
        fig.plot(data=dir+in_sesar, pen="{}p,{}".format(c, color))
        fig.plot(data=dir+in_tambah, style='f4c/0.3c+l+s45+o2.25c', pen="{}p,{}".format(c, color))
        fig.plot(data=dir+'jd1.gmt', style='f4c/0.3c+r+s45+o0.90c', pen="{}p,{}".format(c, color))
        fig.plot(data=dir+in_fault1, style='f4c/0.5c+l+s45+o2.25c', pen="{}p,{}".format(a, color))
        fig.plot(data=dir+in_fault2, pen="{}p,{},-".format(b, color))
        fig.plot(data=dir+in_thrust, style='f1/0.05i+l+t', pen="{}p,{}".format(b, color))
        fig.plot(data=dir+tolo, style='f1/0.05i+r+t', pen="{}p,{}".format(b, color))
        fig.plot(data=dir+in_thrust1, style='f1/0.05i+r+t', pen="{}p,{}".format(b, color))
        fig.plot(data=dir+pf, pen="{}p,{},-".format(b, color))
        fig.plot(data=dir+in_normalup, style='f0.5/0.025i+l+b', pen="{}p,{}".format(d, color), fill=color)
        fig.plot(data=dir+in_normaldown, style='f0.5/0.025i+r+b', pen="{}p,{}".format(d, color), fill=color)
    
        fig.plot(data=dir+'weluki.gmt', style='f1/0.025i+l+t', pen="{}p,{}".format(d, color))
        fig.plot(data=dir+'hal_dip.gmt', style='f2/0.075i+l+t', pen="{}p,{}".format(a, color), fill=color)
        fig.plot(data=dir+'hal_dip1.gmt', style='f2/0.075i+r+t', pen="{}p,{}".format(a, color), fill=color)
        fig.plot(data=dir+gtox, pen="{}p,{}".format(e, color))
    
        fig.plot(data=dir+mat, style='f4c/0.3c+l+s45+o2.25c', pen="{}p,{}".format(a1, color))
        fig.plot(data=dir+pff, pen="{}p,{},-".format(b, color))
        fig.plot(data=dir+sf, pen="{}p,{}".format(b, color))
        fig.plot(data=dir+tf, style='f0.6/0.05i+l+t', pen="{}p,{}".format(d, color))
        fig.plot(data=dir+tf1, style='f0.6/0.05i+r+t', pen="{}p,{}".format(d, color))
        fig.plot(data=dir+tf2, style='f0.6/0.05i+r+t', pen="{}p,{}".format(d, color))
        fig.plot(data=dir+hf, style='f5c/0.3c+l+s45+o1.25c', pen="{}p,{}".format(c, color))
        fig.plot(data=dir+nf, style='f0.5/0.025i+l+b', pen="{}p,{}".format(d, color), fill=color)
        fig.plot(data=dir+law1, style='f5c/0.3c+l+s45+o0.35c', pen="{}p,{}".format(c, color))
        fig.plot(data=dir+pan, pen="{}p,{}".format(d, color))
        fig.plot(data=dir+pan3, pen="{}p,{}".format(a1, color))
        fig.plot(data=dir+tam, pen="{}p,{}".format(c, color))
        fig.plot(data=dir+'faultsulawesi1.gmt', pen="{}p,{}".format(c, color))
    
        fig.plot(data=dir+'trench.gmt', style='f2/0.075i+l+t', pen="{}p,{}".format(a, color), fill=color)
        fig.plot(data=dir+'indonesiafaults.gmt', pen="{}p,{}".format(c, color))
    
    struktur(0.5, 'dimgray')

    table = pd.read_csv(path)
    table1 = table
    table1 = table1.reset_index()
    FM = table1.iloc[:, [2, 3, 4, 5, 6, 7, 11]]
    FM.columns = ["longitude", "latitude", "depth", "strike", "dip", "rake", "magnitude"]

    def shmax_plot(lon, lat, down, up, AR, clus, ukuran):
        if down <=180:
            down1 = down+180
        elif down > 180:
            down1 = down -180
        if up <=180:
            up1 = up+180
        elif up > 180:
            up1 = up -180
        
        if 0 <= AR < 0.25:
            fill = "darkblue"
        elif 0.25 <= AR < 0.75:
            fill = "blue"
        elif 0.75 <= AR < 1.25:
            fill = "green"
        elif 1.25 <= AR < 1.75:
            fill = "yellow"
        elif 1.75 <= AR < 2.25:
            fill = "orange"
        elif 2.25 <= AR < 2.75:
            fill = "red"
        else:
            fill = "darkred"
    
        if clus == 15.35:
            pen = '0.5p,springgreen3'
        elif clus == 15.40:
            pen = '0.5p,gold2'
        elif clus == 15.50:
            pen = '0.5p,tomato'
        data = [[lon, lat, 360-up+90, 360-down+90], [lon, lat, 360-up1+90, 360-down1+90]]
        fig.plot(data=data, style=ukuran, fill=fill, cmap=False, transparency=25, pen=pen)


    for i in range(len(table1)):
        shmax_plot(table1['lon'][i], table1['lat'][i], table1['down'][i], table1['up'][i], table1['AR'][i], table1['name'][i], ukuran)
    fig.basemap(rose="j{}+w1.2c+lW,E,S,N+o0.1c/0.1c+f2".format(lokasirose)) 
    fig.show()

    return fig

utara = plot("/mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Output/shmax/shmax_bagian_utara.csv", 
            [117.5, 126, -3.5, 3.5],
            "w1.25c", 'BR')
selatan = plot("/mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Output/shmax/shmax_bagian_selatan.csv", 
            [118.5, 123, -4.5, -1.7],
            "w1.5c", 'TL')
maluku1 = plot("/mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Output/shmax/shmax_wilayah_barat_sangihe.csv", 
            [124.4, 126.9, 4, 6.6],
            "w2c", 'BL')
maluku2 = plot("/mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Output/shmax/shmax_wilayah_laut_maluku.csv", 
            [123.3, 129.5, -2.05, 5.3],
            "w2c", 'BL')
sula = plot("/mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Output/shmax/shmax_wilayah_sula.csv", 
            [125.5, 128, -3.5, -2.25],
            "w2c", 'BL')
ntt = plot("/mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Output/shmax/shmax_wilayah_nusa_tenggara_timur.csv", 
            [124.2, 126.8, -9.2, -7.2],
            "w2c", 'TL')
