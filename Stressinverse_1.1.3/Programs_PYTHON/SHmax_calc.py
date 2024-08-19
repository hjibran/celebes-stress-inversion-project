# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 15:20:59 2022

@author: Taufiq Rafie
"""
import math as mt
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

'''
azim1, plng1 are the azimuth and plunge for sigma1, and similarly for plng2, etc (in degrees). Because of the ambiguity in the arctan function, you sometimes need to add 90 degrees, but I don't think you need to do that for your data, so just leave out the "pos" argument.
The routine returns alpha, the azimuth of SHmax in degrees.
'''

def shmax_dir(azim1,plng1,azim2,plng2,r,pos=False):
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

    """
    if pos:
        alpha = np.where(beta < 0., beta+90.,beta)
    else:
        alpha = beta
    """
"""
SHmax = np.zeros([360, 5])
i=0
while i <= 359:
    az1 = i
    pl1 = 0
    az2 = i+90
    pl2 = 0
    shmax = "{:.2f}".format(shmax_dir(az1, pl1, az2, pl2, 1, True))
    
    SHmax[i][0] = az1; SHmax[i][1] = pl1
    SHmax[i][2] = az2; SHmax[i][3] = pl2
    SHmax[i][4] = shmax

    i+=1

data = pd.DataFrame(SHmax, columns=["az1", "pl1", "az2", "pl2", "shmax"])
data.to_csv("shmax.csv")
"""