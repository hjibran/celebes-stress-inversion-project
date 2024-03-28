#!/home/haidir/celebes-stress-inversion-project/venv/bin/python3
import pandas as pd
from sklearn.cluster import DBSCAN
import numpy as np
import os
import sys
import re
import pygmt

data = pd.read_csv("/mnt/d/celebes-stress-inversion-project/data/siap-olah/fm50km7mw.csv") #data-tanpa-laut-maluku.csv")
eps = float(sys.argv[1]) #float(input("Masukkan nilai epsilon(dalam desimal): ")) #
min = int(sys.argv[2]) #int(input("Masukkan nilai minimal event: ")) #
dir = ("/mnt/d/celebes-stress-inversion-project/Result/eps{}min{}".format(eps, min))
os.mkdir(dir)
os.mkdir(dir+"/clustered")
os.mkdir(dir+"/ternary-diagram")
os.mkdir(dir+"/stressinverse")
os.mkdir(dir+"/stressinverse/data")
os.mkdir(dir+"/stressinverse/Output")
os.mkdir(dir+"/stressinverse/Output/output")
os.mkdir(dir+"/stressinverse/Output/principal_mechanisms")
os.mkdir(dir+"/stressinverse/Figure")
os.mkdir(dir+"/stressinverse/Figure/shape_ratio")
os.mkdir(dir+"/stressinverse/Figure/stress_directions")
os.mkdir(dir+"/stressinverse/Figure/P_T_axes")
os.mkdir(dir+"/stressinverse/Figure/Mohr_circles")
os.mkdir(dir+"/stressinverse/Figure/fault")

x = data.iloc[:, [3, 2]]
clustering = DBSCAN(eps=eps, min_samples=min).fit(x)
data["cluster"] = clustering.labels_

fig = pygmt.Figure()
fig.basemap(region=[117.5, 127.5, -8.5, 5.5],
            frame=["a", "+teps{}min{}".format(eps, min)],
            projection="M20c"
)
fig.coast(shorelines='1p'
)
fig.plot(
    data="/mnt/d/celebes-stress-inversion-project/data/batas-lempeng-dan-patahan/indonesiafaults.gmt",
    pen="0.85p"
)
fig.plot(
    data="/mnt/d/celebes-stress-inversion-project/data/batas-lempeng-dan-patahan/trench.gmt",
    pen="1p",
    style="f1c/0.2c+l+t",
    fill="black"
)
color = ['gray', 'navy', 'dodgerblue', 'deepskyblue', 'darkslategray',
         'darkgreen', 'red', 'chocolate', 'yellow', 'green',
         'darkbrown', 'orangered', 'black', 'magenta', 'gold4',
         'yellow4', 'chartreuse1', 'lightskyblue4', 'olivedrab1', 'springgreen4',
         'khaki1', 'khaki4', 'purple', 'cyan', 'firebrick2',
         'navy', 'dodgerblue', 'deepskyblue', 'darkslategray',
         'darkgreen', 'red', 'chocolate', 'yellow', 'green',
         'darkbrown', 'orangered', 'black', 'magenta', 'gold4',
         'yellow4', 'chartreuse1', 'lightskyblue4', 'olivedrab1', 'springgreen4',
         'khaki1', 'khaki4', 'purple', 'cyan', 'firebrick2',
         'navy', 'dodgerblue', 'deepskyblue', 'darkslategray',
         'darkgreen', 'red', 'chocolate', 'yellow', 'green',
         'darkbrown', 'orangered', 'black', 'magenta', 'gold4',
         'yellow4', 'chartreuse1', 'lightskyblue4', 'olivedrab1', 'springgreen4',
         'khaki1', 'khaki4', 'purple', 'cyan', 'firebrick2',
         'navy', 'dodgerblue', 'deepskyblue', 'darkslategray',
         'darkgreen', 'red', 'chocolate', 'yellow', 'green',
         'darkbrown', 'orangered', 'black', 'magenta', 'gold4',
         'yellow4', 'chartreuse1', 'lightskyblue4', 'olivedrab1', 'springgreen4',
         'khaki1', 'khaki4', 'purple', 'cyan', 'firebrick2',
         'navy', 'dodgerblue', 'deepskyblue', 'darkslategray',
         'darkgreen', 'red', 'chocolate', 'yellow', 'green',
         'darkbrown', 'orangered', 'black', 'magenta', 'gold4',
         'yellow4', 'chartreuse1', 'lightskyblue4', 'olivedrab1', 'springgreen4',
         'khaki1', 'khaki4', 'purple', 'cyan', 'firebrick2'
]


file = []
c = 0
proses = 0
banyak_cluster = data["cluster"].max()
for kelas in range(-1, banyak_cluster+1):
    hasil = data[data["cluster"]==kelas]

    FM = hasil.iloc[:, [3, 2, 4, 6, 7, 8, 5]]
    FM.columns = ["longitude", "latitude", "depth", "strike", "dip", "rake", "magnitude"]
    fig.meca(
        spec=FM,
        compressionfill=color[c],
        scale="0.2c",
        extensionfill="white"
    )
    c += 1
    print(proses)
    proses += 1

    to_stress_inversion = hasil.iloc[:, [6, 7, 8]]
    to_stress_inversion = to_stress_inversion.reset_index()
    index = list(to_stress_inversion.index.values)
    hasil.to_csv(dir+"/clustered/cls{}.csv".format(kelas), 
                 index=False)
    with open(dir+"/stressinverse/data/cls{}.dat".format(kelas), "w") as dat:
        dat.write("% ini datanya\n")
        dat.write("%  stike   dip   rake\n")
        i = 0
        while i in index:
            isi = "   {}   {}   {}\n".format(to_stress_inversion.iloc[i, 1],
                                             to_stress_inversion.iloc[i, 2],
                                             to_stress_inversion.iloc[i, 3])
            dat.write(isi)
            i += 1
    os.system("python3 /mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Programs_PYTHON/StressInverse.py "+ 
              dir +"/stressinverse/data/cls{}.dat ".format(kelas) + 
              "{} {} {} {}".format(eps, min, kelas, dir))

    print(proses)
    proses += 1

    to_ternery = hasil.iloc[:, [3, 2, 4, 6, 7, 8, 5]]
    to_ternery = to_ternery.reset_index()
    index = list(to_ternery.index.values)
    fl = dir+"/ternary-diagram/cls{}.dat".format(kelas)
    with open(fl, "w") as dat:
        i = 0
        while i in index:
            isi = "{}   {}  {}  {}  {}  {}  {}  X   Y   {}\n".format(to_ternery.iloc[i, 1],
                                                                     to_ternery.iloc[i, 2],
                                                                     to_ternery.iloc[i, 3],
                                                                     to_ternery.iloc[i, 4],
                                                                     to_ternery.iloc[i, 5],
                                                                     to_ternery.iloc[i, 6],
                                                                     to_ternery.iloc[i, 7],
                                                                     i)
            dat.write(isi)
            i += 1
    os.system("python3 /mnt/d/celebes-stress-inversion-project/FMC-master/FMC.py -p "+
              "'{}/ternary-diagram/cls{}.png' ".format(dir, kelas)+
              fl+
              " -pc fclvd -i AR > /mnt/d/celebes-stress-inversion-project/FMC-master/output.dat")
    print(proses)
    proses += 1

fig.savefig(dir+"/clustered/sebaran.jpg")