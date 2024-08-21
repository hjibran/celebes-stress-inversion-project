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
output = 3
if output == 3:
    input_file = "/mnt/d/celebes-stress-inversion-project/Result/eps0.40min15/stressinverse/data/cls{}.dat".format(sys.argv[1])
    seed = int(sys.argv[2])
else:
    # path to file input, file output, and seed (to initialize random bootstrap)
    input_file = r"/mnt/d/celebes-stress-inversion-project/Result/eps0.40min15/stressinverse/data/cls9.dat"
    output_file = r"/mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Output/output"
    seed = 36

# plot option
    # plot with plt.show(): 1
    # save to picture file: 2
    #  don't plot anything: 3
plot = 3

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
def run(str1,dip1,rak1,str2,dip2,rak2,
        friction_min=friction_min,friction_max=friction_max,friction_step=friction_step,
        N_iterations=N_iterations,N_realizations=N_realizations):
    
    # ----------------------------------------------------------------------------------------
    # inversion for stress
    import stress_inversion as si
    tau_optimum,shape_ratio,strike,dip,rake,instability,friction = si.stress_inversion(
        str1,dip1,rak1,str2,dip2,rak2,
        friction_min,friction_max,friction_step,N_iterations,N_realizations)
    # ----------------------------------------------------------------------------------------
    # optimum principal stress axes
    import azimuth_plunge as ap

    direction_sigma_1, direction_sigma_2, direction_sigma_3 = ap.azimuth_plunge(tau_optimum)
    sg1_azm = direction_sigma_1[0]; sg1_pln  = direction_sigma_1[1]
    sg2_azm = direction_sigma_2[0]; sg2_pln  = direction_sigma_2[1]
    sg3_azm = direction_sigma_3[0]; sg3_pln  = direction_sigma_3[1]

    # ----------------------------------------------------------------------------------------
    # SHmax
    import SHmax_calc as sh
    shmax = sh.shmax_dir(sg1_azm,sg1_pln,sg2_azm,sg2_pln,shape_ratio,True)

    # ----------------------------------------------------------------------------------------
    # return the value
    return sg1_azm, sg1_pln, sg2_azm, sg2_pln, sg3_azm, sg3_pln,\
            shape_ratio, friction[0], shmax


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
    import pandas as pd
    import numpy as np

    # run the stress inversion with origin data
    org = np.zeros((2, 21))
    org[0][6], org[0][7], org[0][8], org[0][9], org[0][10], org[0][11],\
        org[0][12], org[0][13], org[0][14],\
        = run(or_str1,or_dip1,or_rak1,or_str2,or_dip2,or_rak2)

    # make a data frame for stress inversion output
    origin = pd.DataFrame(org, columns=
        ["tau11", "tau12", "tau13", "tau22", "tau23", "tau33",
        "azimuth sigma 1", "plunge sigma 1", "azimuth sigma 2", "plunge sigma 2", "azimuth sigma 3", "plunge sigma 3",
        "shape ratio", "friction", "SHmax",
        "principal strike 1", "principal dip 1", "principal rake 1",
        "principal strike 2", "principal dip 2", "principal rake 2"])

    # return the data frame
    return origin
origin = orgn(or_str1,or_dip1,or_rak1,or_str2,or_dip2,or_rak2)

# ----------------------------------------------------------------------------------------
# data with bootstrap
# make function
def btstrp(or_str1,or_dip1,or_rak1,or_str2,or_dip2,or_rak2):
    import numpy as np
    import pandas as pd
    from random import choice
    np.random.seed(seed)

    # make bootstrap data
    boots = np.zeros((N_bootstrap, 21))    
    idxs = [i for i in range(len(or_str1))]
    for i in range(N_bootstrap):
        idxs_boot = np.array([np.random.randint(0, len(or_str1)) for i in range(len(or_str1))])
        bt_str1 = or_str1[idxs_boot]
        bt_dip1 = or_dip1[idxs_boot]
        bt_rak1 = or_rak1[idxs_boot]
        bt_str2 = or_str2[idxs_boot]
        bt_dip2 = or_dip2[idxs_boot]
        bt_rak2 = or_rak2[idxs_boot]

        # run the stress inversion with origin data
        boots[i][6], boots[i][7], boots[i][8], boots[i][9], boots[i][10], boots[i][11],\
            boots[i][12], boots[i][13], boots[i][14],\
            = run(bt_str1,bt_dip1,bt_rak1,bt_str2,bt_dip2,bt_rak2)
  
    # make a data frame for stress inversion output
    bootstrap = pd.DataFrame(boots, columns=
        ["tau11", "tau12", "tau13", "tau22", "tau23", "tau33",
        "azimuth sigma 1", "plunge sigma 1", "azimuth sigma 2", "plunge sigma 2", "azimuth sigma 3", "plunge sigma 3",
        "shape ratio", "friction", "SHmax",
        "principal strike 1", "principal dip 1", "principal rake 1",
        "principal strike 2", "principal dip 2", "principal rake 2"])
    
    # return the data frame
    return bootstrap
bootstrap = btstrp(or_str1,or_dip1,or_rak1,or_str2,or_dip2,or_rak2)


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
                   confidence_data(bootstrap["SHmax"]), confidence_data(bootstrap["shape ratio"])])

if output == 1:
    # export to csv
    origin.drop([1]).to_csv(output_file + "_origin.csv", index=False)
    bootstrap.to_csv(output_file + "_bootstarap.csv", index=False)
    error.insert(0, "value", ["Sigma1 Azimuth", "Sigma1 Plunge",\
                            "Sigma2 Azimuth", "Sigma2 Plunge",\
                            "Sigma3 Azimuth", "Sigma3 Plunge",\
                            "SHmax", "Shape Ratio"])
    error.to_csv(output_file + "_error.csv", index=False)
elif output == 2:
    print(origin.drop([1]))
    print(bootstrap)
    print(error)
elif output == 3:
    error.to_csv("/mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Output/statistic_error.csv", index=False)
else:
    print("You don't define the output option")