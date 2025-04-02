#!/home/haidir/celebes-stress-inversion-project/venv/bin/python3


# import module
import pygmt
import numpy as np
import matplotlib.pyplot as plt

def delta_theta(stress_drop, theta):
    st = stress_drop
    t = np.deg2rad(theta)
    dt = np.rad2deg(np.arctan(((1)-(st*np.sin(2*t))-np.sqrt((st**2)+(1)-(2*st*np.sin(2*t))))/(st*np.cos(2*t))))
    return dt

def stress_drop(t, dt):
    st = -np.sin(2*np.deg2rad(dt))/np.cos((2*np.deg2rad(t))+(2*np.deg2rad(dt)))
    return st

theta_min = np.arange(0,45,0.1)
theta_plus = np.arange(45.1,180,0.1)
theta = np.concatenate((theta_min,theta_plus))

for i in [-1, -0.8, -0.6, -0.4, -0.2, 0.2, 0.4, 0.6, 0.8, 1]:
    delta_th = [delta_theta(i, x) for x in theta]
    plt.plot(theta,delta_th,'darkgray')
    plt.text(80, delta_th[800], str(i), fontsize=10)

plt.plot(55.53, 13.73, 'ro')
plt.plot(90.76, 6.17,'mo')
plt.plot(54.48, 16.36,'bo')

plt.xlim(0,100)
plt.ylim(-50,50)
plt.show()