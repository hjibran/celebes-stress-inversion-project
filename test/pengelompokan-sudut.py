import numpy as np
import random
from matplotlib import pyplot as plt
import sys
strinv_dir = '/mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Programs_PYTHON'
if not strinv_dir in sys.path:
    sys.path.append(strinv_dir)

def bootstrap(list, banyak_sebaran_hasil):
    rerata = []
    for i in range(banyak_sebaran_hasil):
        idxs_boot = np.array([random.randint(0, len(list)-1) for i in range(len(list))])
        temp = [list[x] for x in idxs_boot]
        rerata.append(sum(temp)/len(temp))
    return rerata


sigma = 1
Q1=(bootstrap(np.arange(sigma-5, sigma+5+0.0000001, 1), 2500))
q1a = [x+360 for x in Q1 if x < 0]
q1b = [x for x in Q1 if x > 0]
q1 = q1a+q1b+(bootstrap(np.arange(181-5, 181+5+0.0000001, 1), 400))

def unifying_direction(data):
    import statistics as sts
    
    median = sts.median(data)
    up = median + 90
    down = median - 90
    if up > 350:
        up = up - 360
        bottom_part = [x for x in data if x < up]
        midle_part = [x+180 for x in data if down < x < up]
        upper_part = [x for x in data if x > down]
        result = bottom_part + midle_part + upper_part
        result.sort()
        return result
    elif down < 0:
        down = down + 360
        bottom_part = [x for x in data if x < up]
        midle_part = [x-180 for x in data if down < x < up]
        upper_part = [x for x in data if x > down]
        result = bottom_part + midle_part + upper_part
        result.sort()
        return result
    else:
        bottom_part = [x+180 for x in data if x < down]
        midle_part = [x for x in data if down < x < up]
        upper_part = [x-180 for x in data if x > up]
        result = bottom_part + midle_part + upper_part
        result.sort()
        return result

result = unifying_direction(q1)

import numpy as np
conint = np.percentile(result, [2.5, 97.5])
print(conint)

import confidence_interval as ci
print(ci.confidence_interval(result))

plt.hist(result, bins = 360)
#plt.hist(q1, bins = 360)
y = np.linspace(0,30)
x = [conint for i in y]
plt.plot(x,y)
plt.show()