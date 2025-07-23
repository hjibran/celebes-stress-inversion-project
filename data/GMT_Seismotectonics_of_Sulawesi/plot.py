import pygmt
import geopandas as gpd

boundary = gpd.read_file("/mnt/d/celebes-stress-inversion-project/data/Soquet2006/soquet2006plateboundary(LN).shp")

fig = pygmt.Figure()

fig.coast(projection = 'M10c',
          region = [117,130,-9, 5],
          water = 'white',
          shorelines = 'gray'
          )

#fig.plot(data=boundary, pen="0.5p,red", label="microblock (Soquet, 2006)")

#fig.plot('/mnt/d/celebes-stress-inversion-project/data/GMT_Seismotectonics_of_Sulawesi/batuithrust.gmt')
#fig.plot('/mnt/d/celebes-stress-inversion-project/data/GMT_Seismotectonics_of_Sulawesi/butonthrust.gmt')
#fig.plot('/mnt/d/celebes-stress-inversion-project/data/GMT_Seismotectonics_of_Sulawesi/cs.gmt')
#fig.plot('/mnt/d/celebes-stress-inversion-project/data/GMT_Seismotectonics_of_Sulawesi/dashed.gmt')
#fig.plot('/mnt/d/celebes-stress-inversion-project/data/GMT_Seismotectonics_of_Sulawesi/dashed1.gmt')
#fig.plot('/mnt/d/celebes-stress-inversion-project/data/GMT_Seismotectonics_of_Sulawesi/faultsulawesi.gmt')
#fig.plot('/mnt/d/celebes-stress-inversion-project/data/GMT_Seismotectonics_of_Sulawesi/faultsulawesi1.gmt')
#fig.plot('/mnt/d/celebes-stress-inversion-project/data/GMT_Seismotectonics_of_Sulawesi/gorotaloextension.gmt')
#fig.plot('/mnt/d/celebes-stress-inversion-project/data/GMT_Seismotectonics_of_Sulawesi/hal_dip.gmt')
#fig.plot('/mnt/d/celebes-stress-inversion-project/data/GMT_Seismotectonics_of_Sulawesi/hal_dip1.gmt')
#fig.plot('/mnt/d/celebes-stress-inversion-project/data/GMT_Seismotectonics_of_Sulawesi/hf.gmt')
#fig.plot('/mnt/d/celebes-stress-inversion-project/data/GMT_Seismotectonics_of_Sulawesi/jd.gmt')
#fig.plot('/mnt/d/celebes-stress-inversion-project/data/GMT_Seismotectonics_of_Sulawesi/jd1.gmt')
#fig.plot('/mnt/d/celebes-stress-inversion-project/data/GMT_Seismotectonics_of_Sulawesi/kendarihamilton.gmt')
#fig.plot('/mnt/d/celebes-stress-inversion-project/data/GMT_Seismotectonics_of_Sulawesi/law.gmt')
#fig.plot('/mnt/d/celebes-stress-inversion-project/data/GMT_Seismotectonics_of_Sulawesi/law1.gmt')
#fig.plot('/mnt/d/celebes-stress-inversion-project/data/GMT_Seismotectonics_of_Sulawesi/line1.gmt')
#fig.plot('/mnt/d/celebes-stress-inversion-project/data/GMT_Seismotectonics_of_Sulawesi/mamasa.gmt')
#fig.plot('/mnt/d/celebes-stress-inversion-project/data/GMT_Seismotectonics_of_Sulawesi/mat.gmt')
#fig.plot('/mnt/d/celebes-stress-inversion-project/data/GMT_Seismotectonics_of_Sulawesi/matanoarrow.gmt')
#fig.plot('/mnt/d/celebes-stress-inversion-project/data/GMT_Seismotectonics_of_Sulawesi/strikeslipsulawesihall.gmt')
#fig.plot('/mnt/d/celebes-stress-inversion-project/data/GMT_Seismotectonics_of_Sulawesi/sang1.gmt')
#fig.plot('/mnt/d/celebes-stress-inversion-project/data/GMT_Seismotectonics_of_Sulawesi/sang2.gmt')
fig.plot('/mnt/d/celebes-stress-inversion-project/data/GMT_Seismotectonics_of_Sulawesi/slabdepthlegend.gmt')

fig.show()