#!/home/haidir/celebes-stress-inversion-project/venv/bin/python3
#*************************************************************************#
#                                                                         #
#  script INPUT_PARAMETERS                                                #
#                                                                         #
#  list of input parameters needed for the inversion                      #
#                                                                         #
#*************************************************************************#
import numpy as np
import os
import sys

file_path = str(sys.argv[1])
eps = float(sys.argv[2])
tetangga = int(sys.argv[3])
kelas = int(sys.argv[4])
dir = str(sys.argv[5])

### NOTE: do not remove r before strings (r'filename'), to safely use
#         backslashes in filenames

#--------------------------------------------------------------------------
# input file with focal mechnaisms
#--------------------------------------------------------------------------
input_file = r'{}'.format(file_path) #West_Bohemia_mechanisms.dat'

#--------------------------------------------------------------------------
# output file with results
#--------------------------------------------------------------------------
output_file = r'{}/stressinverse/Output/output/cls{}'.format(dir, kelas) #West_Bohemia_Output'

# ASCII file with calculated principal mechanisms
principal_mechanisms_file = r'{}/stressinverse/Output/principal_mechanisms/cls{}'.format(dir, kelas) #West_Bohemia_principal_mechanisms' 

#-------------------------------------------------------------------------
# accuracy of focal mechansisms
#--------------------------------------------------------------------------
# number of random noise realizations for estimating the accuracy of the
# solution
N_noise_realizations = 100
# =============================================================================
# 
# estimate of noise in the focal mechanisms (in degrees)
# the standard deviation of the normal distribution of
# errors
mean_deviation = 5

#--------------------------------------------------------------------------
# figure files
#--------------------------------------------------------------------------
shape_ratio_plot = r'{}/stressinverse/Figure/shape_ratio/cls{}_shape_ratio'.format(dir, kelas)
stress_plot      = r'{}/stressinverse/Figure/stress_directions/cls{}_stress_directions'.format(dir, kelas)
P_T_plot         = r'{}/stressinverse/Figure/P_T_axes/cls{}_P_T_axes'.format(dir, kelas)
Mohr_plot        = r'{}/stressinverse/Figure/Mohr_circles/cls{}_Mohr_circles'.format(dir, kelas)
faults_plot      = r'{}/stressinverse/Figure/fault/cls{}_fault'.format(dir, kelas)
 
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


#--------------------------------------------------------------------------
# create output directories if needed
all_files = (output_file, shape_ratio_plot, stress_plot, P_T_plot, Mohr_plot, faults_plot)
for f in all_files:
    folder = os.path.dirname(f)
    if not os.path.exists(folder):
        os.makedirs(folder)
