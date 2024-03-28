#!/home/haidir/celebes-stress-inversion-project/venv/bin/python3

import numpy as np
import pandas as pd

#Memasukkan tabel input
dat1 = pd.read_csv("/mnt/d/celebes-stress-inversion-project/data/clean/DataPakFawzy.csv")
dat2 = pd.read_csv("/mnt/d/celebes-stress-inversion-project/data/clean/Globalcmt.csv")
dat3 = pd.read_csv("/mnt/d/celebes-stress-inversion-project/data/clean/isc-gem-cat.csv")

#Menggabungkan data input
raw = pd.concat([dat1, dat2, dat3])
raw = raw.sort_values(by=['date', 'time'])
raw = raw.reset_index()
raw = raw.drop(['index'],axis=1)
des_raw = raw.describe()
sum_raw = des_raw.iloc[0,1]

#Membuat yang baru
new = pd.DataFrame(raw.loc[0])
new = new.T
drop = pd.DataFrame(raw.loc[0])
drop = drop.T

for i in range (1, int(sum_raw)):
    a1 = raw.iloc[i, 0]
    b1 = raw.iloc[i, 1]
    c1 = pd.Timestamp(a1+" "+b1).timestamp()
    a2 = raw.iloc[i-1, 0]
    b2 = raw.iloc[i-1, 1]
    c2 = pd.Timestamp(a2+" "+b2).timestamp()
    d = c1 - c2
    if d > 300:
        tem = pd.DataFrame(raw.loc[i])
        tem = tem.T
        new = pd.concat([new, tem])
    elif abs(float(raw.iloc[i, 2])-float(raw.iloc[i-1, 2])) > 0.5:
        tem = pd.DataFrame(raw.loc[i])
        tem = tem.T
        new = pd.concat([new, tem])
    elif abs(float(raw.iloc[i, 3])-float(raw.iloc[i-1, 3])) > 0.5:
        tem = pd.DataFrame(raw.loc[i])
        tem = tem.T
        new = pd.concat([new, tem])
    elif abs(float(raw.iloc[i, 5])-float(raw.iloc[i-1, 5])) > 0.3:
        tem = pd.DataFrame(raw.loc[i])
        tem = tem.T
        new = pd.concat([new, tem])
    else:
        tem = pd.DataFrame(raw.loc[i])
        tem = tem.T
        drop = pd.concat([drop, tem])

new.to_csv("/mnt/d/celebes-stress-inversion-project/data/siap-olah/data-gabungan.csv", index=False)
drop.to_csv("/mnt/d/celebes-stress-inversion-project/data/siap-olah/data-kembar.csv", index=False)