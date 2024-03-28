#!/home/haidir/celebes-stress-inversion-project/venv/bin/python3

import pygmt
#pygmt.show_versions()

fig = pygmt.Figure()
fig.coast(
    region=[117.5, 127.5, -8.5, 5.5], 
    frame=["a", "+tPulau Sulawesi"],
    shorelines=1
)
#fig.savefig("pygmt_tut_1.pdf")
fig.show()
