# ----------------------------------------------------------------#
# this code was created to determine the seed value that          # 
# will be used in each cluster                                    #
# the best seed is the seed with  mean standar deviation          #
# ----------------------------------------------------------------#
import os
import numpy as np
import pandas as pd
import sys

print("started running at:")
str(os.system("date"))

result = np.zeros([10, 3])
cluster = 0
while cluster <= 9:
    print("on progress for cluster {}".format(cluster))

    mean_std_seed = np.zeros([50, 3])
    seed = 1
    while seed <= 50:
        print("on progress for cluster {} seed {}".format(cluster, seed))
        str(os.system("date"))

        os.system("/home/haidir/celebes-stress-inversion-project/bin/python3.10\
                   /mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Programs_PYTHON/stress-inversion-with-bootstrap-for-error.py {} {}".format(cluster, seed))

        #print("we are still on progress")
        data = pd.read_csv("/mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Output/statistic_error.csv")
        mean_std = np.mean(data["stdev"])
        mean_std_seed[seed-1][0] = cluster
        mean_std_seed[seed-1][1] = seed
        mean_std_seed[seed-1][2] = mean_std

        print("cluster {} seed {} done".format(cluster, seed))
        seed +=1
    
    def mini(store):
        mini = np.min(store, axis=0)
        where = np.where(store == mini[2])
        index = where[0][0]
        minim = store[index]
        return minim
    
    result[cluster] = mini(mean_std_seed)
    print("cluster {} done".format(cluster))
    cluster += 1

result = pd.DataFrame(result, columns=["cluster", "best seed", "mean stdev"])
result.to_csv("/mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Output/statistic_error.csv")

print("finished running at:")
time2 = str(os.system("date"))
print("thank you")