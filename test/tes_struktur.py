import pygmt

fig = pygmt.Figure()
fig.coast(region=[114, 130, -10, 7],
          projection='M20c',
          land='gray')

fig.plot(data='/mnt/d/celebes-stress-inversion-project/data/GMT_Seismotectonics_of_Sulawesi/trench.gmt')
#fig.plot(data='/mnt/d/celebes-stress-inversion-project/data/GMT_Seismotectonics_of_Sulawesi/indonesiafaults.gmt')
fig.show()