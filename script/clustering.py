# ----------------------------------------------------------------#
# this code was created to determine the seed value that          # 
# will be used in each cluster                                    #
# the best seed is the seed with  mean standar deviation          #
# ----------------------------------------------------------------#
import pandas as pd
import numpy as np
import re

# ========================================================================================
# ------------------------------------------------
# input parameter
# ------------------------------------------------
import sys
import os

data = pd.read_csv("/mnt/d/celebes-stress-inversion-project/data/siap-olah/fm50km7mw.csv")
eps = 0.5 #float(sys.argv[1]) #float(input("Masukkan nilai epsilon(dalam desimal): ")) #
min = 15 #int(sys.argv[2]) #int(input("Masukkan nilai minimal event: ")) #
dir = ("/mnt/d/celebes-stress-inversion-project/Result/eps{}min{}".format(eps, min))

# ------------------------------------------------
# additional option
# ------------------------------------------------
# clustering
save_cluster_csv = True
plot = False; save_fig = False
fig_name = "sebaran.png"

# ternary diagram
ternary = False

# save_data_to_stress_inverse
save_stress_inverse = False
# P/T axis (can't plot PTaxis without saving to stress inversion data)
PTaxis = False

# make directory
if save_cluster_csv:
    if not os.path.exists(dir):
        os.mkdir(dir)
    if not os.path.exists(dir+"/clustered"):
        os.mkdir(dir+"/clustered")
if plot and save_fig:
    if not os.path.exists(dir):
        os.mkdir(dir)
    if not os.path.exists(dir+"/clustered"):
        os.mkdir(dir+"/clustered")
if ternary:
    if not os.path.exists(dir):
        os.mkdir(dir)
    if not os.path.exists(dir+"/ternary"):
        os.mkdir(dir+"/ternary")
if save_stress_inverse:
    if not os.path.exists(dir):
        os.mkdir(dir)
    if not os.path.exists(dir+"/stressinverse"):
        os.mkdir(dir+"/stressinverse")
if PTaxis:
    if not os.path.exists(dir):
        os.mkdir(dir)
    if not os.path.exists(dir+"/PTaxis"):
        os.mkdir(dir+"/PTaxis")


# ========================================================================================
# ------------------------------------------------
# clustering
# ------------------------------------------------
from sklearn.cluster import DBSCAN

# run DBSCAN
x = data.iloc[:, [3, 2]]
clustering = DBSCAN(eps=eps, min_samples=min).fit(x)
data["cluster"] = clustering.labels_ #add cluster columns to data DataFrame

if save_cluster_csv:
    banyak_cluster = data["cluster"].max()
    for kelas in range(-1, banyak_cluster+1):
        hasil = data[data["cluster"]==kelas]
        hasil.to_csv(dir+"/clustered/cls{}.csv".format(kelas), 
                     index=False)
        

# ========================================================================================
# ------------------------------------------------
# plot cluster
# ------------------------------------------------
import pygmt
import random

# setting basemap
fig = pygmt.Figure()
fig.basemap(region=[117.5, 127.5, -8.5, 5.5], # [minlon, maxlon, minlat, maxlat]
            frame=["a", "+teps{}min{}".format(eps, min)], 
            projection="M20c")

# plot shore lines
fig.coast(shorelines='1p')

# plot fault
fig.plot(data="/mnt/d/celebes-stress-inversion-project/data/batas-lempeng-dan-patahan/indonesiafaults.gmt",
         pen="0.85p")

# plot trench
fig.plot(data="/mnt/d/celebes-stress-inversion-project/data/batas-lempeng-dan-patahan/trench.gmt",
         pen="1p",
         style="f1c/0.2c+l+t",
         fill="black")

# plot noise data from DBSCAN
hasil = data[data["cluster"]==-1]

FM = hasil.iloc[:, [3, 2, 4, 6, 7, 8, 5]]
FM.columns = ["longitude", "latitude", "depth", "strike", "dip", "rake", "magnitude"]

fig.meca(spec=FM,
         compressionfill="gray",
         scale="0.2c",
         extensionfill="white")

# add color option
color = ['navy', 'dodgerblue', 'deepskyblue', 'darkslategray',
         'darkgreen', 'red', 'chocolate', 'yellow', 'green',
         'darkbrown', 'orangered', 'black', 'magenta', 'gold4',
         'yellow4', 'chartreuse1', 'lightskyblue4', 'olivedrab1', 'springgreen4',
         'khaki1', 'khaki4', 'purple', 'cyan', 'firebrick2']

# plotclusters data from DBSCAN
banyak_cluster = data["cluster"].max()
for kelas in range(0, banyak_cluster+1):
    hasil = data[data["cluster"]==kelas]

    FM = hasil.iloc[:, [3, 2, 4, 6, 7, 8, 5]]
    FM.columns = ["longitude", "latitude", "depth", "strike", "dip", "rake", "magnitude"]

    fig.meca(
        spec=FM,
        compressionfill=random.choice(color),
        scale="0.2c",
        extensionfill="white")

# plot/save_fig
if plot:
    if save_fig:
        fig.savefig(dir+"/clustered/"+fig_name)
    else:
        fig.show()


# ========================================================================================
# ------------------------------------------------
# ternary diagram
# ------------------------------------------------
if ternary:
    banyak_cluster = data["cluster"].max()
    for kelas in range(0, banyak_cluster+1):
        hasil = data[data["cluster"]==kelas]

        to_ternery = hasil.iloc[:, [3, 2, 4, 6, 7, 8, 5]]
        to_ternery = to_ternery.reset_index()
        index = list(to_ternery.index.values)
        fl = dir+"/ternary/cls{}.dat".format(kelas)
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
                  "'{}/ternary/cls{}.png' ".format(dir, kelas)+
                  fl+
                  " -pc fclvd -i AR")


# ========================================================================================
# ------------------------------------------------
# save data to stress inverse and plot P/T axis
# ------------------------------------------------
if save_stress_inverse:

    if PTaxis: # make function to plot PT axis      
        def plot_stress(strike,dip,rake,kelas):
            import plot_stress as ps
            import matplotlib.pyplot as plt
            import numpy as np
            # plotting the stress directions in the focal sphere
            fig, ax = plt.subplots()
            ax.set_title('Principal stress and P/T axes',fontsize = 16)
            ax.axis('equal')
            ax.axis([-1.05,  1.70, -1.05, 1.05])
            ax.axis('off')
            #ax.axis()        
            # P/T axes
            ps.plot_P_T_axes(strike,dip,rake)
            # boundary circle and the centre of the circle
            fi = np.arange(0,360, 0.1)
            plt.plot(np.cos(fi*np.pi/180.),np.sin(fi*np.pi/180.),'k-', linewidth = 2.0)
            plt.plot(0,0,'k+', markersize = 10);        
            # legend
            #plt.legend((sig1,sig2,sig3), ('sigma 1','sigma 2','sigma 3'), loc='lower right', fontsize = 14, numpoints=1)
            plt.legend(('sigma 1','sigma 2'), loc='lower right', fontsize = 14, numpoints=1)
            plt.savefig(dir+"/PTaxis/cls{}.png".format(kelas))

    # ------------------------------------------------
    # save data to stress inverse
    banyak_cluster = data["cluster"].max()
    for kelas in range(0, banyak_cluster+1): # repeat in each cluster
        hasil = data[data["cluster"]==kelas] # quarry cluster

        to_stress_inversion = hasil.iloc[:, [6, 7, 8]] # take strike, dip, and rake value
        to_stress_inversion = to_stress_inversion.reset_index() 
        index = list(to_stress_inversion.index.values)

        # create and fill files 
        with open(dir+"/stressinverse/cls{}.dat".format(kelas), "w") as dat:
            dat.write("% ini datanya\n")
            dat.write("%  stike   dip   rake\n")
            i = 0
            while i in index:
                isi = "   {}   {}   {}\n".format(to_stress_inversion.iloc[i, 1],
                                                 to_stress_inversion.iloc[i, 2],
                                                 to_stress_inversion.iloc[i, 3])
                dat.write(isi)
                i += 1
            dat.close()

            # ------------------------------------------------
            # plot PT axis
            if PTaxis:
                # add Programs_PYTHON to path (to access the functions within it)
                strinv_dir = '/mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Programs_PYTHON'
                if not strinv_dir in sys.path:
                    sys.path.append(strinv_dir)
                
                # uses a previously created file as input
                input_file = dir+"/stressinverse/cls{}.dat".format(kelas)

                # run stress inverse
                import read_mechanism as rm
                str1,dip1,rak1,str2,dip2,rak2 = rm.read_mechanisms(input_file)
                import stress_inversion as si
                tau_optimum,shape_ratio,strike,dip,rake,instability,friction = si.stress_inversion(
                    str1,dip1,rak1,str2,dip2,rak2,0.40,1.00,0.05,6,10)
                
                # plot P/T axis
                plot_stress(strike,dip,rake,kelas)