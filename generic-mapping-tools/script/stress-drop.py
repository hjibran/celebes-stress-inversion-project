#!/home/haidir/celebes-stress-inversion-project/venv/bin/python3

#---------------------------------------------------------------------#
# Import module
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pygmt
import statistics as sts
fig = pygmt.Figure()

#---------------------------------------------------------------------#
# Mendefenisikan Fungsi

## Persamaan untuk menghitung delta theta
def delta_theta(stress_drop, theta):

    # Konversi drajat ke radian
    st = stress_drop
    t = np.deg2rad(theta)

    # Persamaan untuk menghitung delta theta
    dt = np.rad2deg(np.arctan(((1)-(st*np.sin(2*t))-np.sqrt((st**2)+(1)-(2*st*np.sin(2*t))))/(st*np.cos(2*t))))

    return dt

## Persamaan untuk menghitung nilai stress drop
def stress_drop(t, dt):

    # Input: theta (t) dan delta theta (dt)
    st = -np.sin(2*np.deg2rad(dt))/np.cos((2*np.deg2rad(t))+(2*np.deg2rad(dt)))

    return st

## Fungsi Menghitung nilai theta dan delta theta
### Fungsi pada patahan dengan arah gerak horizontal (Strike-Slip)
def theta_strike(geometry_fault, before, after):

    theta_before    = geometry_fault    - before
    theta_after     = geometry_fault    - after
    delta_theta     = theta_after       - theta_before
    
    # Mengembalikan nilai theta dan delta theta
    return theta_before, delta_theta

### Fungsi pada patahan dengan arah gerak vertikal (Subduksi)
def theta_dip(geometry_fault, before, after):

    theta_before    = geometry_fault    + before
    theta_after     = geometry_fault    + after
    delta_theta     = theta_after       - theta_before

    # Mengembalikan nilai theta dan delta theta
    return theta_before, delta_theta

## Plot histogram sebaran data
def histo(title, data, bin = 50):
    
    pltHist, axH = plt.subplots()
    n, bins, patches = axH.hist(x = data, bins = bin, color='#0504aa', alpha = 0.7, rwidth=0.85)
    axH.set_title(title, fontsize = 14)
    axH.grid(True)
    #plt.xlim(0,1)
    plt.show()
    plt.close()

## Menghitung Sebaran theta & delta thetha
def sebaran_theta(nama, before, after):

    # Membuat lokasi penyimpanan sebaran data hasil kalkulasi
    sebaran_theta       = np.zeros(250)
    sebaran_delta_theta = np.zeros(250)
    sebaran_stress_drop = np.zeros(250)

    for i in range(250):

        # Menghitung theta & delta theta
        if nama == 'plunge':
            theta, delta_theta_ = theta_dip(dip, before[i], after[i]) 
        elif nama == 'azimuth' or 'shmax':
            theta, delta_theta_ = theta_strike(strike, before[i], after[i]) 

        # Menghitung stress drop
        stress_drop_ = stress_drop(theta, delta_theta_)

        # Memasukkan nilai kedalam lokasi penyimpanan yang telah dibuat sebelumnya
        sebaran_theta[i]       = theta
        sebaran_delta_theta[i] = delta_theta_
        sebaran_stress_drop[i] = stress_drop_

    bootstrap = pd.DataFrame(data={'theta':sebaran_theta, 'delta theta':sebaran_delta_theta, 'stress drop':sebaran_stress_drop})

    histo('Sebaran Nilai Theta', sebaran_theta)
    histo('Sebaran Nilai Delta Theta', sebaran_delta_theta)
    histo('Sebaran Nilai Stress Drop', sebaran_stress_drop)

    result = np.zeros((4,3))

    result[0][0] = np.float64(np.percentile(sebaran_theta, 97.5))
    result[1][0] = np.float64(np.percentile(sebaran_theta, 2.5))
    result[2][0] = np.float64((np.percentile(sebaran_theta, 97.5)+np.percentile(sebaran_theta, 2.5))/2)
    result[3][0] = np.float64((np.percentile(sebaran_theta, 97.5)-np.percentile(sebaran_theta, 2.5))/2)

    result[0][1] = np.float64(np.percentile(sebaran_delta_theta, 97.5))
    result[1][1] = np.float64(np.percentile(sebaran_delta_theta, 2.5))
    result[2][1] = np.float64((np.percentile(sebaran_delta_theta, 97.5)+np.percentile(sebaran_delta_theta, 2.5))/2)
    result[3][1] = np.float64((np.percentile(sebaran_delta_theta, 97.5)-np.percentile(sebaran_delta_theta, 2.5))/2)
    
    result[0][2] = np.float64(np.percentile(sebaran_stress_drop, 97.5))
    result[1][2] = np.float64(np.percentile(sebaran_stress_drop, 2.5))
    result[2][2] = np.float64((np.percentile(sebaran_stress_drop, 97.5)+np.percentile(sebaran_stress_drop, 2.5))/2)
    result[3][2] = np.float64((np.percentile(sebaran_stress_drop, 97.5)-np.percentile(sebaran_stress_drop, 2.5))/2)

    tabel = pd.DataFrame(result, columns=['theta','delta theta','stress drop'])

    return tabel, bootstrap


#---------------------------------------------------------------------#
# Import Data
data_before = pd.read_csv('/mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Output/eps0.40pts15/new_shmax/palu_before_2018/output_bootstarap.csv')
data_after  = pd.read_csv('/mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Output/eps0.40pts15/new_shmax/palu_after_2018/output_bootstarap.csv')
sebaran_nilai_azimuth_before    = data_before['azimuth sigma 1']
sebaran_nilai_azimuth_before[sebaran_nilai_azimuth_before > sts.mode(sebaran_nilai_azimuth_before)-180+90] -= 180
sebaran_nilai_azimuth_after     = data_after['azimuth sigma 1']
sebaran_nilai_azimuth_after[sebaran_nilai_azimuth_after > sts.mode(sebaran_nilai_azimuth_after)+90] -= 180
sebaran_nilai_plunge_before     = data_before['plunge sigma 1']
sebaran_nilai_plunge_after      = data_after['plunge sigma 1']
sebaran_nilai_shmax_before      = data_before['SHmax']
sebaran_nilai_shmax_before[sebaran_nilai_shmax_before > sts.mode(sebaran_nilai_shmax_before)-180+90] -= 180
sebaran_nilai_shmax_after       = data_after['SHmax']
sebaran_nilai_shmax_after[sebaran_nilai_shmax_after > sts.mode(sebaran_nilai_shmax_after)+90] -= 180


## Geometri patahan Palu 2018 Mw7.5 berdasarkan Focal mechanism global CMT
strike = 168
dip = 57

# Menghitung sebaran theta dan delta theta
hasil, bootstrap = sebaran_theta("shmax", sebaran_nilai_shmax_before, sebaran_nilai_shmax_after)

print(hasil)

#---------------------------------------------------------------------#
# Membuat kurva sebaran nilai stress drop (theta vs delta theta)

## Membuat array nilai theta 0 hingga 180 drajat dengan interval 0.1 tanpa mengikutkan angka 0
theta_min = np.arange(0,45,0.1)
theta_plus = np.arange(45.1,180,0.1)
axis_theta = np.concatenate((theta_min,theta_plus))

plt.figure(figsize=(15,13))

## Menghitung nilai delta theta untuk masing-masing stress drop
for i in [-1, -0.8, -0.6, -0.4, -0.2, 0.2, 0.4, 0.6, 0.8, 1]:
    delta_th = [delta_theta(i, x) for x in axis_theta]
    plt.plot(axis_theta,delta_th,'black')
    plt.text(80, delta_th[800], str(i), fontsize=18)

for i in range(250):
#     if hasil['stress drop'][1] < bootstrap['stress drop'][i] < hasil['stress drop'][0]:
#         plt.plot(bootstrap['theta'][i], bootstrap['delta theta'][i], 'o', color='gray', markersize=6)
    plt.plot(bootstrap['theta'][i], bootstrap['delta theta'][i], 'o', color='gray', markersize=6)
plt.plot([hasil['theta'][0],hasil['theta'][1]], [hasil['delta theta'][2],hasil['delta theta'][2]], '-r', marker='|', markevery=[0, -1], markersize=12, markeredgewidth=2)
plt.plot([hasil['theta'][2],hasil['theta'][2]], [hasil['delta theta'][0],hasil['delta theta'][1]], '-r', marker='_', markevery=[0, -1], markersize=12, markeredgewidth=2)
plt.plot(hasil['theta'][2], hasil['delta theta'][2], 'ro', markersize=14)

plt.xlabel(r"$\theta$ (degree)", fontsize=30)
plt.ylabel(r"$\Delta\theta$ (degree)", fontsize=30)
plt.xlim(0,90)
plt.xticks(fontsize=20)
plt.ylim(-45,45)
plt.yticks(fontsize=20)
plt.grid()
plt.show()
plt.close()

print('Nilai stress drop: {}'.format(stress_drop(hasil['theta'][2], hasil['delta theta'][2])))

plt.figure(figsize=(15,13))

## Menghitung nilai delta theta untuk masing-masing stress drop
for i in [-1, -0.8, -0.6, -0.4, -0.2, 0.2, 0.4, 0.6, 0.8, 1]:
    delta_th = [delta_theta(i, x) for x in axis_theta]
    plt.plot(axis_theta,delta_th,'black')
    plt.text(80, delta_th[800], str(i), fontsize=18)

#for i in range(250):
#     if hasil['stress drop'][1] < bootstrap['stress drop'][i] < hasil['stress drop'][0]:
#         plt.plot(bootstrap['theta'][i], bootstrap['delta theta'][i], 'o', color='gray', markersize=6)
#     plt.plot(bootstrap['theta'][i], bootstrap['delta theta'][i], 'o', color='gray', markersize=6)
plt.plot([hasil['theta'][0],hasil['theta'][1]], [hasil['delta theta'][2],hasil['delta theta'][2]], '-r', marker='|', markevery=[0, -1], markersize=12, markeredgewidth=2)
plt.plot([hasil['theta'][2],hasil['theta'][2]], [hasil['delta theta'][0],hasil['delta theta'][1]], '-r', marker='_', markevery=[0, -1], markersize=12, markeredgewidth=2)
plt.plot(hasil['theta'][2], hasil['delta theta'][2], 'ro', markersize=14)

plt.xlabel(r"$\theta$ (degree)", fontsize=30)
plt.ylabel(r"$\Delta\theta$ (degree)", fontsize=30)
plt.xlim(0,90)
plt.xticks(fontsize=20)
plt.ylim(-45,45)
plt.yticks(fontsize=20)
plt.grid()
plt.show()
plt.close()

print('Nilai stress drop: {}'.format(stress_drop(hasil['theta'][2], hasil['delta theta'][2])))