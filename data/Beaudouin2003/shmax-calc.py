def shmax_dir(azim1,plng1,azim2,plng2,r,pos=False):
    
    import math as mt
    import numpy as np

    az1,pg1 = (mt.radians(azim1),mt.radians(plng1))
    az2,pg2 = (mt.radians(azim2),mt.radians(plng2))
    s1 = (np.cos(pg1)*np.sin(az1),np.cos(pg1)*np.cos(az1),-np.sin(pg1))
    s2 = (np.cos(pg2)*np.sin(az2),np.cos(pg2)*np.cos(az2),-np.sin(pg2))
    x = 2.*(s1[1]*s1[0]+(1-r)*s2[1]*s2[0])/((s1[1]**2-s1[0]**2) + (1-r)*(s2[1]**2-s2[0]**2))
    beta = 0.5*np.degrees(np.arctan(x))
    alpha = beta

    if pos:
        if azim1 <=45:
            alpha = beta
        elif azim1 <=90:
            alpha = 90+beta
        
        elif azim1 <=135:
            alpha = 90+beta
        elif azim1 <=180:
            alpha = 90+90+beta

        elif azim1 <=225:
            alpha = 180+beta
        elif azim1 <=270:
            alpha = 180+90+beta
            
        elif azim1 <=315:
            alpha = 270+beta
        elif azim1 <=360:
            alpha = 270+90+beta

    return alpha

import pandas as pd

data = pd.read_csv('/mnt/d/celebes-stress-inversion-project/data/Beaudouin2003/Beaudouin-stress.csv')
for i in range(len(data)):
    shmax = shmax_dir(data['Az1'][i],data['Pl1'][i],data['Az2'][i],data['Pl2'][i],data['R'][i],True)
    if shmax < 0:
        shmax+=360
    print(shmax)