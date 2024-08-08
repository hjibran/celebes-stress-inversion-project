# This is where new functions used in calculations are stored
     
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

def percentil(data):
    import numpy as np
    value = np.percentile(data, [2.5, 97.5])
    if value[0] < 0:
        value[0] += 360
    elif value[1] > 360:
        value[1] -= 360
    return value



#print(unifying_direction.__doc__)

#Q1 = [359, 360, 360, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 3, 3, 4, 181, 180, 182, 181, 182, 180, 181, 179, 178, 183, 184]
#Q2 = []


#from matplotlib import pyplot as plt
#plt.hist(Q1, 359)
#plt.show()

#print(Q1)

#newQ1 =unifying_direction(Q1)
#plt.hist(newQ1, 350)
#plt.show()

#print(newQ1)

#def rad_360(data):
#    import numpy as np
#    radians = np.linspace(0, ((2*np.pi)-(np.pi/180)), 360)
#    tinggi = []
#    for i in range(360):
#        if i == 0:
#            temp1 = [x for x in data if x < 0.5]
#            temp2 = [x for x in data if 359.5 < x]
#            n = len(temp1)+len(temp2)
#        else:
#            temp = [x for x in data if i-0.5 < x < i+0.5]
#            n = len(temp)
#        tinggi.append(n)
#    ax = plt.subplot(projection='polar')
#    ax.bar(radians, tinggi, width = np.pi/180)

#rad_360(Q1)
#rad_360(newQ1)
#plt.show()
