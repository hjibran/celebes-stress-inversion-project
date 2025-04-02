#!/home/haidir/celebes-stress-inversion-project/bin/python3

"""
    This is the python code to run the modified Stressinversion
    by Vavricuk to calculate the error with bootstrap instead of
    the method given by him. furthermore, this code also runs 
    the SHmax calculation performed by Taufiq Rafie 2021.

    This code was created by Haidir Jibran for his final project 
    as a Geophysics student at Hasanuddin University.
"""
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# ========================================================================================
# ------------------------------------------------
# input parameter
# ------------------------------------------------
#output option
    # export output: 1
    # print  output: 2
    # statistic error: 3
    # to run all cluster: 4
output = 1
if output == 3:
    input_file = "/mnt/d/celebes-stress-inversion-project/Result/eps0.40min15/stressinverse/data/cls{}.dat".format(sys.argv[1])
    seed = int(sys.argv[2])
elif output == 4:
    input_file = "/mnt/d/celebes-stress-inversion-project/Result/eps{}min15-final/stressinverse/data/cls{}.dat".format(sys.argv[1], sys.argv[2])
    output_file = "/mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Output/eps{}pts15/new_shmax/cls{}/".format(sys.argv[1], sys.argv[2])
    seed = int(sys.argv[3])
else:
    # path to file input, file output, and seed (to initialize random bootstrap)
    input_file = r"/mnt/d/celebes-stress-inversion-project/Result/eps0.40min15-final/stressinverse/data/palu0.4after.dat"
    output_file = r"/mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Output/eps0.40pts15/new_shmax/palu_after_2018/"
    seed = 1

# plot option
    # plot with plt.show(): 1
    # save to picture file: 2
    #  don't plot anything: 3
plot = 2

# number of random bootstrap
N_bootstrap = 250

# ----------------------------------------------------------------------------------------
# advance control parameter(usually not needed to be changed)
# number of iterations of the stress inversion 
N_iterations = 6

# number of initial stres inversions with random choice of faults
N_realizations = 10

# axis of the histogram of the shape ratio
shape_ratio_axis = np.arange(0+0.0125, 1, 0.025)
 
# interval for friction values
friction_min  = 0.40
friction_max  = 1.00
friction_step = 0.05


# ========================================================================================
# ------------------------------------------------
# make stress inversion function
# ------------------------------------------------
def run(str1,dip1,rak1,str2,dip2,rak2,k=0,
        friction_min=friction_min,friction_max=friction_max,friction_step=friction_step,
        N_iterations=N_iterations,N_realizations=N_realizations):
    
    # ----------------------------------------------------------------------------------------
    # inversion for stress
    import stress_inversion as si
    tau_optimum,shape_ratio,strike,dip,rake,instability,friction,sigma = si.stress_inversion(
        str1,dip1,rak1,str2,dip2,rak2,
        friction_min,friction_max,friction_step,N_iterations,N_realizations) 
    
    # return the component of tau
    t11 = tau_optimum[0][0]; t12 = tau_optimum[0][1]; t13 = tau_optimum[0][2]
    t22 = tau_optimum[1][1]; t23 = tau_optimum[1][2]
    t33 = tau_optimum[2][2]

    # ----------------------------------------------------------------------------------------
    # optimum principal stress axes
    import azimuth_plunge as ap
    diag_tensor, vector = np.linalg.eig(tau_optimum)

    value = [diag_tensor[0], diag_tensor[1], diag_tensor[2]]
    value_sorted = np.sort(value)
    j = np.argsort(value)

    sigma_vector_1_optimum  = np.array(vector[:,j[0]])
    sigma_vector_2_optimum  = np.array(vector[:,j[1]])
    sigma_vector_3_optimum  = np.array(vector[:,j[2]])

    direction_sigma_1, direction_sigma_2, direction_sigma_3 = ap.azimuth_plunge(tau_optimum)
    sg1_azm = direction_sigma_1[0]; sg1_pln  = direction_sigma_1[1]
    sg2_azm = direction_sigma_2[0]; sg2_pln  = direction_sigma_2[1]
    sg3_azm = direction_sigma_3[0]; sg3_pln  = direction_sigma_3[1]

    # ----------------------------------------------------------------------------------------
    # SHmax
    import SHmax_calc as sh
    shmax = sh.shmax_dir(sg1_azm,sg1_pln,sg2_azm,sg2_pln,shape_ratio,True)

    # ----------------------------------------------------------------------------------------
    # slip deviations
    import slip_deviation as sd
    slip_deviation_1, slip_deviation_2 = sd.slip_deviation(tau_optimum,strike,dip,rake)

    # ----------------------------------------------------------------------------------------
    # principal focal mechanism
    import principal_mechanisms as pm
    principal_strike, principal_dip, principal_rake = pm.principal_mechanisms(sigma_vector_1_optimum,sigma_vector_3_optimum,friction)

    # ----------------------------------------------------------------------------------------
    # simpson index
    import simpson_index as simpx

    if len(k) == 0:
        K = simpx.fault_mechanism(principal_strike[0], principal_dip[0], principal_rake[0])
        aR = simpx.simpson_index(K, sigma)
    else:
        K = simpx.fault_mechanism(k["principal strike 1"][0], k["principal dip 1"][0], k["principal rake 1"][0]) 
        aR = simpx.simpson_index(K, sigma)
    # ----------------------------------------------------------------------------------------
    # return the value
    return t11, t12, t13, t22, t23, t33,\
            sg1_azm, sg1_pln, sg2_azm, sg2_pln, sg3_azm, sg3_pln,\
            shape_ratio, friction[0], shmax,\
            principal_strike[0], principal_dip[0], principal_rake[0],\
            principal_strike[1], principal_dip[1], principal_rake[1],\
            strike, dip, rake,\
            sigma_vector_1_optimum, sigma_vector_2_optimum, sigma_vector_3_optimum,\
            aR


# ========================================================================================
# ------------------------------------------------
# reading input data
# ------------------------------------------------
# focal mechanism
import read_mechanism as rm
or_str1,or_dip1,or_rak1,or_str2,or_dip2,or_rak2 = rm.read_mechanisms(input_file)


# ========================================================================================
# ------------------------------------------------
# run stress inversion
# ------------------------------------------------
# origin data
# make function
def orgn(or_str1,or_dip1,or_rak1,or_str2,or_dip2,or_rak2):
    print('run origin')
    import pandas as pd
    import numpy as np

    k = pd.DataFrame()
    # run the stress inversion with origin data
    org = np.zeros((2, 22))
    org[0][0], org[0][1], org[0][2], org[0][3], org[0][4], org[0][5],\
        org[0][6], org[0][7], org[0][8], org[0][9], org[0][10], org[0][11],\
        org[0][12], org[0][13], org[0][14],\
        org[0][15], org[0][16], org[0][17],\
        org[0][18], org[0][19], org[0][20],\
        strike, dip, rake,\
        sigma_vector_1_optimum, sigma_vector_2_optimum, sigma_vector_3_optimum,\
        org[0][21]\
        = run(or_str1,or_dip1,or_rak1,or_str2,or_dip2,or_rak2,k)

    print('origin selesai')
    # make a data frame for stress inversion output
    origin = pd.DataFrame(org, columns=
        ["tau11", "tau12", "tau13", "tau22", "tau23", "tau33",
        "azimuth sigma 1", "plunge sigma 1", "azimuth sigma 2", "plunge sigma 2", "azimuth sigma 3", "plunge sigma 3",
        "shape ratio", "friction", "SHmax",
        "principal strike 1", "principal dip 1", "principal rake 1",
        "principal strike 2", "principal dip 2", "principal rake 2",
        "simpson index"])

    # return the data frame
    return origin, strike, dip, rake
origin, strike, dip, rake = orgn(or_str1,or_dip1,or_rak1,or_str2,or_dip2,or_rak2)

# ----------------------------------------------------------------------------------------
# data with bootstrap
# make function
def btstrp(or_str1,or_dip1,or_rak1,or_str2,or_dip2,or_rak2, origin):
    import numpy as np
    import pandas as pd
    from random import choice
    np.random.seed(seed)

    # make bootstrap data
    boots = np.zeros((N_bootstrap, 22))
    sigma_vector_11 = np.zeros((N_bootstrap)); sigma_vector_12 = np.zeros((N_bootstrap)); sigma_vector_13 = np.zeros((N_bootstrap))
    sigma_vector_21 = np.zeros((N_bootstrap)); sigma_vector_22 = np.zeros((N_bootstrap)); sigma_vector_23 = np.zeros((N_bootstrap))
    sigma_vector_31 = np.zeros((N_bootstrap)); sigma_vector_32 = np.zeros((N_bootstrap)); sigma_vector_33 = np.zeros((N_bootstrap))
    
    idxs = [i for i in range(len(or_str1))]
    for i in range(N_bootstrap):
        print("run bootstrap ke {}".format(i+1))
        idxs_boot = np.array([np.random.randint(0, len(or_str1)) for i in range(len(or_str1))])
        bt_str1 = or_str1[idxs_boot]
        bt_dip1 = or_dip1[idxs_boot]
        bt_rak1 = or_rak1[idxs_boot]
        bt_str2 = or_str2[idxs_boot]
        bt_dip2 = or_dip2[idxs_boot]
        bt_rak2 = or_rak2[idxs_boot]

        origin = origin
        # run the stress inversion with origin data
        boots[i][0], boots[i][1], boots[i][2], boots[i][3], boots[i][4], boots[i][5],\
            boots[i][6], boots[i][7], boots[i][8], boots[i][9], boots[i][10], boots[i][11],\
            boots[i][12], boots[i][13], boots[i][14],\
            boots[i][15], boots[i][16], boots[i][17],\
            boots[i][18], boots[i][19], boots[i][20],\
            strike, dip, rake,\
            sigma_vector_1_optimum, sigma_vector_2_optimum, sigma_vector_3_optimum,\
            boots[i][21],\
            = run(bt_str1,bt_dip1,bt_rak1,bt_str2,bt_dip2,bt_rak2,origin)
        
        sigma_vector_11[i] = sigma_vector_1_optimum[0]; sigma_vector_12[i] = sigma_vector_1_optimum[1]; sigma_vector_13[i] = sigma_vector_1_optimum[2]
        sigma_vector_21[i] = sigma_vector_2_optimum[0]; sigma_vector_22[i] = sigma_vector_2_optimum[1]; sigma_vector_23[i] = sigma_vector_2_optimum[2]
        sigma_vector_31[i] = sigma_vector_3_optimum[0]; sigma_vector_32[i] = sigma_vector_3_optimum[1]; sigma_vector_33[i] = sigma_vector_3_optimum[2]

    print('bootstrap selesai')
    # make a data frame for stress inversion output
    bootstrap = pd.DataFrame(boots, columns=
        ["tau11", "tau12", "tau13", "tau22", "tau23", "tau33",
        "azimuth sigma 1", "plunge sigma 1", "azimuth sigma 2", "plunge sigma 2", "azimuth sigma 3", "plunge sigma 3",
        "shape ratio", "friction", "SHmax",
        "principal strike 1", "principal dip 1", "principal rake 1",
        "principal strike 2", "principal dip 2", "principal rake 2",
        "simpson index"])
    
    sigma_vector_1_statistics = np.array([sigma_vector_11, sigma_vector_12, sigma_vector_13])
    sigma_vector_2_statistics = np.array([sigma_vector_21, sigma_vector_22, sigma_vector_23])
    sigma_vector_3_statistics = np.array([sigma_vector_31, sigma_vector_32, sigma_vector_33])
    
    # return the data frame
    return bootstrap, sigma_vector_1_statistics, sigma_vector_2_statistics, sigma_vector_3_statistics
bootstrap, sigma_vector_1_statistics, sigma_vector_2_statistics, sigma_vector_3_statistics = btstrp(or_str1,or_dip1,or_rak1,or_str2,or_dip2,or_rak2,origin)


# ========================================================================================
# ------------------------------------------------
# save result
# ------------------------------------------------
# make function
def confidence_data(data):
    import numpy as np
    import unify_direction as ud
    
    dat, tempo = ud.unifying_direction(data)

    # calculate error
    mean_of_all_data = np.mean(tempo)
    stdev = np.std(tempo)
    percentil = ud.percentil(tempo)
    half_of_95_percentil = np.float64((np.percentile(tempo, 97.5)-np.percentile(tempo, 2.5))/2)
    data_in_percentil_range = [x for x in tempo if np.percentile(tempo, 2.5) <= x <= np.percentile(tempo, 97.5)]
    mean_of_ci95_data = np.mean(data_in_percentil_range)
    stdev_of_ci95 = np.std(data_in_percentil_range)
    result = pd.DataFrame(np.array([[mean_of_all_data, stdev, mean_of_ci95_data, stdev_of_ci95, np.float64(percentil[0]), np.float64(percentil[1]), half_of_95_percentil]]),
                            columns=["mean of all data","stdev","mean of ci95 data","stdev of ci95","2.5%","97.5%","half width 95% percentil"])
    return result

# store error to data frame
error = pd.concat([confidence_data(bootstrap["azimuth sigma 1"]), confidence_data(bootstrap["plunge sigma 1"]), 
                   confidence_data(bootstrap["azimuth sigma 2"]), confidence_data(bootstrap["plunge sigma 2"]), 
                   confidence_data(bootstrap["azimuth sigma 3"]), confidence_data(bootstrap["plunge sigma 3"]), 
                   confidence_data(bootstrap["SHmax"]), confidence_data(bootstrap["shape ratio"]),
                   confidence_data(bootstrap["simpson index"])])

if output == 1 or output == 4:
    # export to csv
    origin.drop([1]).to_csv(output_file + "output_origin.csv", index=False); print('file origin tersimpan')
    bootstrap.to_csv(output_file + "output_bootstarap.csv", index=False); print('file bootstrap tersimpan')
    error.insert(0, "value", ["Sigma1 Azimuth", "Sigma1 Plunge",\
                            "Sigma2 Azimuth", "Sigma2 Plunge",\
                            "Sigma3 Azimuth", "Sigma3 Plunge",\
                            "SHmax", "Shape Ratio",
                            "simpson index"])
    error.to_csv(output_file + "output_error.csv", index=False); print('file error tersimpan')
elif output == 2:
    print(origin.drop([1]))
    print(bootstrap)
    print(error)
elif output == 3:
    error.to_csv("/mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Output/statistic_error.csv", index=False)
else:
    print("You don't define the output option")

# ========================================================================================
# ------------------------------------------------
# plot result
# ------------------------------------------------
# make function
def histo(title, data, plot, bin = 25):
    import statistics as sts
    import unify_direction as ud

    result, tempo = ud.unifying_direction(data)

    #bin: 
    # "az" for azimuth or SHmax, 
    # "pl" for plunge, and 
    # "sr" for shape ratio
    mode = sts.mode(data)
    if bin == "az":
        bin = np.arange(mode-90, mode+90, 4)
    elif bin == "pl":
        bin = np.arange(0, 90, 2)
    elif bin == "sr":
        bin = np.arange(0+0.0125, 1, 0.025)
    elif bin == "ar":
        bin = np.arange(0, 3, 0.075)
    
    if plot == 3:
        pass
    else:
        pltHist, axH = plt.subplots()
        n, bins, patches = axH.hist(x = tempo, bins = bin, color='#0504aa', alpha = 0.7, rwidth=0.85)
        axH.set_title(title, fontsize = 14)
        axH.grid(True)
        if plot == 1:
            plt.show()
        elif plot == 2:
            plt.savefig(output_file + "{}.png".format(title))
            print('plot {} tersimpan'.format(title))

histo("Azimuth Sigma 1", bootstrap["azimuth sigma 1"], plot, "az")
histo("Plunge sigma 1", bootstrap["plunge sigma 1"], plot, "pl")
histo("Azimuth Sigma 2", bootstrap["azimuth sigma 2"], plot, "az")
histo("Plunge sigma 2", bootstrap["plunge sigma 2"], plot, "pl")
histo("Azimuth Sigma 3", bootstrap["azimuth sigma 3"], plot, "az")
histo("Plunge sigma 3", bootstrap["plunge sigma 3"], plot, "pl")
histo("SHmax", bootstrap["SHmax"], plot, "az")
histo("Shape Ratio", bootstrap["shape ratio"], plot, "sr")
histo("Simpson Index", bootstrap["simpson index"], plot, "ar")

# ----------------------------------------------------------------------------------------
# P/T axes and the optimum principal stress axes
import plot_stress as plots
plots.plot_stress(1,strike,dip,rake,plot,output_file)

# ----------------------------------------------------------------------------------------
# confidence limiuts of the principal stress axes
import plot_stress_axes as plotsa
plotsa.plot_stress_axes(sigma_vector_1_statistics, sigma_vector_2_statistics, sigma_vector_3_statistics, plot,output_file)