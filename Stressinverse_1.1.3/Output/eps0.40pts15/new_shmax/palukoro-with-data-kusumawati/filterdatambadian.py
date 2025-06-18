import pandas as pd
import numpy as np
import pytz

## mengeneralkan format
def atur_format_dian():
    ## menyamakan format data semperti dengan data clean yang lain
    ## luaran berupa dua file, yang pertama mengandung semua data, dan yang kedua mengandung data dengan kualitas A dan B saja
    ## luaran hanya mengandung data dengan kedalaman <= 50 dan magnitude <= 7.0
    ## perlu dilakukan cutting data menggunakan qgis, untuk mengambil data dalam batas cluster palu

    data = pd.read_csv('/mnt/d/celebes-stress-inversion-project/data/clean/Katalog_mekanisme_fokus_SPM_PEPI_Kusumawati_et_al_2024_rapih.csv')
    
    clean = np.zeros([len(data),1])

    data_clean = data.iloc[:, [2,3,4,5,6,7,11,12,13,14,15,16,21]]
    data_clean.columns = ['date','time','lat','lon','depth','mw','str1','dip1','rake1','str2','dip2','rake2','fac']
    data_clean.insert(12, 'mo', clean)
    data_clean.insert(14, 'mpp', clean)
    data_clean.insert(15, 'mpr', clean)
    data_clean.insert(16, 'mrr', clean)
    data_clean.insert(17, 'mrt', clean)
    data_clean.insert(18, 'mtp', clean)
    data_clean.insert(19, 'mtt', clean)

    data_clean = data_clean.query('depth <= 50')
    data_clean = data_clean.query('mw <= 7')

    A_B = data_clean[data_clean['fac'].isin(['A', 'B'])]

    #data_clean.to_csv("/mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Output/eps0.40pts15/new_shmax/palukoro-with-data-kusumawati/datawithkusumawati(A-D).csv", index=False)
    #_B.to_csv("/mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Output/eps0.40pts15/new_shmax/palukoro-with-data-kusumawati/datawithkusumawati(A-B).csv", index=False)

## Mengurutkan sesuai dengan waktu dan tahun
def urut_dian():
    data = pd.read_csv('/mnt/d/celebes-stress-inversion-project/data/clean/Katalog_mekanisme_fokus_palu_Kusumawati_et_al_2024.csv')

    data['datetime'] = data['date'] + ' ' + data['time']

    # Konversi ke datetime
    data['datetime'] = pd.to_datetime(data['datetime'], format='%d-%m-%Y %H:%M:%S.%f')

    # Urutkan berdasarkan datetime
    data = data.sort_values('datetime')

    data_new = data.drop('datetime',axis=1)

    print(data_new)
    #data_new.to_csv("/mnt/d/celebes-stress-inversion-project/data/clean/Katalog_mekanisme_fokus_palu_Kusumawati_et_al_2024.csv", index=False)

def memperbaiki_data_gabungan():
    # memasukkan data-gabungan.csv
    data = pd.read_csv('/mnt/d/celebes-stress-inversion-project/data/siap-olah/data-gabungan.csv')

    # menghapus data yang tidak memiliki focal mechanism
    data = data.query('0 <= str1 < 360')
    data = data.query('depth <= 50')
    data = data.query('mw <= 7')

    # cek data
    print(data)
    #data.to_csv("/mnt/d/tes.csv", index=False)

## menggabungkan data 
def gabung_data():
    dian = pd.read_csv('/mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Output/eps0.40pts15/new_shmax/palukoro-with-data-kusumawati/datakusumawatipalu.csv')
    dian['datetime'] = dian['date'] + ' ' + dian['time']
    dian['datetime'] = pd.to_datetime(dian['datetime'], format='%Y-%m-%d %H:%M:%S.%f')
    '''
    wita = pytz.timezone('Asia/Makassar')  # WITA - Waktu Indonesia Tengah
        # Set timezone asal (WITA/UTC+8)
    dian['datetime'] = dian['datetime'].dt.tz_localize(wita)
    # Konversi ke UTC
    dian['datetime'] = dian['datetime'].dt.tz_convert('UTC')
    # Hapus timezone info jika tidak diperlukan
    dian['datetime'] = dian['datetime'].dt.tz_localize(None)
    '''
    palu = pd.read_csv('/mnt/d/celebes-stress-inversion-project/Result/eps0.40min15-final/clustered/cluster7epsilon40.csv')
    palu['datetime'] = palu['date'] + ' ' + palu['time']
    palu['datetime'] = pd.to_datetime(palu['datetime'], format='%Y-%m-%d %H:%M:%S.%f')

    gabung = pd.concat([dian, palu])

    
    raw = gabung.sort_values(by=['datetime'])
    raw = raw.reset_index()
    raw = raw.drop(['index'],axis=1)
    des_raw = raw.describe()
    sum_raw = des_raw.iloc[0,1]
    raw['time_diff'] = raw['datetime'].diff()
    raw['time_diff_seconds'] = raw['time_diff'].dt.total_seconds()

    #Membuat yang baru
    new = pd.DataFrame(raw.loc[0])
    new = new.T
    drop = pd.DataFrame(raw.loc[0])
    drop = drop.T

    for i in range (1, int(sum_raw)):
        if raw['time_diff_seconds'][i] > 300:
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
    
    print(drop)
    raw = raw.drop('datetime',axis=1)
    raw = raw.drop('time_diff',axis=1)
    raw = raw.drop('time_diff_seconds',axis=1)
    #raw.to_csv('/mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Output/eps0.40pts15/new_shmax/palukoro-with-data-kusumawati/datawithkusumawati.csv')
    return raw, drop

def pisah_before_after():
    data = pd.read_csv('/mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Output/eps0.40pts15/new_shmax/palukoro-with-data-kusumawati/datawithkusumawati(A-B).csv')
    data['datetime'] = data['date'] + ' ' + data['time']
    data['datetime'] = pd.to_datetime(data['datetime'], format='%Y-%m-%d %H:%M:%S.%f')
    palu2018 =  pd.to_datetime('2018-09-28 10:02:59')
    before = data[data['datetime'] < palu2018]
    after = data[data['datetime'] > palu2018]

    before.to_csv('/mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Output/eps0.40pts15/new_shmax/palukoro-with-data-kusumawati/datawithkusumawati(A-B)before.csv', index=False)
    after.to_csv('/mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Output/eps0.40pts15/new_shmax/palukoro-with-data-kusumawati/datawithkusumawati(A-B)after.csv', index=False)

def persiapan_data_inversi_stress():
    before = pd.read_csv('/mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Output/eps0.40pts15/new_shmax/palukoro-with-data-kusumawati/datawithkusumawati(A-D)before.csv')
    after = pd.read_csv('/mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Output/eps0.40pts15/new_shmax/palukoro-with-data-kusumawati/datawithkusumawati(A-D)after.csv')

    before_to_inverse = before.iloc[:, [6, 7, 8]]
    after_to_inverse = after.iloc[:, [6, 7, 8]]

    before_to_inverse.to_csv('/mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Output/eps0.40pts15/new_shmax/palukoro-with-data-kusumawati/datawithkusumawati(A-D)beforetoinverse.dat', index=False)
    after_to_inverse.to_csv('/mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Output/eps0.40pts15/new_shmax/palukoro-with-data-kusumawati/datawithkusumawati(A-D)aftertoinverse.dat', index=False)

persiapan_data_inversi_stress()