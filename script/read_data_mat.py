#!/home/haidir/celebes-stress-inversion-project/venv/bin/python3
import scipy.io
import pandas as pd
import numpy as np

kelas = 9

mat = scipy.io.loadmat("/mnt/d/celebes-stress-inversion-project/Result/stressinversewithbootstrap/kelas0/output_drs.mat")#input("Masukkan path file mat yang ingin dilihat:\n"))

print(mat)