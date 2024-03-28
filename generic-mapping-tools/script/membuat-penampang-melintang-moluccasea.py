import pygmt
import pandas as pd
import numpy as np

#lokasi yang akan di buatkan penampang melintang
A=[122.2, 1.75]
B=[122.2, 1]
lebar_jangkauan=0.5

tabel = pd.read_csv("/mnt/d/celebes-stress-inversion-project/data/siap-olah/fm50km.csv")
tabel = tabel.iloc[:, [3,2,4,6,7,8,5]]
tabel.columns = ["longitude", "latitude", "depth", "strike", "dip", "rake", "magnitude"]
#membuat palet warna. warna sesuai kedalaman
pygmt.makecpt(
    cmap="blue,green,yellow,red",
    series="0,20,30,40,50",
    output="palet-warna.cpt"
    )
#membuat gambar
fig = pygmt.Figure()

#basemap, membuat lembar gambar map
fig.basemap(
    region=[121, 124, 0, 2.5],
    projection='X3i/2.5i',
    frame=['xa1f0.5g0.5+lLongitude', 'ya1f0.5g0.5+lLatitude', '+tTes Menampilkan FM dan Cross']
)

fig.coast(
    shorelines="black",
    land="khaki"
)
fig.plot(
    data="/mnt/d/celebes-stress-inversion-project/data/batas-lempeng-dan-patahan/indonesiafaults.gmt",
    pen="0.85p"
)
fig.plot(
    data="/mnt/d/celebes-stress-inversion-project/data/batas-lempeng-dan-patahan/trench.gmt",
    pen="1p",
    style="f1c/0.2c+l+t",
    fill="black"
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
fig.shift_origin(yshift="-2.5i")

#mengambil nilai titik yang berada pada garis penampang melintang dengan lebar jangkauan yang telah ditentukan sebelumnya
cross = pygmt.project(
    center="{}/{}".format(A[0],A[1]),
    endpoint="{}/{}".format(B[0],B[1]),
    data=tabel,
    width="-{}/{}".format(lebar_jangkauan,lebar_jangkauan)
)

#basemap baru
fig.basemap(
    region=[0, ((abs(A[0]-B[0])**2+abs(A[1]-B[1])**2)**(1/2))*111.322, 0, 60],
    projection="X3i/-2i",
    frame=["WSrt", "xa50+lkm", "ya4+ldepth km"],
)
fig.text(
    x=0.15,
    y=1.25,
    text="A"
)
fig.text(
    x=((abs(A[0]-B[0])**2+abs(A[1]-B[1])**2)**(1/2))-0.15,
    y= 1.25,
    text="B"
)

#plot data pada penampang melintang
fig.plot(
    x=cross[7]*111.322,
    y=cross[2],
    fill=cross[2],
    cmap="palet-warna.cpt",
    style="c3p"
)


fig.show()