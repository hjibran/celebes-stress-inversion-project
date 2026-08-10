import pygmt

# Buat CPT dua warna solid
pygmt.makecpt(
    cmap="135/206/250,211/211/211",  # dua warna: biru muda, abu-abu cerah
    series=[-1000, 1000, 1000],      # dua segmen: (-1000–0), (0–1000)
    continuous=False,                 # non-kontinu → warna blok
    output="two_color.cpt"            # simpan ke file CPT
)
