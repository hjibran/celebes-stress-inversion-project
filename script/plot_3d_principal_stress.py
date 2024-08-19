
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle
import mpl_toolkits.mplot3d.art3d as art3d
import pandas as pd

data = pd.read_csv("/mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Output/cluster0/output_bootstarap.csv")

ax = plt.figure().add_subplot(projection='3d')
#p = Circle((0,0), 1, edgecolor="black", color="white")
#ax.add_patch(p)
#art3d.pathpatch_2d_to_3d(p, z=-1.5, zdir="z")

def vector3d(azimuth, plunge, color):
    X = np.cos(np.radians(plunge))*np.sin(np.radians(azimuth))
    Y = np.cos(np.radians(plunge))*np.cos(np.radians(azimuth))
    Z = -np.sin(np.radians(plunge))

    for i in range(len(X)):
        ax.plot([0,X[i],], [0,Y[i]], [0,Z[i]], color=color)
        ax.plot([0,-X[i],], [0,-Y[i]], [0,-Z[i]], color=color)
        ax.scatter(X[i], Y[i], -1.5, color=color)
        ax.scatter(-X[i], -Y[i], -1.5, color=color)

#azimuth = np.arange(-5, 95, 5)
#plunge = 87
#
#vector3d(azimuth, np.full(len(azimuth), plunge), "red")

vector3d(data["azimuth sigma 1"], data["plunge sigma 1"], "red")
vector3d(data["azimuth sigma 2"], data["plunge sigma 2"], "green")
vector3d(data["azimuth sigma 3"], data["plunge sigma 3"], "blue")

ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_zlim(-1.5, 1.5)
ax.set_xlabel("west-east")
ax.set_ylabel("south-north")
ax.set_zlabel("down-up")

plt.show()