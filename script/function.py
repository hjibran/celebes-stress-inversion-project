# This is where new functions used in calculations are stored
     
def unifying_direction(data):
    '''fungsi ini dibuat untuk mengembalikan azimut yang terbalik 180 derajat dari rata-rata hasil inversi'''

    import statistics as sts
    from matplotlib import pyplot as plt
    
    median = sts.median(data)
    up = median + 90
    down = median - 90
    if up > 350:
        up = up - 360
        bottom_part = [x for x in data if x < up]
        midle_part = [x+180 for x in data if down < x < up]
        upper_part = [x for x in data if x > down]
        temp = bottom_part + midle_part + upper_part
    elif down < 0:
        down = down + 360
        bottom_part = [x for x in data if x < up]
        midle_part = [x-180 for x in data if down < x < up]
        upper_part = [x for x in data if x > down]
        temp = bottom_part + midle_part + upper_part
    else:
        bottom_part = [x+180 for x in data if x < down]
        midle_part = [x for x in data if down < x < up]
        upper_part = [x-180 for x in data if x > up]
        temp = bottom_part + midle_part + upper_part
    
    plt.hist(temp, 350)
    plt.show()
    
    indegree = [x for x in temp if 0 <= x <= 360]
    belowdegree = [x+360 for x in temp if x < 0]
    upperdegree = [x-360 for x in temp if x > 360]
    result = upperdegree + indegree + belowdegree
    result.sort()
    return result

#print(unifying_direction.__doc__)

Q1 = [359, 360, 360, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 3, 3, 4, 181, 180, 182, 181, 182, 180, 181]
Q2 = []


from matplotlib import pyplot as plt
plt.hist(Q1, 350)
plt.show()

newQ1 =unifying_direction(Q1)
plt.hist(newQ1, 350)
plt.show()

print(Q1)
print(newQ1)