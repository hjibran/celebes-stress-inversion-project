#*************************************************************************#
#                                                                         #
#  script INPUT_PARAMETERS                                                #
#                                                                         #
#  list of input parameters needed for the inversion                      #
#                                                                         #
#*************************************************************************#
import numpy as np
import os,sys
import matplotlib.pyplot as plt
import types
from random import choice
np.random.seed(42)
strinv_dir = '/mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Programs_PYTHON'
if not strinv_dir in sys.path:
    sys.path.append(strinv_dir)

file_path = "/mnt/d/celebes-stress-inversion-project/Result/eps0.40min15/stressinverse/data/cls6.dat"

cekbootstrap = "y" # str(input("Bootstrap[y/n]: "))
if  cekbootstrap == "y":
    Bootstrap = True
elif cekbootstrap == "n":
    Bootstrap = False
else:
    ("Your input is invalid")

### NOTE: do not remove r before strings (r'filename'), to safely use
#         backslashes in filenames

#--------------------------------------------------------------------------
# input file with focal mechnaisms
#--------------------------------------------------------------------------
input_file = r'{}'.format(file_path) #West_Bohemia_mechanisms.dat'
 

#-------------------------------------------------------------------------
# accuracy of focal mechansisms
#--------------------------------------------------------------------------
# number of random noise realizations for estimating the accuracy of the
# solution
N_noise_realizations = 250
# =============================================================================
# 
# estimate of noise in the focal mechanisms (in degrees)
# the standard deviation of the normal distribution of
# errors
mean_deviation = 10

#--------------------------------------------------------------------------
# advanced control parameters (usually not needed to be changed)
#--------------------------------------------------------------------------
# number of iterations of the stress inversion 
N_iterations = 6

# number of initial stres inversions with random choice of faults
N_realizations = 10

# axis of the histogram of the shape ratio
shape_ratio_min = 0
shape_ratio_max = 1
shape_ratio_step = 0.025

shape_ratio_axis = np.arange(shape_ratio_min+0.0125, shape_ratio_max, shape_ratio_step)

# interval for friction values
friction_min  = 0.40
friction_max  = 1.00
friction_step = 0.05


import read_mechanism as rm
strike_orig_1, dip_orig_1, rake_orig_1, strike_orig_2, dip_orig_2, rake_orig_2 = rm.read_mechanisms(input_file)

##  solution from noise-free dara
#--------------------------------------------------------------------------
# inversion for stress
#--------------------------------------------------------------------------
import stress_inversion as si
tau_optimum,shape_ratio,strike,dip,rake,instability,friction = si.stress_inversion(
    strike_orig_1,dip_orig_1,rake_orig_1,strike_orig_2,dip_orig_2,rake_orig_2,
    friction_min,friction_max,friction_step,N_iterations,N_realizations)     # inverze napeti z ohniskovych mechanismu, Michael (1984,1987)

#--------------------------------------------------------------------------
# optimum principal stress axes
#--------------------------------------------------------------------------
import azimuth_plunge as ap
diag_tensor, vector = np.linalg.eig(tau_optimum)

value = [diag_tensor[0], diag_tensor[1], diag_tensor[2]]
value_sorted = np.sort(value)
j = np.argsort(value)

sigma_vector_1_optimum  = np.array(vector[:,j[0]])
sigma_vector_2_optimum  = np.array(vector[:,j[1]])
sigma_vector_3_optimum  = np.array(vector[:,j[2]])

direction_sigma_1, direction_sigma_2, direction_sigma_3 = ap.azimuth_plunge(tau_optimum)

#--------------------------------------------------------------------------
# principal focal mechanisms
#--------------------------------------------------------------------------
import principal_mechanisms as pm
principal_strike, principal_dip, principal_rake = pm.principal_mechanisms(sigma_vector_1_optimum,sigma_vector_3_optimum,friction)

## solutions from noisy data
#--------------------------------------------------------------------------
# loop over noise realizations
#--------------------------------------------------------------------------
import noisy_mechanisms as nm
import statistics_stress_inversion_bot as ssi

n_error_ = np.zeros(N_noise_realizations)
u_error_ = np.zeros(N_noise_realizations)

shape_ratio_statistics = np.zeros(N_noise_realizations)
shape_ratio_error_statistics = np.zeros(N_noise_realizations)

sigma_vector_1_statistics = np.zeros((3,N_noise_realizations))
sigma_vector_2_statistics = np.zeros((3,N_noise_realizations))
sigma_vector_3_statistics = np.zeros((3,N_noise_realizations))
sigma_vector_1_directions = np.zeros((2,N_noise_realizations))
sigma_vector_2_directions = np.zeros((2,N_noise_realizations))
sigma_vector_3_directions = np.zeros((2,N_noise_realizations))

idxs = [i for i in range(len(strike_orig_1))]
for i in range(N_noise_realizations):
    if Bootstrap:
        idxs_boot = np.array([choice(idxs) for i in range(len(strike_orig_1))])
        strike1 = strike_orig_1[idxs_boot]
        dip1    = dip_orig_1[idxs_boot]
        rake1   = rake_orig_1[idxs_boot]
        strike2 = strike_orig_2[idxs_boot]
        dip2    = dip_orig_2[idxs_boot]
        rake2   = rake_orig_2[idxs_boot]
        sigma_vector_1,sigma_vector_2,sigma_vector_3,shape_ratio_noisy,tau = \
            ssi.statistics_stress_inversion(strike1,dip1,rake1,strike2,dip2,rake2,
                                        friction,N_iterations,N_realizations)
    else:
        # superposition of noise to focal mechanisms
        strike1,dip1,rake1,strike2,dip2,rake2,n_error,u_error = nm.noisy_mechanisms(mean_deviation,strike_orig_1,dip_orig_1,rake_orig_1)
        
        n_error_[i] = np.mean(n_error)
        u_error_[i] = np.mean(u_error)

        sigma_vector_1,sigma_vector_2,sigma_vector_3,shape_ratio_noisy,tau = \
            ssi.statistics_stress_inversion(strike1,dip1,rake1,strike2,dip2,rake2,friction,N_iterations,N_realizations)

    sigma_vector_1_statistics [:,i] = sigma_vector_1
    sigma_vector_2_statistics [:,i] = sigma_vector_2
    sigma_vector_3_statistics [:,i] = sigma_vector_3
    shape_ratio_statistics    [i]   = shape_ratio_noisy

    [sigma_vector_1_directions[:,i],
        sigma_vector_2_directions[:,i],
        sigma_vector_3_directions[:,i]] = ap.azimuth_plunge(tau)
    
sigma_1_azimut_distribution, sigma_1_plunge_distribution  = sigma_vector_1_directions[0], sigma_vector_1_directions[1]
sigma_2_azimut_distribution, sigma_2_plunge_distribution  = sigma_vector_2_directions[0], sigma_vector_2_directions[1]
sigma_3_azimut_distribution, sigma_3_plunge_distribution  = sigma_vector_3_directions[0], sigma_vector_3_directions[1]


#--------------------------------------------------------------------------
# calculation of errors of the stress inversion
#--------------------------------------------------------------------------

sigma_1_error_statistics = np.zeros(N_noise_realizations)
sigma_2_error_statistics = np.zeros(N_noise_realizations)
sigma_3_error_statistics = np.zeros(N_noise_realizations)
shape_ratio_error_statistics = np.zeros(N_noise_realizations)

for i in range(N_noise_realizations):
    sigma_1_error_statistics[i] = np.degrees(np.arccos(np.abs(\
                                                        np.dot(sigma_vector_1_statistics[:,i],
                                                                sigma_vector_1_optimum))))
    sigma_2_error_statistics[i] = np.degrees(np.arccos(np.abs(\
                                                        np.dot(sigma_vector_2_statistics[:,i],
                                                                sigma_vector_2_optimum))))
    sigma_3_error_statistics[i] = np.degrees(np.arccos(np.abs(\
                                                        np.dot(sigma_vector_3_statistics[:,i],
                                                                sigma_vector_3_optimum))))
    shape_ratio_error_statistics[i] = 100*np.abs((shape_ratio-\
                                                shape_ratio_statistics[i])\
                                                /shape_ratio)

#--------------------------------------------------------------------------
# confidence limits
#--------------------------------------------------------------------------
mean_n_error = np.mean(n_error_)
mean_u_error = np.mean(u_error_)

max_sigma_1_error = np.max(sigma_1_error_statistics)
max_sigma_2_error = np.max(sigma_2_error_statistics)
max_sigma_3_error = np.max(sigma_3_error_statistics)

max_shape_ratio_error = np.max(np.abs(shape_ratio_error_statistics))

# ------------------------------------------------
# saving the results
# ------------------------------------------------
import scipy.io as sio
import confidence_interval as ci

#if Bootstrap:
#    direction_sigma_1[0], ci_azimuth_1 = ci.confidence_interval(sigma_1_azimut_distribution)
print(ci.confidence_interval(sigma_1_azimut_distribution))
print(ci.confidence_interval(sigma_1_plunge_distribution))
print(ci.confidence_interval(sigma_2_azimut_distribution))
print(ci.confidence_interval(sigma_2_plunge_distribution))
print(ci.confidence_interval(sigma_3_azimut_distribution))
print(ci.confidence_interval(sigma_3_plunge_distribution))

ci.histogram(sigma_1_azimut_distribution, 
                sigma_1_plunge_distribution, 
                sigma_2_azimut_distribution, 
                sigma_2_plunge_distribution, 
                sigma_3_azimut_distribution, 
                sigma_3_plunge_distribution, 
                25)


sigma_1 = {'azimuth': '{:.3f}'.format(direction_sigma_1[0]), 'plunge': '{:.3f}'.format(direction_sigma_1[1]) }
sigma_2 = {'azimuth': '{:.3f}'.format(direction_sigma_2[0]), 'plunge': '{:.3f}'.format(direction_sigma_2[1]) }
sigma_3 = {'azimuth': '{:.3f}'.format(direction_sigma_3[0]), 'plunge': '{:.3f}'.format(direction_sigma_3[1]) }


sigma_1_data = np.transpose(np.array([direction_sigma_1[0], direction_sigma_1[1]]))
sigma_2_data = np.transpose(np.array([direction_sigma_2[0], direction_sigma_2[1]]))
sigma_3_data = np.transpose(np.array([direction_sigma_3[0], direction_sigma_3[1]]))

mechanisms = {'strike': strike, 'dip': dip, 'rake': rake, }

mechanisms_data = np.transpose(np.array([strike, dip, rake]))
principal_mechanisms_data = np.transpose(np.array([principal_strike, principal_dip, principal_rake]))

principal_mechanisms = {'strike': principal_strike, 'dip': principal_dip, 'rake': principal_rake, }

#np.savez(output_file_sts,s1=sigma_vector_1_statistics,
#           s2=sigma_vector_2_statistics,s3=sigma_vector_3_statistics,
#            shp=shape_ratio_statistics)


#np.savez(output_file_drs,s1=sigma_vector_1_directions,
#            s2=sigma_vector_2_directions,s3=sigma_vector_3_directions,
#            shp=shape_ratio_statistics)

#print(sigma_1)
#print(sigma_2)
#print(sigma_3)