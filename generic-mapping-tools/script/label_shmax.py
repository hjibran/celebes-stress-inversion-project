import pygmt

fig = pygmt.Figure()
fig.basemap(region=[0,1,0,1],
            projection="X5c/5c",
            frame=True
)

def shmax_plot(lon, lat, down, up):
    if down <=180:
        down1 = down+180
    elif down > 180:
        down1 = down -180
    if up <=180:
        up1 = up+180
    elif up > 180:
        up1 = up -180

    def project(azimuth):
        degree = 360-azimuth+90
        return degree

    data = [[lon, lat, 2, 360-up+90, 360-down+90], [lon, lat, 2, 360-up1+90, 360-down1+90]]
    fig.plot(data=data, style="w", fill="gold2")#, transparency=20)#, pen="1p, red")

shmax_plot(0.5,0.5,35,95)

fig.show()