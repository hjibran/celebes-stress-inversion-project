def konversi_lonlat_to_xyz(lon, lat, vlon, vlat, vup):
    import numpy as np

    # Konversi lon dan lat ke radian
    lon_rad = np.deg2rad(lon)
    lat_rad = np.deg2rad(lat)

    # Matriks transformasi
    transformation_matrix = np.array([
        [-np.sin(lon_rad), -np.sin(lat_rad) * np.cos(lon_rad), np.cos(lat_rad) * np.cos(lon_rad)],
        [np.cos(lon_rad), -np.sin(lat_rad) * np.sin(lon_rad), np.cos(lat_rad) * np.sin(lon_rad)],
        [0, np.cos(lat_rad), np.sin(lat_rad)]
    ])

    # Vektor kecepatan geodetik
    velocity_geodetic = np.array([vlon, vlat, vup])

    # Transformasi ke kartesian
    velocity_cartesian = transformation_matrix @ velocity_geodetic

    # Output hasil
    v_x, v_y, v_z = velocity_cartesian
    return v_x, v_y, v_z

def konversi_xyz_to_lonlat(lon, lat, vx, vy, vz):
    import numpy as np

    # Konversi lon dan lat ke radian
    lon_rad = np.deg2rad(lon)
    lat_rad = np.deg2rad(lat)

    # Transformasi ke kecepatan geodetik
    v_lambda = (-vx * np.sin(lon_rad) + vy * np.cos(lon_rad)) / np.cos(lat_rad)
    v_phi = vx * np.cos(lon_rad) * np.sin(lat_rad) + vy * np.sin(lon_rad) * np.sin(lat_rad) - vz * np.cos(lat_rad)
    v_h = vx * np.cos(lon_rad) * np.cos(lat_rad) + vy * np.sin(lon_rad) * np.cos(lat_rad) + vz * np.sin(lat_rad)

    # Output hasil
    return v_lambda, v_phi, v_h

def konversi_ITRF2000_to_sunda(lon, lat, vx, vy, vz):
    import numpy as np

    # Parameter Euler lempeng Sunda (dalam derajat dan radian/tahun)
    phi_euler = -2.5 # Latitude Euler
    lambda_euler = 129.9  # Longitude Euler
    omega_euler = 2.23  # Kecepatan rotasi (radian/tahun)

    # Konversi Euler ke kartesian
    phi_rad = np.deg2rad(phi_euler)
    lambda_rad = np.deg2rad(lambda_euler)
    omega_x = omega_euler * np.cos(phi_rad) * np.cos(lambda_rad)
    omega_y = omega_euler * np.cos(phi_rad) * np.sin(lambda_rad)
    omega_z = omega_euler * np.sin(phi_rad)
    omega = np.array([omega_x, omega_y, omega_z])

    # Radius Bumi (meter)
    R = 6371000

    # Hitung kecepatan relatif
    # Konversi koordinat GPS ke kartesian
    lat_rad = np.deg2rad(lat)
    lon_rad = np.deg2rad(lon)
    x_r = R * np.cos(lat_rad) * np.cos(lon_rad)
    y_r = R * np.cos(lat_rad) * np.sin(lon_rad)
    z_r = R * np.sin(lat_rad)
    r = np.array([x_r, y_r, z_r])

    # Hitung kecepatan prediksi
    v_pred = np.cross(omega, r)

    # Hitung kecepatan relatif
    v_gps = np.array([vx, vy, vz])
    v_rel = v_gps - v_pred / 1000  # Skala ke km/tahun

    # Output hasil
    return v_rel

import numpy as np
import pandas as pd

data = pd.read_csv("/mnt/d/socquet2006data.csv")
n_data = len(data)

result = np.zeros((n_data, 7))  
for i in range(n_data):
    vx_itrf, vy_itrf, vz_itrf = konversi_lonlat_to_xyz(data['Lon'][i], data['Lat'][i], data['V_lon'][i], data['V_lat'][i], data['V_up'][i])
    vx_sunda, vy_sunda, vz_sunda = konversi_ITRF2000_to_sunda(data['Lon'][i], data['Lat'][i], vx_itrf, vy_itrf, vz_itrf)
    vlon_sunda, vlat_sunda, vup_sunda = (konversi_xyz_to_lonlat(data['Lon'][i], data['Lat'][i], vx_sunda, vy_sunda, vz_sunda))

    result[i][0] = data['Lon'][i]; result[i][1] = data['Lat'][i]
    result[i][2] = -vlon_sunda; result[i][3] = -vlat_sunda
    result[i][4] = data['S_lon'][i]; result[i][5] = data['S_lat'][i]
    result[i][6] = data['Corr'][i]

tabel_hasil = pd.DataFrame(result, columns=['Long','Lat','Vlon','Vlat','dVlon','dVlat','Corr'])
tabel_hasil['Site'] = data['Site']
tabel_hasil.to_csv('/mnt/d/socquet2006datasundarelative.csv', index=False)