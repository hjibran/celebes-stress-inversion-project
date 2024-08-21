import numpy as np
import matplotlib.pyplot as plt
import random
import pandas as pd
eps = '0.35'
min = 15
banyak_kelompok = 9

for kelas in range(0, banyak_kelompok+1):
  data = pd.read_csv("/mnt/d/celebes-stress-inversion-project/Result/eps{}min{}/clustered/cls{}.csv".format(eps, min, kelas))

  x = data.lon
  y = data.lat
  ind = [0 for i in range(0,len(x))]

  #mendefenisikan CorePoint
  for i in range(0,len(ind)):
    tes_noise = []
    for t in range (0,len(ind)):
      tes = ((x[i]-x[t])**2+(y[i]-y[t])**2)**(1/2)
      if tes <= float(eps):
        tes_noise.append(t)
    a = len(tes_noise)
    if a >= min:
      ind[i] = "c"

  data['corepoint'] = ind

  dat = data.query('corepoint != 0')

  dat.to_csv("/mnt/d/celebes-stress-inversion-project/Result/eps{}min{}/clustered/corepoint{}.csv".format(eps, min, kelas), index=False)