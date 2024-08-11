# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 15:20:59 2022

@author: Taufiq Rafie
"""
import math as mt
import numpy as np
import matplotlib.pyplot as plt

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
    if pos:
        alpha = np.where(beta < 0., beta+90.,beta)
    else:
        alpha = beta
    return alpha

#shmax=shmax_dir(211,30,304,52,0.7,pos=True)