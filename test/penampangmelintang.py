import pygmt
import pandas as pd
import numpy as np

#lokasi yang akan di buatkan penampang melintang
A=[0.5, 3.5]
B=[4.5, 0.5]
lebar_jangkauan=5

#membuat titik sebaran data / bisa import data yang sudah ada, urutan data harus sesuai
#longitude, latitude, depth, strike, dip, rake, magnitude
titik = np.array([
    [1, 2, 1, 0, 90, 0, 4],
    [2, 2, 4, 0, 45, -90, 4],
    [3, 2, 9, 0, 45, 90, 4],
    [4, 2, 16, 90, 90, -87, 4],
    [1.5, 3, 2.25, 89, 70, -56, 4],
    [2.8, 1, 7.84, 342, 34, -7, 4],
    [3, 2.8, 9, 8, 58, 8, 4]
])
tabel = pd.DataFrame(titik,
    columns=["longitude","latitude","depth","strike","dip","rake","magnitude"]
)

#membuat palet warna. warna sesuai kedalaman
pygmt.makecpt(
    cmap="blue,green,yellow,red",
    series="0,4,8,12,16",
    output="palet-warna.cpt"
    )

#membuat gambar
fig = pygmt.Figure()

#basemap, membuat lembar gambar map
fig.basemap(
    region=[0, 5, 0, 4,],
    projection='X5c/4c',
    frame=['xa1f0.5g0.5+lLongitude', 'ya1f0.5g0.5+lLatitude', '+tTes Menampilkan FM dan Cross']
)

#plot focal mechanism
fig.meca(
        spec=tabel,
        compressionfill="black",
        cmap="palet-warna.cpt",
        scale="0.2c",
        extensionfill="white"
    )

#plot lokasi yang akan dibuatkan penampang melintangnya
fig.plot(
    x=[A[0],B[0]],
    y=[A[1],B[1]],
    pen="1p,red"
)
fig.text(
    x=A[0]-0.2,
    y=A[1],
    text="A"
)
fig.text(
    x=B[0]+0.2,
    y=B[1],
    text="B"
)

#membuat map baru di bawah map sebelumnya
fig.shift_origin(yshift="-4.25c")

#mengambil nilai titik yang berada pada garis penampang melintang dengan lebar jangkauan yang telah ditentukan sebelumnya
cross = pygmt.project(
    center="{}/{}".format(A[0],A[1]),
    endpoint="{}/{}".format(B[0],B[1]),
    data=tabel,
    width="-{}/{}".format(lebar_jangkauan,lebar_jangkauan)
)

#basemap baru
fig.basemap(
    region=[0,((np.abs(A[0]-B[0])*2+np.abs(A[1]-B[1])*2)*(1/2)), 0, 20],
    projection="X5c/-2c",
    frame=["WSrt", "xa1+lkm", "ya4+ldepth km"],
)
fig.text(
    x=0.15,
    y=1.25,
    text="A"
)
fig.text(
    x=((np.abs(A[0]-B[0])*2+abs(A[1]-B[1])*2)*(1/2))-0.15,
    y= 1.25,
    text="B"
)

#plot data pada penampang melintang
fig.plot(
    x=cross[7],
    y=cross[2],
    fill=cross[2],
    cmap="palet-warna.cpt",
    style="c3p"
)


fig.show()