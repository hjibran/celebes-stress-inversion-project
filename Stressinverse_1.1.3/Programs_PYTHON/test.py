import pandas as pd
import numpy as np

zero = np.zeros((3))
data = np.array([[1, 3.4, 3], [4, 'a', 6], [7, 8, 9]])
df2 = pd.DataFrame(data, columns=['a', 'b', 'c'])

#zero[2] = 1
print(zero)