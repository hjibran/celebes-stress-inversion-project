#!/home/haidir/celebes-stress-inversion-project/venv/bin/python3
import numpy as np
import pandas as pd

data = pd.read_csv("/mnt/d/celebes-stress-inversion-project/data/siap-olah/data-tanpa-laut-maluku.csv")

x = data.lon
y = data.lat

jarak_minimum_tiap_titik = []
for titik in range(0, len(x)):
  jarak_antar_titik = []
  for titik_lain in range (0, len(x)):
    jarak = (abs( x[titik] - x[titik_lain] )**2 + abs( y[titik] - y[titik_lain] )**2)**0.5
    if jarak != 0:
      jarak_antar_titik.append(jarak)
  jarak_minimum_tiap_titik.append(min(jarak_antar_titik))
print(sum(jarak_minimum_tiap_titik)/len(jarak_minimum_tiap_titik))
