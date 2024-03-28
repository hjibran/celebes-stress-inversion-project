import os
parameter = [
    (0.30, 10),
    (0.35, 10),
    (0.40, 10),
    (0.45, 10),
    (0.50, 10),
    (0.55, 10)
]

i = 0
while i < len(parameter):
    eps, min = parameter[i]
    print(eps,min)
    os.system("python3 /mnt/d/celebes-stress-inversion-project/script/clustering.py {} {}".format(eps, min))
    i += 1






