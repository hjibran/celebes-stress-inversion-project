import pygmt

def buat_peta(region, judul, nama_file, posisi_judul):
    """
    Fungsi untuk membuat peta dengan parameter yang dapat disesuaikan
    """
    # Membuat figure baru
    fig = pygmt.Figure()
    
    # Menambahkan basemap dengan proyeksi Mercator
    fig.basemap(
        region=region,
        projection="M15c",  # Mercator 15cm
        frame=["a2f1", "WSne"]  # Grid setiap 2 derajat, frame setiap 1 derajat
    )
    
    # Menambahkan garis pantai dengan warna hitam
    fig.coast(
        shorelines="1/0.5p,black",  # Garis pantai hitam dengan ketebalan 0.5p
        land="lightgray",           # Warna daratan abu-abu muda
        water="lightblue",          # Warna laut biru muda
        borders="1/0.25p,gray"      # Batas negara/provinsi dengan garis abu-abu tipis
    )
    
    # Menambahkan grid
    fig.basemap(frame=["a2f1", "WSne"])
    
    # Menambahkan judul
    fig.text(
        text=judul,
        x=posisi_judul[0],  # Posisi x (longitude)
        y=posisi_judul[1],  # Posisi y (latitude)
        font="16p,Helvetica-Bold,black",
        justify="MC"  # Middle Center
    )
    
    # Menambahkan skala
    fig.basemap(
        map_scale="jBL+w200k+o0.5c/0.5c+f",  # Skala 200km di pojok kiri bawah
    )
    
    # Menambahkan kompas/arah utara
    fig.basemap(
        rose="jTR+w3c+f2+l+o0.5c/0.5c"  # Kompas di pojok kanan atas
    )
    
    # Menyimpan peta
    fig.savefig(f"{nama_file}.png", dpi=300)
    fig.savefig(f"{nama_file}.pdf")
    
    # Menampilkan peta
    fig.show()
    
    return fig

# === PETA 1: PULAU SULAWESI ===
print("Membuat peta Pulau Sulawesi...")

# Koordinat untuk area Pulau Sulawesi
# Batas longitude: 118°E - 126°E, Batas latitude: 6°S - 2°N
region_sulawesi = [118, 126, -6, 2]
posisi_judul_sulawesi = [122, 1.5]

fig_sulawesi = buat_peta(
    region=region_sulawesi,
    judul="Peta Pulau Sulawesi",
    nama_file="peta_sulawesi",
    posisi_judul=posisi_judul_sulawesi
)

# === PETA 2: PULAU SUMATRA ===
print("Membuat peta Pulau Sumatra...")

# Koordinat untuk area Pulau Sumatra  
# Batas longitude: 95°E - 108°E, Batas latitude: 6°N - (-6°S)
region_sumatra = [95, 108, -6, 6]
posisi_judul_sumatra = [101.5, 5]

fig_sumatra = buat_peta(
    region=region_sumatra,
    judul="Peta Pulau Sumatra", 
    nama_file="peta_sumatra",
    posisi_judul=posisi_judul_sumatra
)

print("\n=== HASIL ===")
print("✓ Peta Pulau Sulawesi berhasil dibuat!")
print("  - File: peta_sulawesi.png dan peta_sulawesi.pdf")
print("✓ Peta Pulau Sumatra berhasil dibuat!")
print("  - File: peta_sumatra.png dan peta_sumatra.pdf")
print("\nTotal: 4 file gambar telah dibuat (2 PNG + 2 PDF)")