import numpy as np
import pandas as pd
import os

def shmax_plot(lon, lat, down, up, AR):
    if down <=180:
        down1 = down+180
    elif down > 180:
        down1 = down -180
    if up <=180:
        up1 = up+180
    elif up > 180:
        up1 = up -180
    
    if 0 <= AR < 1:
        fill = "blue"
    elif 1 <= AR < 2:
        fill = "green"
    elif 2.0 <= AR < 3:
        fill = "red"

    data = [[lon, lat, 360-up+90, 360-down+90], [lon, lat, 360-up1+90, 360-down1+90]]
    fig.plot(data=data, style="w1.5c", fill=fill, cmap=False, transparency=25, pen="black")
    
import pygmt

fig = pygmt.Figure()

fig.coast(region=[0, 5, -1.5, 1.5],
          projection='M10c',
          frame=["a", "EWSN"],
          land='lightgray',
          resolution='f',
          #shorelines='0.25p,black,solid'
          )

font = "13p,Helvetica-Bold,black"

shmax_plot(1, 0.5,  55, 105, 2.5)  #; fig.text(x=2.5, y=0, text="Makassar", font=font)
shmax_plot(1, 0,    55, 105, 1.5)  #; fig.text(x=2.5, y=0, text="Makassar", font=font)
shmax_plot(1, -0.5, 55, 105, 0.5)  #; fig.text(x=2.5, y=0, text="Makassar", font=font)

fig.plot(x=2, y=0.5,   style="p0.25c", fill="red")        #; fig.text(x=2.5, y=0, text="Makassar", font=font)
fig.plot(x=2, y=0,     style="p0.25c", fill="green")      #; fig.text(x=2.5, y=0, text="Makassar", font=font)
fig.plot(x=2, y=-0.50, style="p0.25c", fill="blue")       #; fig.text(x=2.5, y=0, text="Makassar", font=font)

fig.plot(x=3, y=0.2,  style="c0.25c", pen='1.25p,red')    #; fig.text(x=2.5, y=0, text="Makassar", font=font)
fig.plot(x=3, y=-0.2, style="+0.25c", pen='1.25p,blue')   #; fig.text(x=2.5, y=0, text="Makassar", font=font) 

fig.plot(x=[3.75,4.25], y=[0.50,0.50], pen="2p,red")      #; fig.text(x=2.5, y=0, text="Makassar", font=font)
fig.plot(x=[3.75,4.25], y=[0.00,0.00], pen="2p,yellow")   #; fig.text(x=2.5, y=0, text="Makassar", font=font)
fig.plot(x=[3.75,4.25], y=[-0.5,-0.5], pen="2p,purple")   #; fig.text(x=2.5, y=0, text="Makassar", font=font)

fig.show()