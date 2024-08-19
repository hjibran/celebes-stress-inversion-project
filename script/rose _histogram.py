def rose_histogram(cluster, azsh, azimuth=1):
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd

    data = pd.read_csv("/mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Output/cluster{}/output_bootstarap.csv".format(cluster))
    
    if azsh == "azimuth":
        azm = data["azimuth sigma {}".format(azimuth)]
        rad = azm / 180 * np.pi
    elif azsh == "shmax":
        shmax = data["SHmax"]
        rad = shmax / 180 * np.pi

    fig, ax = plt.subplots(figsize=(8,8), subplot_kw=dict(polar=True))
    ax.set_theta_direction('clockwise')
    ax.set_theta_zero_location('N')

    ax.hist(x = rad, bins = 90)

    #print("azimuth sigma {} cluster {}".format(azimuth, cluster))
    print("cluster {}".format(cluster))
    plt.show()

cluster = 0
while cluster <= 9:
    rose_histogram(cluster, "shmax")

    #azimut = 1
    #while azimut <=3:
    #    rose_histogram(cluster, azimut)
    #    azimut+=1

    cluster+=1

print("done")