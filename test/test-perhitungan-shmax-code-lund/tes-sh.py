import numpy as np
import pandas as pd
import function as f
from SH_lund import SH as lund
from SHmax_calc import shmax_dir as shcalc
from function import confidence_data as cd
from function import struktur
from function import shmax_plot

eps = 0.35

lunds = []
selfs = []
for cluster in range(10):
    if eps == 0.40:
        data = pd.read_csv('/mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Output/eps0.40pts15/new_shmax/cls{}/output_bootstarap_with_simpson.csv'.format(cluster))
    else:
        data = pd.read_csv('/mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Output/eps{:.2f}pts15/cls{}/output_bootstarap_with_simpson.csv'.format(eps, cluster))
        
    lund_calc = []
    self_calc = []

    Az1 = data['azimuth sigma 1']
    Pl1 = data['plunge sigma 1']
    Az2 = data['azimuth sigma 2']
    Pl2 = data['plunge sigma 2']
    Az3 = data['azimuth sigma 3']
    Pl3 = data['plunge sigma 3']
    R = data['shape ratio']

    N1 = np.cos(np.radians(Az1))*np.cos(np.radians(Pl1))
    N2 = np.cos(np.radians(Az2))*np.cos(np.radians(Pl2))
    N3 = np.cos(np.radians(Az3))*np.cos(np.radians(Pl3))
    E1 = np.sin(np.radians(Az1))*np.cos(np.radians(Pl1))
    E2 = np.sin(np.radians(Az2))*np.cos(np.radians(Pl2))
    E3 = np.sin(np.radians(Az3))*np.cos(np.radians(Pl3))
    D1 = np.sin(np.radians(Pl1))
    D2 = np.sin(np.radians(Pl2))
    D3 = np.sin(np.radians(Pl3))

    for i in range(len(data)):
        az1 = Az1[i]; pl1 = Pl1[i]
        az2 = Az2[i]; pl2 = Pl2[i]
        az3 = Az3[i]; pl3 = Pl3[i]
        s1 = [N1[i],E1[i],D1[i]]
        s2 = [N2[i],E2[i],D2[i]]
        s3 = [N3[i],E3[i],D3[i]]
        r = R[1]

        self=shcalc(az1,pl1,az2,pl2,r,True)
        lun=np.degrees(lund(s1,s2,s3,r))

        self_calc.append(self)
        lund_calc.append(lun)

        if self > 180:
            self -= 180
        if lun > 180:
            lun -= 180

        self = '{:.2f}'.format(self)
        lun = '{:.2f}'.format(lun)
        
        #if self != lun:
        #    print(cluster, i, self, lun, data['shape ratio'][i],data['simpson index'][i])

    lunds.append(cd(lund_calc))
    selfs.append(cd(self_calc))

tabel = pd.DataFrame(
    np.array([lunds, selfs]).T, 
    columns=['calculator lund', 'calculator buatan'])
#print(tabel)

#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
# Ploting Data
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
import pygmt
import geopandas as gpd
from sklearn.cluster import DBSCAN

grid = pygmt.datasets.load_earth_relief(
    resolution="30s", # resolution of earth relief
    region=[117.5, 127.5, -8.5, 5.5], # boarder of map: [minlon, maxlon, minlat, maxlat]
    registration="gridline"
)

fig = pygmt.Figure()

fig.grdimage(grid=grid, # call grid
             frame=["a", "EWSN"],#, "+tPulau Sulawesi"],
             projection="M20c",
             cmap= '/mnt/d/celebes-stress-inversion-project/test/test-perhitungan-shmax-code-lund/softearth.cpt',#"/mnt/d/celebes-stress-inversion-project/generic-mapping-tools/two_color.cpt",
             shading=True
)

#fig.basemap(region=[117.5, 127.5, -8.5, 5.5], frame=["WNES", "a"], projection="M20c")
#fig.coast(water="white")
struktur(fig, 0.75, 'dimgray')

buffer = gpd.read_file("/mnt/d/celebes-stress-inversion-project/Result/eps{:.2f}min15-final/eps{:.2f}pts15.shp".format(eps,eps))
#fig.plot(data=buffer, pen="2.5p,dimgray", label="Cluster Boundaries")

event = pd.read_csv("/mnt/d/celebes-stress-inversion-project/data/siap-olah/fm50km7mw.csv")
x = event.iloc[:, [3, 2]]
clustering = DBSCAN(eps=eps, min_samples=15).fit(x)
event["cluster"] = clustering.labels_

#FM = event.iloc[:, [3, 2, 4, 6, 7, 8, 5]]
#FM.columns = ["longitude", "latitude", "depth", "strike", "dip", "rake", "magnitude"]
#fig.meca(
#    spec=FM,
#    compressionfill='gray',
#    scale="0.2c",
#    extensionfill="white"
#)

f.tabel_frame(fig, 117.65, 123.5, -8.35, -4.3)
fig.plot(x=[117.65, 123.5], y=[-4.7, -4.7], pen='1.5p,black')
tebel_lon = 118.2; tabel_lat = -4.6
fig.text(x=tebel_lon, y=tabel_lat+0.08, text='Cluster', font="15p,Helvetica-Bold,black", fill='white')
fig.text(x=tebel_lon+1.7, y=tabel_lat+0.08, text="Self Calculation", font="15p,Helvetica-Bold,black", fill='white')
fig.text(x=tebel_lon+4.1, y=tabel_lat+0.08, text="Lund's Calculator", font="15p,Helvetica-Bold,black", fill='white')

banyak_cluster = event["cluster"].max()
for kelas in range(banyak_cluster+1):
    hasil = event[event["cluster"]==kelas]
    event_in_class = hasil.iloc[:, [3, 2]]
    event_in_class.columns = ["longitude", "latitude"]

    lon = sum(event_in_class.longitude)/len(event_in_class.longitude)
    lat = sum(event_in_class.latitude)/len(event_in_class.latitude)

    if tabel['calculator lund'][kelas] != tabel['calculator buatan'][kelas]:
        color='red'
    else:
        color='black'

    shmax_plot(fig, lon, lat, tabel['calculator buatan'][kelas], 'yellow', 2.8)
    shmax_plot(fig, lon, lat, tabel['calculator lund'][kelas], 'red',2.8)
    fig.text(
        x=lon,
        y=lat,
        text=kelas,#str(len(event_in_class)),
        font="20p,{}".format(color),
        fill='white'
    )

    fig.text(x=tebel_lon, y=tabel_lat-((kelas+1)*0.35), text=kelas, font="15p,{}".format(color), fill='white')
    fig.text(x=tebel_lon+1.7, y=tabel_lat-((kelas+1)*0.35), text=tabel['calculator buatan'][kelas], font="15p,{}".format(color), fill='white')
    fig.text(x=tebel_lon+4.1, y=tabel_lat-((kelas+1)*0.35), text=tabel['calculator lund'][kelas], font="15p,{}".format(color), fill='white')

f.tabel_frame(fig, 117.7, 122.9, 2.9, 5.4)
fig.text(x=120.3, y=5.2, text="Comparison of SHmax Calculation", font="17p,Helvetica-Bold,black", fill='white')
fig.text(x=119.785, y=4.85, text="Parameter: Eps{:.2f}minPts15".format(eps), font="16p,Helvetica-Bold,black", fill='white')
shmax_plot(fig, 118.5, 4.2, '45\u00B125', 'yellow', 1.5)
shmax_plot(fig, 118.5, 3.4, '45\u00B125', 'red', 1.5)
fig.text(x=120.4, y=4.2, text="Self-made Calculator", font="15p,black", fill='white')
fig.text(x=120.2, y=3.4, text="Lund's Calculator", font="15p,black", fill='white')

fig.show()


pygmt.makecpt(
    cmap="#1f3d82,#8fc6ff",
    series="-7500/0",
    continuous=True,
    output="/mnt/d/celebes-stress-inversion-project/test/test-perhitungan-shmax-code-lund/sea.cpt"
)

pygmt.makecpt(
    cmap="#a6e3a1,#c8a27a",
    series="0/3500",
    continuous=True,
    output="/mnt/d/celebes-stress-inversion-project/test/test-perhitungan-shmax-code-lund/land.cpt"
)
with open("/mnt/d/celebes-stress-inversion-project/test/test-perhitungan-shmax-code-lund/softearth.cpt","w") as out:
    out.write(open("/mnt/d/celebes-stress-inversion-project/test/test-perhitungan-shmax-code-lund/sea.cpt").read())
    out.write(open("/mnt/d/celebes-stress-inversion-project/test/test-perhitungan-shmax-code-lund/land.cpt").read())