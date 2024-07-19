import numpy as np


my_list = [1, 5, 3, 8, 2, 7, 4, 6]
result = [x for x in my_list if 9 < x < 12]
print(len(result))


radians = np.linspace(0, ((2*np.pi)-(np.pi/180)), 360)
print(np.pi/180)
print(np.pi/180/2)