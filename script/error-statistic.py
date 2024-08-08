import os
import sys
cluster = int(sys.argv[1])
iterasi_seed = 50

print("seed,azimut1,error,plunge1,error,azimut2,error,plunge2,error,azimut3,error,plunge3,error,shaperatio,error")

def run(cluster,seed):
    os.system("python3 /mnt/d/celebes-stress-inversion-project/script/StressInvBot-copy.py {} {}".format(cluster, seed))

for i in range(iterasi_seed):
    run(cluster, int(i))

