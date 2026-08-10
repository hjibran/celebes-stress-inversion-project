# This is where new functions used in calculations are stored
     
def unifying_direction(data):
    '''fungsi ini dibuat untuk mengembalikan azimut yang terbalik 180 derajat dari rata-rata hasil inversi'''

    import statistics as sts
    from matplotlib import pyplot as plt
    
    mode = sts.mode(data)
    up = mode + 90
    down = mode - 90
    if up > 350:
        up = up - 360
        bottom_part = [x for x in data if x < up]
        midle_part = [x+180 for x in data if up < x < down]
        upper_part = [x for x in data if x > down]
        temp = bottom_part + midle_part + upper_part
    elif down < 0:
        down = down + 360
        bottom_part = [x for x in data if x < up]
        midle_part = [x-180 for x in data if up < x < down]
        upper_part = [x for x in data if x > down]
        temp = bottom_part + midle_part + upper_part
    else:
        bottom_part = [x+180 for x in data if x < down]
        midle_part = [x for x in data if down < x < up]
        upper_part = [x-180 for x in data if x > up]
        temp = bottom_part + midle_part + upper_part
    
    indegree = [x for x in temp if 0 <= x <= 360]
    belowdegree = [x+360 for x in temp if x < 0]
    upperdegree = [x-360 for x in temp if x > 360]
    result = upperdegree + indegree + belowdegree
    result.sort()

    if mode < 180:
        temp1 = [x for x in result if x < mode+90]
        temp2 = [x-360 for x in result if x > mode+90]
        tempo = temp1 + temp2
    elif mode > 180:
        temp1 = [x+360 for x in result if x < mode-90]
        temp2 = [x for x in result if x > mode-90]
        tempo = temp1 + temp2

    return result, tempo

def percentil_calc(data):
    import numpy as np
    value = np.percentile(data, [2.5, 97.5])
    if value[0] < 0:
        value[0] += 360
    elif value[1] > 360:
        value[1] -= 360
    return value

def confidence_data(data):
    import numpy as np
    import pandas as pd
    
    dat, tempo = unifying_direction(data)

    # calculate error
    percentil = percentil_calc(tempo)
    down = percentil[0]
    up = percentil[1]
    if down < up:
        mid = (down+up)/2
        plusmin = (up-down)/2
    elif down > up:
        down -= 360
        mid = (down+up)/2
        plusmin = (up-down)/2
    
    if mid < 0:
        mid += 360
    
    if mid > 180:
        mid -= 180

    return '{:.2f}\u00B1{:.2f}'.format(mid, plusmin)

def struktur(fig, size, color):

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

    fig.plot(data=dir+in_subduct, style='f1/0.075i+l+t', pen="{}p,{}".format(a, color), fill=color)
    fig.plot(data=dir+'strikewalane.gmt', style='f5c/0.6c+l+s45+o0.60c', pen="{}p,{}".format(c, color))
    fig.plot(data=dir+'tambahanbaru1.gmt', pen="{}p,{}".format(c, color))
    fig.plot(data=dir+'walanethrust.gmt', style='f0.3/0.05i+l+t', pen="{}p,{}".format(c, color))
    fig.plot(data=dir+'butonthrust.gmt', style='f0.3/0.05i+r+t', pen="{}p,{}".format(c, color))
    fig.plot(data=dir+in_sesar, pen="{}p,{}".format(c, color))
    fig.plot(data=dir+in_tambah, style='f4c/0.6c+l+s45+o2.25c', pen="{}p,{}".format(c, color))
    fig.plot(data=dir+'jd1.gmt', style='f4c/0.6c+r+s45+o0.90c', pen="{}p,{}".format(c, color))
    fig.plot(data=dir+in_fault1, style='f4c/1c+l+s45+o2.25c', pen="{}p,{}".format(a, color))
    fig.plot(data=dir+in_fault2, pen="{}p,{},-".format(b, color))
    fig.plot(data=dir+in_thrust, style='f1/0.06i+l+t', pen="{}p,{}".format(b, color))
    fig.plot(data=dir+tolo, style='f1/0.06i+r+t', pen="{}p,{}".format(b, color))
    fig.plot(data=dir+in_thrust1, style='f1/0.06i+r+t', pen="{}p,{}".format(b, color))
    fig.plot(data=dir+pf, pen="{}p,{},-".format(b, color))
    fig.plot(data=dir+in_normalup, style='f0.5/0.05i+l+b', pen="{}p,{}".format(d, color), fill=color)
    fig.plot(data=dir+in_normaldown, style='f0.5/0.05i+r+b', pen="{}p,{}".format(d, color), fill=color)

    fig.plot(data=dir+'weluki.gmt', style='f1/0.06i+l+t', pen="{}p,{}".format(d, color))
    fig.plot(data=dir+'hal_dip.gmt', style='f1/0.075i+l+t', pen="{}p,{}".format(a, color), fill=color)
    fig.plot(data=dir+'hal_dip1.gmt', style='f1/0.075i+r+t', pen="{}p,{}".format(a, color), fill=color)
    fig.plot(data=dir+gtox, pen="{}p,{}".format(e, color))

    fig.plot(data=dir+mat, style='f4c/0.6c+l+s45+o2.25c', pen="{}p,{}".format(a1, color))
    fig.plot(data=dir+pff, pen="{}p,{},-".format(b, color))
    fig.plot(data=dir+sf, pen="{}p,{}".format(b, color))
    fig.plot(data=dir+tf, style='f0.3/0.06i+l+t', pen="{}p,{}".format(d, color))
    fig.plot(data=dir+tf1, style='f0.3/0.06i+r+t', pen="{}p,{}".format(d, color))
    fig.plot(data=dir+tf2, style='f0.3/0.06i+r+t', pen="{}p,{}".format(d, color))
    fig.plot(data=dir+hf, style='f5c/0.6c+l+s45+o1.25c', pen="{}p,{}".format(c, color))
    fig.plot(data=dir+nf, style='f0.5/0.05i+l+b', pen="{}p,{}".format(d, color), fill=color)
    fig.plot(data=dir+law1, style='f5c/0.6c+l+s45+o0.35c', pen="{}p,{}".format(c, color))
    fig.plot(data=dir+pan, pen="{}p,{}".format(d, color))
    fig.plot(data=dir+pan3, pen="{}p,{}".format(a1, color))
    fig.plot(data=dir+tam, pen="{}p,{}".format(c, color))
    fig.plot(data=dir+'faultsulawesi1.gmt', pen="{}p,{}".format(c, color))

    fig.plot(data=dir+'trench.gmt', style='f1/0.075i+l+t', pen="{}p,{}".format(a, color), fill=color)
    fig.plot(data=dir+'indonesiafaults.gmt', pen="{}p,{}".format(c, color))

def valueerror2downup(valueerror):
    value, error = valueerror.split('\u00B1')
    down = float(value)-float(error)
    up = float(value)+float(error)
    if down < 0:
        down += 360
    if up > 360:
        up -+ 360
    return down, up

def shmax_plot(fig, lon, lat, valueerror, fill, size=2.8, trans=40):
    down, up = valueerror2downup(valueerror)

    if down <=180:
        down1 = down+180
    elif down > 180:
        down1 = down -180
    if up <=180:
        up1 = up+180
    elif up > 180:
        up1 = up -180
    
    data = [[lon, lat, 360-up+90, 360-down+90], [lon, lat, 360-up1+90, 360-down1+90]]
    fig.plot(data=data, style="w{}c".format(size), fill=fill, cmap=False, transparency=trans, pen="black")

def tabel_frame(fig, minlon,maxlon,minlat,maxlat):
    import pandas as pd

    kotak = pd.DataFrame({
    "x":[minlon, maxlon,  maxlon,  minlon, minlon],
    "y":[minlat,  minlat, maxlat, maxlat,  minlat]
    })
    fig.plot(data=kotak, fill="white", pen="2p,black")
