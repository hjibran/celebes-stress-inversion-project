import numpy as np
import pandas as pd

def mean(up, down):
    return ((up+down)/2)

def regime(value):
    if value < 0.25:
        reg = "RdEx"
    elif value < 0.75:
        reg = "PrEx"
    elif value < 1.25:
        reg = "TrTn"
    elif value < 1.75:
        reg = "PrSS"
    elif value < 2.25:
        reg = "TrPr"
    elif value < 2.75:
        reg = "PrCm"
    else:
        reg = "RdCm"

    return reg
print("                              Minimum Point: 15, Epsilon: 0.40                              ")
print("|------------------------------------------------------------------------------------------|")
print("| Simpson tanpa bootstrap | Simpson dengan bootstrap | Simpson dengan bootstrap modifikasi |")
print("|-------------------------|--------------------------|-------------------------------------|")

for cls in range(10):
    data_simpson_modifikasi_bootstrap = pd.read_csv("/mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Output/eps0.40pts15/new_shmax/cls{}/output_error_with_simpson.csv".format(cls))
    data_simpson_dengan_bootstrap = pd.read_csv("/mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Output/eps0.40pts15/new_shmax/cls{}/output_error.csv".format(cls))
    data_simpson_tanpa_bootstrap = pd.read_csv("/mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Output/eps0.40pts15/new_shmax/cls{}/output_origin.csv".format(cls))

    mean_simpson_dengan_bootstrap = mean(data_simpson_dengan_bootstrap["97.5%"][8],data_simpson_dengan_bootstrap["2.5%"][8])
    mean_simpson_modifikasi_bootstrap = mean(data_simpson_modifikasi_bootstrap["97.5%"][8],data_simpson_modifikasi_bootstrap["2.5%"][8])

    print("|       {:.2f} ({})       |    {:.2f} \u00B1 {:.2f} ({})    |          {:.2f} \u00B1 {:.2f} ({})         |".format(\
        data_simpson_tanpa_bootstrap["simpson index"][0],
        regime(data_simpson_tanpa_bootstrap["simpson index"][0]),
        mean_simpson_dengan_bootstrap,
        data_simpson_dengan_bootstrap["half width 95% percentil"][8],
        regime(mean_simpson_dengan_bootstrap),
        mean_simpson_modifikasi_bootstrap,
        data_simpson_modifikasi_bootstrap["half width 95% percentil"][8],
        regime(mean_simpson_modifikasi_bootstrap)))

print("|------------------------------------------------------------------------------------------|")

print("Keterangan:")
print("RdEx = Radial Extention\
     \nPrEx = Pure Extention\
     \nTrTn = Trans Tensive\
     \nPrSS = Pure Strike Slip\
     \nTrPr = Trans Pressive\
     \nPrCm = Pure Compressive\
     \nRdCm = Radial Compressive")