import os
import pandas as pd

print("Start running to calculate simpson index bootstrap per cluster")

epsilons = ["0.40"]

for epsilon in epsilons:
    table = pd.read_csv("/mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Output/eps{}pts15/new_shmax/z_statistic_error.csv".format(epsilon))
    seed = table["best seed"]
    clss = range(10)
    for cls in clss:
        os.system("python3 /mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Programs_PYTHON/stress-inversion-with-bootstrap.py {} {} {}".format(epsilon, cls, int(seed[cls])))
        print("epsilon{}, cluster {} done".format(epsilon, cls))