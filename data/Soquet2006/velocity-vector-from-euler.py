import pandas as pd
import geopandas as gpd

def haversine_distance(lat1, lon1, lat2, lon2):
    import math
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    
    Parameters:
    lat1, lon1: Coordinates of the first point (decimal degrees)
    lat2, lon2: Coordinates of the second point (decimal degrees)
    
    Returns:
    Distance between the two points in kilometers
    """
    # Radius of the Earth in kilometers
    R = 6371.0
    
    # Convert degrees to radians
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)
    
    # Differences
    dlon = lon2_rad - lon1_rad
    dlat = lat2_rad - lat1_rad
    
    # Haversine formula
    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    
    return distance

def euler_to_velocity(euler, xo, yo, x, y):
    import math
    import numpy as np

    kecepatan_sudut = math.radians(euler)
    jarak = haversine_distance(yo, xo, x, y)

    arah_center_ke_titik_tujuan = np.array([x-xo,y-yo])
    arah_kecepatan_linear = np.array([-arah_center_ke_titik_tujuan[1], arah_center_ke_titik_tujuan[0]])
    kecepatan_linear = jarak * kecepatan_sudut
    panjang_vektor_kecepatan_linear = np.linalg.norm(arah_kecepatan_linear)
    normalisasi_vektor_kecepatan_linear = arah_kecepatan_linear/panjang_vektor_kecepatan_linear
    vektor_kecepatan_linear = kecepatan_linear*normalisasi_vektor_kecepatan_linear
  
    komponen_x_kecepatan_linear = vektor_kecepatan_linear[0]
    komponen_y_kecepatan_linear = vektor_kecepatan_linear[1]
    return komponen_x_kecepatan_linear, komponen_y_kecepatan_linear

data = pd.read_csv('/mnt/d/celebes-stress-inversion-project/data/Soquet2006/velocity.csv')
data = pd.read_csv('/mnt/d/celebes-stress-inversion-project/data/Soquet2006/stationv3.csv')
boundary = gpd.read_file("/mnt/d/celebes-stress-inversion-project/data/Soquet2006/soquet2006plateboundary(LN).shp")
print(data)

lon = data['lon']
lat = data['lat']
block = data['block']
x = []
y = []
for i in range(len(data)):
    if block[i] == 'Makassar':
        euler = 1.4
        xo = 117.4
        yo = -4.8
    elif block[i] == 'North Sula':
        euler = -2.6
        xo = 129.5
        yo = 2.4
    elif block[i] == 'Manado':
        euler = -3.2
        xo = 126.5
        yo = 1.8
    elif block[i] == 'Banda':
        euler = 1.8
        xo = 113.3
        yo = -9.7
    elif block[i] == 'East Sula':
        euler = 2.2
        xo = 115.0
        yo = -7.9

    xtemp, ytemp = euler_to_velocity(euler, xo, yo, lon[i], lat[i])
    x.append(xtemp/20)
    y.append(ytemp/20)

import pygmt

fig = pygmt.Figure()

fig.coast(region=[117, 130, -9, 6],
          projection='M10',
          land='darkgray',
          frame=True)

fig.plot(data=boundary, pen="2.5p,black", label="microblock (Soquet, 2006)")

fig.velo(
    data={
        'x': lon,
        'y' :lat,
        "east_velocity": x,
        "north_velocity": y,
        #"east_sigma": data['dVlon'],
        #"north_sigma": data['dVlon'],
        #"correlation_EN": data['Corr.']
    },
    spec="e0.1/0.39+f18",
    #uncertaintyfill="lightblue1",
    pen="0.6p,red",
    line=True,
    vector="0.3c+p1p+e+gred"
)

fig.show()