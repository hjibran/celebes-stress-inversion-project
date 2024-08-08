#!/home/haidir/celebes-stress-inversion-project/venv/bin/python3
import scipy.io
import pandas as pd
import numpy as np

mat = scipy.io.loadmat("/mnt/d/celebes-stress-inversion-project/Result/stressinversewithbootstrap/kelas9/output.mat")#input("Masukkan path file mat yang ingin dilihat:\n"))

shape_ratio= mat['shape_ratio'][0][0]
sigma1 = np.array([1, mat['sigma_1'][0][0][0][0][0], mat['sigma_1'][0][0][1][0][0]])
sigma2 = np.array([2, mat['sigma_2'][0][0][0][0][0], mat['sigma_2'][0][0][1][0][0]])
sigma3 = np.array([3, mat['sigma_3'][0][0][0][0][0], mat['sigma_3'][0][0][1][0][0]])
sigma = pd.DataFrame(np.array([sigma1, sigma2, sigma3]), columns=['sigma', 'azimuth', 'plunge'])

planeA = np.array([mat['principal_mechanisms'][0][0][0][0][0],
                   mat['principal_mechanisms'][0][0][1][0][0],
                   mat['principal_mechanisms'][0][0][2][0][0]])
planeB = np.array([mat['principal_mechanisms'][0][0][0][0][1],
                   mat['principal_mechanisms'][0][0][1][0][1],
                   mat['principal_mechanisms'][0][0][2][0][1]])
FM_principal = pd.DataFrame(np.array([planeA, planeB]), columns=['strike', 'dip', 'rake'])


mechanisms = mat['mechanisms']
mechanisms_data = mat['mechanisms_data']
friction = mat['friction'][0][0]


print("----------------------------------------------------\nPrincipal Mechanisms")
print(FM_principal)
print("----------------------------------------------------\nStress Directions")
print(sigma)
print("----------------------------------------------------\nShape Ratio")
print("{:0.3f}".format(shape_ratio))
print("----------------------------------------------------\nFriction")
print("{:0.3f}".format(friction))
#print("----------------------------------------------------\nMechanisms")
#print(mechanisms)
#print("----------------------------------------------------\nMechanisms Data")
#print(mechanisms_data)
print("----------------------------------------------------")
