def histo(title, data, plot, output_file, bin = 25):
    import matplotlib.pyplot as plt
    import numpy as np
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
            plt.savefig(output_file + "{} 0.075 Interval.png".format(title))

import pandas as pd

for cls in range(10):
    print("class {}".format(cls))
    output_file = "/mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Output/eps0.50pts15/cls{}/".format(cls)
    bootstrap = pd.read_csv("/mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Output/eps0.50pts15/cls{}/output_bootstarap.csv".format(cls))
    histo("Simpson Index", bootstrap["simpson index"], 2, output_file, "ar")