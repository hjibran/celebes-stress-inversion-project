#!/home/haidir/celebes-stress-inversion-project/venv/bin/python3
"""
Program ini dibuat untuk menampilkan hasil dbscan sesuai
dengan yang disajikan pada bab metode penelitian. yaitu
dengan menggunakan 30 pasangan parameter dan menyajikan
peta sebaran klaster terhadap struktur geologi, pt-axis 
dan ternary diagram
"""

import pandas as pd
from sklearn.cluster import DBSCAN
import numpy as np
import os
import sys
import re
import pygmt
from shapely.geometry import Point, MultiPoint
from shapely.ops import unary_union

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
  plt.savefig('/mnt/d/celebes-stress-inversion-project/Result/DBSCAN/minpts{}eps{}/stressinverse{}.png'.format(min,eps,kelas+1))
   
data = pd.read_csv("/mnt/d/celebes-stress-inversion-project/data/siap-olah/fm50km7mw.csv")

Min = [10,15,20]
Eps = [0.05,
       0.10,
       0.15,
       0.20,
       0.25,
       0.30,
       0.35,
       0.40,
       0.45,
       0.50]

for min in Min: #range(10,20+1,5):
   for eps in Eps: #np.arange(0.05, 0.50+0.01, 0.05):

    print('minpts{}eps{} mulai'.format(min,eps))
    os.system('mkdir /mnt/d/celebes-stress-inversion-project/Result/DBSCAN/minpts{}eps{}'.format(min,eps))

    x = data.iloc[:, [3, 2]]
    clustering = DBSCAN(eps=eps, min_samples=min).fit(x)
    data["cluster"] = clustering.labels_
    banyak_cluster = data["cluster"].max()

    core_point_per_klaster = []
    for kelas in range(0,banyak_cluster+1):
        temp_data = data.query('cluster == {}'.format(kelas))
        temp_data = temp_data.reset_index()

        x = temp_data['lon'].tolist()
        y = temp_data['lat'].tolist()    
        ind = [0 for i in range(0,len(x))]

        # mendefenisikan CorePoint
        for i in range(0,len(ind)):
          tes_noise = []
          for t in range (len(data['lon'])): #(0,len(ind)): #
            tes = ((x[i]-data['lon'][t])**2+(y[i]-data['lat'][t])**2)**(1/2) # ((x[i]-x[t])**2+(y[i]-y[t])**2)**(1/2) 
            if tes < float(eps):
              tes_noise.append(t)
          a = len(tes_noise)
          if a >= min:
            ind[i] = "c"

        temp_data['corepoint'] = ind

        dat = temp_data.query('corepoint != 0')
        #if len(core_point_per_klaster) > 0:
        core_point_per_klaster.append(dat)
        print('    core point {} selesai'.format(kelas))
        print(len(dat))

    fig = pygmt.Figure()
    print('  mulai membuat peta sebaran')

    grid = pygmt.datasets.load_earth_relief(
       resolution="30s", # resolution of earth relief
       region=[data['lon'].min()-0.5, data['lon'].max()-0.5, data['lat'].min()-0.5, data['lat'].max()+0.5], # boarder of map: [minlon, maxlon, minlat, maxlat],
       registration="gridline"
       )
    # plot grid image
    fig.grdimage(
       grid=grid, # call grid
       frame=["a", "EWSN"],#, "+tPulau Sulawesi"],
       projection="M20c",
       cmap= "/mnt/d/celebes-stress-inversion-project/generic-mapping-tools/script/color.cpt",
       #shading = True
    )
    fig.coast(
      water = 'white',
      shorelines = '1.5p,dimgray'
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
    struktur(1, 'gray19')

    fig.plot(
      x = data['lon'],
      y = data['lat'],
      style = 'c0.15c',
      #fill = 'yellow',
      pen = 'black',
      label = 'Epicenter'
    )

    for i in range(len(core_point_per_klaster)):
      data_temp = core_point_per_klaster[i]

      fig.text(
         x = (float(data_temp['lon'].min())+float(data_temp['lon'].max()))/2, # float(data_temp['lon'].min())-0.1, #
         y = (float(data_temp['lat'].min())+float(data_temp['lat'].max()))/2, # float(data_temp['lat'].max()), #
         text = str(i+1),
         font = "20p,Helvetica-Bold,black",
         fill = 'white'
      )

      # Buat buffer menggunakan Shapely
      points = [Point(x, y) for x, y in zip(data_temp['lon'], data_temp['lat'])]
      buffers = [point.buffer(eps) for point in points]  # buffer 0.1 derajat

      # Gabungkan semua buffer menjadi satu polygon
      merged_buffer = unary_union(buffers)

      # Ekstrak koordinat untuk plotting
      if hasattr(merged_buffer, 'exterior'):
          # Single polygon
          x_buf, y_buf = merged_buffer.exterior.coords.xy
      else:
          # Multiple polygons
          x_buf, y_buf = [], []
          for geom in merged_buffer.geoms:
              x, y = geom.exterior.coords.xy
              x_buf.extend(x)
              y_buf.extend(y)

      # Plot buffer polygon
      fig.plot(
         x=x_buf, 
         y=y_buf, 
         pen="2.5p,black", 
         label='Cluster Boundary'
      )

    #fig.show()
    fig.savefig('/mnt/d/celebes-stress-inversion-project/Result/DBSCAN/minpts{}eps{}/peta.png'.format(min,eps))
    print('    peta sebaran tersimpan')

    print('  memulai pembuatan ternery diagram dan ptaxis')
    banyak_cluster = data["cluster"].max()
    for kelas in range(0, banyak_cluster+1):
      hasil = data[data["cluster"]==kelas]

      to_ternery = hasil.iloc[:, [3, 2, 4, 6, 7, 8, 5]]
      to_ternery = to_ternery.reset_index()

      index = list(to_ternery.index.values)
      fl = '/mnt/d/celebes-stress-inversion-project/Result/DBSCAN/minpts{}eps{}/ternery{}.dat'.format(min,eps,kelas+1)
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
                                                                       i
              )
              dat.write(isi)
              i += 1
      os.system("python3 /mnt/d/celebes-stress-inversion-project/FMC-master/FMC.py -p " +
                "'/mnt/d/celebes-stress-inversion-project/Result/DBSCAN/minpts{}eps{}/ternery{}.png' ".format(min,eps,kelas+1) +
                fl +
                ' -pc fclvd -i AR > ' +
                '/mnt/d/celebes-stress-inversion-project/Result/DBSCAN/minpts{}eps{}/terneryresult{}.dat'.format(min,eps,kelas+1) 
      )
      print('    ternery{} tersimpan'.format(kelas+1))

      to_stress_inversion = hasil.iloc[:, [6, 7, 8]] # take strike, dip, and rake value
      to_stress_inversion = to_stress_inversion.reset_index() 
      index = list(to_stress_inversion.index.values)

      # create and fill files 
      with open('/mnt/d/celebes-stress-inversion-project/Result/DBSCAN/minpts{}eps{}/stressinverse{}.dat'.format(min,eps,kelas+1), "w") as dat:
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

      # add Programs_PYTHON to path (to access the functions within it)
      strinv_dir = '/mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Programs_PYTHON'
      if not strinv_dir in sys.path:
          sys.path.append(strinv_dir)

      # uses a previously created file as input
      input_file = '/mnt/d/celebes-stress-inversion-project/Result/DBSCAN/minpts{}eps{}/stressinverse{}.dat'.format(min,eps,kelas+1)
      # run stress inverse

      import read_mechanism as rm
      str1,dip1,rak1,str2,dip2,rak2 = rm.read_mechanisms(input_file)

      import stress_inversion as si
      tau_optimum,shape_ratio,strike,dip,rake,instability,friction,sigma = si.stress_inversion(
          str1,dip1,rak1,str2,dip2,rak2,0.00,1.00,0.05,6,10)

      # plot P/T axis
      plot_stress(strike,dip,rake,kelas)
      print('    ptaxis{} tersimpan'.format(kelas+1))   