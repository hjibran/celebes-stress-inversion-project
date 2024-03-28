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

Bootstrap = True

strinv_dir = os.environ['HOME'] + '/Dropbox/Software/Stressinverse_1.1.2/Programs_PYTHON'
if not strinv_dir in sys.path:
    sys.path.append(strinv_dir)



def run_stress_inversion(tag,sgmnt):
    
    ### NOTE: do not remove r before strings (r'filename'), to safely use
    #         backslashes in filenames

    #--------------------------------------------------------------------------
    # input file with focal mechnaisms
    #--------------------------------------------------------------------------
    if pre_or_pst == 'pst':
        datadir = r'./post_mainshock/segment_%s/' % sgmnt
    else:
        datadir = r'./pre_mainshock/segment_%s/' % sgmnt
    datadir = r'./Datanew/'
    outdir  = r'./Output/'
    outdir  = r'./Outnew/'
    figdir  = r'./Figures/'
    figdir  = r'./Fignew/'

    # repalce used for B-C-D segment
    #input_file = r'%sdata%s.dat' % (datadir,sgmnt[0]+'_all') #.replace('-','_'))
    input_file = r'%sdata%s.dat' % (datadir,sgmnt.replace('-','_'))
    input_file = datadir+pre_or_pst+r'%s_Input.dat' % sgmnt

    print('running for input file: %s' % input_file)


    #--------------------------------------------------------------------------
    # output file with results
    #--------------------------------------------------------------------------
    output_file = outdir+r'%s_Output' % tag

    # ASCII file with calculated principal mechanisms
    principal_mechanisms_file = outdir+r'%s_principal_mechanisms' % tag

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
    # figure files
    #--------------------------------------------------------------------------
    shape_ratio_plot = figdir+r'%s_shape_ratio' % tag
    stress_plot      = figdir+r'%s_stress_directions' % tag
    P_T_plot         = figdir+r'%s_P_T_axes' % tag
    Mohr_plot        = figdir+r'%s_Mohr_circles' % tag
    faults_plot      = figdir+r'%s_faults' % tag

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

    #####
    from read_mechanism import read_mechanisms
    from stress_inversion import stress_inversion
    from azimuth_plunge import azimuth_plunge
    from scipy.linalg import eig
    from numpy.linalg import eig
    from noisy_mechanisms import noisy_mechanisms
    from principal_mechanisms import principal_mechanisms
    from statistics_stress_inversion import statistics_stress_inversion
    from plot_stress import plot_stress
    from plot_mohr import plot_mohr
    from plot_stress_axes import plot_stress_axes
    from math import acos

    [strike_orig_1,dip_orig_1,rake_orig_1,strike_orig_2,dip_orig_2,rake_orig_2] = read_mechanisms(input_file)

    ##  solution from noise-free dara
    #--------------------------------------------------------------------------
    # inversion for stress
    #--------------------------------------------------------------------------

    [tau_optimum,shape_ratio,strike,dip,rake,instability,friction] = \
        stress_inversion (strike_orig_1,dip_orig_1,rake_orig_1,
                          strike_orig_2,dip_orig_2,rake_orig_2,
                          friction_min,friction_max,friction_step,N_iterations, N_realizations)

    #--------------------------------------------------------------------------
    # optimum principal stress axes
    #--------------------------------------------------------------------------
    [value,vector] = eig(tau_optimum)
    value_sorted = value.copy(); value_sorted.sort()
    j = value.argsort()

    sigma_vector_1_optimum = vector[:,j[0]]
    sigma_vector_2_optimum = vector[:,j[1]]
    sigma_vector_3_optimum = vector[:,j[2]]

    [direction_sigma_1, direction_sigma_2, direction_sigma_3] = \
        azimuth_plunge(tau_optimum)

    #--------------------------------------------------------------------------
    # principal focal mechanisms
    #--------------------------------------------------------------------------
    [principal_strike,principal_dip,principal_rake] = \
        principal_mechanisms(sigma_vector_1_optimum,sigma_vector_3_optimum,friction)

    ## solutions from noisy data
    #--------------------------------------------------------------------------
    # loop over noise realizations
    #--------------------------------------------------------------------------
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
            [sigma_vector_1,sigma_vector_2,sigma_vector_3,
             shape_ratio_noisy,tau] = \
                statistics_stress_inversion(strike1,dip1,rake1,strike2,dip2,rake2,
                                            friction,N_iterations,N_realizations)
        else:
            # superposition of noise to focal mechanisms
            [strike1,dip1,rake1,strike2,dip2,rake2,n_error,u_error] = \
                 noisy_mechanisms(mean_deviation,strike_orig_1,dip_orig_1,
                                  rake_orig_1)
            n_error_[i] = n_error.mean()
            u_error_[i] = u_error.mean()

            [sigma_vector_1,sigma_vector_2,sigma_vector_3,
             shape_ratio_noisy,tau] = \
                statistics_stress_inversion(strike1,dip1,rake1,strike2,dip2,rake2,
                                            friction,N_iterations,N_realizations)

        sigma_vector_1_statistics[:,i] = sigma_vector_1
        sigma_vector_2_statistics[:,i] = sigma_vector_2
        sigma_vector_3_statistics[:,i] = sigma_vector_3
        shape_ratio_statistics[i]   = shape_ratio_noisy

        [sigma_vector_1_directions[:,i],
         sigma_vector_2_directions[:,i],
         sigma_vector_3_directions[:,i]] = azimuth_plunge(tau)

    #--------------------------------------------------------------------------
    # calculation of errors of the stress inversion
    #--------------------------------------------------------------------------
    sigma_1_error_statistics = np.zeros(N_noise_realizations)
    sigma_2_error_statistics = np.zeros(N_noise_realizations)
    sigma_3_error_statistics = np.zeros(N_noise_realizations)
    for i in range(N_noise_realizations):
        sigma_1_error_statistics[i] = np.degrees(acos(abs(\
                                                          np.dot(sigma_vector_1_statistics[:,i],
                                                                 sigma_vector_1_optimum))))
        sigma_2_error_statistics[i] = np.degrees(acos(abs(\
                                                          np.dot(sigma_vector_2_statistics[:,i],
                                                                 sigma_vector_2_optimum))))
        sigma_3_error_statistics[i] = np.degrees(acos(abs(\
                                                          np.dot(sigma_vector_3_statistics[:,i],
                                                                 sigma_vector_3_optimum))))
        shape_ratio_error_statistics[i] = 100*abs((shape_ratio-\
                                                   shape_ratio_statistics[i])\
                                                  /shape_ratio)

    #--------------------------------------------------------------------------
    # confidence limits
    #--------------------------------------------------------------------------
    mean_n_error = n_error_.mean()    # These are never
    mean_u_error = u_error_.mean()    #   used?

    max_sigma_1_error = sigma_1_error_statistics.max()
    max_sigma_2_error = sigma_2_error_statistics.max()
    max_sigma_3_error = sigma_3_error_statistics.max()

    max_shape_ratio_error = abs(shape_ratio_error_statistics).max()

    ## saving the results
    sigma_1 = types.SimpleNamespace()
    sigma_1.azimuth = direction_sigma_1[0]
    sigma_1.plunge  = direction_sigma_1[1]
    sigma_2 = types.SimpleNamespace()
    sigma_2.azimuth = direction_sigma_2[0]
    sigma_2.plunge  = direction_sigma_2[1]
    sigma_3 = types.SimpleNamespace()
    sigma_3.azimuth = direction_sigma_3[0]
    sigma_3.plunge  = direction_sigma_3[1]

    mechanisms = types.SimpleNamespace()
    mechanisms.strike = strike; mechanisms.dip = dip; mechanisms.rake = rake
    mechanisms_data   = np.array([strike, dip, rake])

    principal_mechanisms.strike = principal_strike
    principal_mechanisms.dip = principal_dip
    principal_mechanisms.rake = principal_rake
    principal_mechanisms_data = np.array([principal_strike, principal_dip,
                                          principal_rake])

    output_file_mat = output_file+'.mat'
    output_file_dat = output_file+'.dat'
    output_file_drs = output_file+'_drs.dat'
    output_file_sts = output_file+'_sts.dat'
    principal_mechanisms_file_dat = principal_mechanisms_file+'.dat'

    np.savez(output_file_sts,s1=sigma_vector_1_statistics,
             s2=sigma_vector_2_statistics,s3=sigma_vector_3_statistics,
             shp=shape_ratio_statistics)
    np.savez(output_file_drs,s1=sigma_vector_1_directions,
             s2=sigma_vector_2_directions,s3=sigma_vector_3_directions,
             shp=shape_ratio_statistics)
    np.savez(output_file_mat,sigma_1=sigma_1,sigma_2=sigma_2,sigma_3=sigma_3,
             shape_ratio=shape_ratio,mechanisms=mechanisms,friction=friction,
             principal_mechanisms=principal_mechanisms)
    np.savetxt(output_file_dat,
               [mechanisms_data[:,i] for i in range(mechanisms_data.shape[1])],
               fmt='%15.7e') 
    np.savetxt(principal_mechanisms_file_dat,
               [principal_mechanisms_data[:,i] for i in range(2)],fmt='%15.7e')

    ## plotting the results

    #--------------------------------------------------------------------------
    # P/T axes and the optimum principal stress axes
    #--------------------------------------------------------------------------
    plot_stress(tau_optimum,strike,dip,rake,P_T_plot)

    #--------------------------------------------------------------------------
    # Mohr circlediagram
    #--------------------------------------------------------------------------
    plot_mohr(tau_optimum,strike,dip,rake,principal_strike,
              principal_dip,principal_rake,Mohr_plot)

    #--------------------------------------------------------------------------
    # confidence limiuts of the principal stress axes
    #--------------------------------------------------------------------------
    plot_stress_axes(sigma_vector_1_statistics,sigma_vector_2_statistics,
                     sigma_vector_3_statistics,stress_plot)

    #--------------------------------------------------------------------------
    # confidence limits (histogram) of the shape ratio
    #--------------------------------------------------------------------------
    fig = plt.figure()
    plt.hist(shape_ratio_statistics,shape_ratio_axis)
    #v = axis; axis([shape_ratio_min shape_ratio_max v(3) v(4)]);
    # saving the plot
    plt.savefig(shape_ratio_plot+'.png');
    plt.close(fig)

for pre_or_pst in ['pre', 'pst']:
    for sgmnt in ['A-B-C','A','B','C']: #,'F','G']:
        tag = pre_or_pst + sgmnt  # Dataset identifier
        run_stress_inversion(tag,sgmnt)
