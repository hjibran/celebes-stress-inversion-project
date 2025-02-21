import numpy as np
import pandas as pd
import os

def unifying_direction(data):
    '''fungsi ini dibuat untuk mengembalikan azimut yang terbalik 180 derajat dari rata-rata hasil inversi'''
    import statistics as sts
    from matplotlib import pyplot as plt
    
    mode = sts.mode(data)
    up = mode + 90
    down = mode - 90
    if up > 350:
        up = up - 360
        bottom_part = [x for x in data if x < up]
        midle_part = [x+180 for x in data if up < x < down]
        upper_part = [x for x in data if x > down]
        temp = bottom_part + midle_part + upper_part
    elif down < 0:
        down = down + 360
        bottom_part = [x for x in data if x < up]
        midle_part = [x-180 for x in data if up < x < down]
        upper_part = [x for x in data if x > down]
        temp = bottom_part + midle_part + upper_part
    else:
        bottom_part = [x+180 for x in data if x < down]
        midle_part = [x for x in data if down < x < up]
        upper_part = [x-180 for x in data if x > up]
        temp = bottom_part + midle_part + upper_part
    
    indegree = [x for x in temp if 0 <= x <= 360]
    belowdegree = [x+360 for x in temp if x < 0]
    upperdegree = [x-360 for x in temp if x > 360]
    result = upperdegree + indegree + belowdegree
    result.sort()

    if mode < 180:
        temp1 = [x for x in result if x < mode+90]
        temp2 = [x-360 for x in result if x > mode+90]
        tempo = temp1 + temp2
    elif mode > 180:
        temp1 = [x+360 for x in result if x < mode-90]
        temp2 = [x for x in result if x > mode-90]
        tempo = temp1 + temp2

    return result, tempo

def percentil_calc(data):
    import numpy as np

    value = np.percentile(data, [2.5, 97.5])
    if value[0] < 0:
        value[0] += 360
    elif value[1] > 360:
        value[1] -= 360
    return value

def confidence_data(data):
    import numpy as np
    
    dat, tempo = unifying_direction(data)

    # calculate error
    percentil = percentil_calc(tempo)
    half_of_95_percentil = np.float64((np.percentile(tempo, 97.5)-np.percentile(tempo, 2.5))/2)
    result = pd.DataFrame(np.array([[np.float64(percentil[0]), np.float64(percentil[1]), (percentil[0]+percentil[1])/2, half_of_95_percentil]]),
                            columns=["2.5%","97.5%", "middle value","+-"])
    return result

matrix = np.zeros([30,18])
cluster_file=["/mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Output/eps0.35pts15", "/mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Output/eps0.40pts15/new_shmax", "/mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Output/eps0.50pts15"]
lonlat_file=["/mnt/d/celebes-stress-inversion-project/Result/eps0.35min15-final/clustered", "/mnt/d/celebes-stress-inversion-project/Result/eps0.40min15-final/clustered", "/mnt/d/celebes-stress-inversion-project/Result/eps0.50min15-final/clustered"]
parameter = [15.35, 15.40, 15.50]

os.system("echo ")

i=0
for file in range(len(cluster_file)):
    for clus in range(10):
        data_bootstrap = pd.read_csv(cluster_file[file]+"/cls{}/output_bootstarap.csv".format(clus))
        data_cluster = pd.read_csv(lonlat_file[file]+"/cls{}.csv".format(clus))
        str1 = confidence_data(data_bootstrap["principal strike 1"])
        dip1 = confidence_data(data_bootstrap["principal dip 1"])
        rake1 = confidence_data(data_bootstrap["principal rake 1"])
        str2 = confidence_data(data_bootstrap["principal strike 2"])
        dip2 = confidence_data(data_bootstrap["principal dip 2"])
        rake2 = confidence_data(data_bootstrap["principal rake 2"])
        tau11 = confidence_data(data_bootstrap["tau11"])
        tau12 = confidence_data(data_bootstrap["tau12"])
        tau13 = confidence_data(data_bootstrap["tau13"])
        tau22 = confidence_data(data_bootstrap["tau22"])
        tau23 = confidence_data(data_bootstrap["tau23"])
        tau33 = confidence_data(data_bootstrap["tau33"])
        shmax = confidence_data(data_bootstrap["SHmax"])
        lon = data_cluster["lon"];mean_longitude = np.mean(lon)
        lat = data_cluster["lat"];mean_latitude = np.mean(lat)

        tau = np.zeros([3,3])
        tau[0][0] = float(tau11["middle value"].iloc[0]); tau[0][1] = float(tau12["middle value"].iloc[0]); tau[0][2] = float(tau13["middle value"].iloc[0])
        tau[1][0] = float(tau12["middle value"].iloc[0]); tau[1][1] = float(tau22["middle value"].iloc[0]); tau[1][2] = float(tau23["middle value"].iloc[0])
        tau[2][0] = float(tau13["middle value"].iloc[0]); tau[2][1] = float(tau23["middle value"].iloc[0]); tau[2][2] = float(tau33["middle value"].iloc[0])
        sigma = np.sort(np.linalg.eigvals(tau))
        shape_ratio = (sigma[1]-sigma[0])/(sigma[2]-sigma[0])

        if  i == 0:
            os.system("echo {} {} {} {} {} {} {} X Y {} > /mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Output/tmp".format(mean_longitude, mean_latitude, "10", float(str1["middle value"].iloc[0]), float(dip1["middle value"].iloc[0]), float(rake1["middle value"].iloc[0]), "4.0", i))
        else:
            os.system("echo {} {} {} {} {} {} {} X Y {} >> /mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Output/tmp".format(mean_longitude, mean_latitude, "10", float(str1["middle value"].iloc[0]), float(dip1["middle value"].iloc[0]), float(rake1["middle value"].iloc[0]), "4.0", i))

        os.system("python3 /mnt/d/celebes-stress-inversion-project/FMC-master/FMC.py /mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Output/tmp -i AR > /mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Output/result")

        matrix[i][0] = parameter[file]; matrix[i][1] = float(clus); matrix[i][2] = mean_longitude; matrix[i][3] = mean_latitude 
        matrix[i][4] = 10.0; matrix[i][11] = 4.0; matrix[i][12] = float(shmax["2.5%"].iloc[0]); matrix[i][13] = float(shmax["97.5%"].iloc[0]); matrix[i][14] = shape_ratio
        matrix[i][5] = float(str1["middle value"].iloc[0]); matrix[i][6] = float(dip1["middle value"].iloc[0]); matrix[i][7] = float(rake1["middle value"].iloc[0])
        matrix[i][8] = float(str2["middle value"].iloc[0]); matrix[i][9] = float(dip2["middle value"].iloc[0]); matrix[i][10] = float(rake2["middle value"].iloc[0])

        i += 1

table = pd.DataFrame(matrix, columns=["name", "cluster", "lon", "lat", "depth", "strike1", "dip1", "rake1", "strike2", "dip2", "rake2", "Mw", "down", "up", "R", "type", "K", "AR"])
result = pd.read_csv("/mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Output/result", sep='\s+')
type = result['rupture_type']

table['type'] = table['type'].astype('string')
for i in range(len(type)):
    table.iloc[i, 15] = type[i]

    R = table.iloc[i, 14]
    if type[i] == "N":
        k = 0
        AR = (k+0.5)+((-1**k)*(R-0.5))
        table.iloc[i, 16] = k
        table.iloc[i, 17] = AR

    elif type[i] == "N-SS":
        k = 0
        AR = (k+0.5)+((-1**k)*(R-0.5))
        table.iloc[i,16] = k
        table.iloc[i, 17] = AR

    elif type[i] == "SS-N":
        k = 1
        AR = (k+0.5)+((-1**k)*(R-0.5))
        table.iloc[i,16] = k
        table.iloc[i, 17] = AR

    elif type[i] == "SS":
        k = 1
        AR = (k+0.5)+((-1**k)*(R-0.5))
        table.iloc[i,16] = k
        table.iloc[i, 17] = AR

    elif type[i] == "SS-R":
        k = 1
        AR = (k+0.5)+((-1**k)*(R-0.5))
        table.iloc[i,16] = k
        table.iloc[i, 17] = AR

    elif type[i] == "R-SS":
        k = 2
        AR = (k+0.5)+((-1**k)*(R-0.5))
        table.iloc[i,16] = k
        table.iloc[i, 17] = AR

    elif type[i] == "R":
        k = 2
        AR = (k+0.5)+((-1**k)*(R-0.5))
        table.iloc[i,16] = k
        table.iloc[i, 17] = AR
    
os.system("rm /mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Output/tmp /mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Output/result")

table.to_csv("/mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Output/shmax.csv", index=False)