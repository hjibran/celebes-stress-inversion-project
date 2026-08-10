def konvergensi(chosen_planes, initial_planes):
    import numpy as np

    diff = np.abs(chosen_planes - initial_planes)
    diff[:, 0] = np.minimum(diff[:, 0], 360 - diff[:, 0])
    diff[:, 2] = np.minimum(diff[:, 2], 360 - diff[:, 2])

    correct_identifications = np.sum(np.all(diff < 1.0, axis=1))
    konvergen = (correct_identifications / len(initial_planes)) * 100

    return konvergen

def plot_konvergensi(konvergensi, figName=False):
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns

    tabel_konvergensi = pd.DataFrame({
        "iterasi ke" : [x+1 for x in range(len(konvergensi))],
        "persen konvergensi" : konvergensi
    })

    # Atur tema/gaya plot menggunakan Seaborn
    sns.set_theme(style="whitegrid", palette="viridis")

    # Buat plot
    # Menggunakan plt.subplots() memberikan kontrol yang lebih baik atas ukuran gambar
    fig, ax = plt.subplots(figsize=(10, 6))

    # Gunakan sns.lineplot untuk menggambar garis
    # marker='o' untuk memberikan tanda pada setiap titik data
    sns.lineplot(
        data=tabel_konvergensi,
        x='iterasi ke',
        y='persen konvergensi',
        marker='o',
        linewidth=2.5,
        ax=ax
    )

    # 4. Tambahkan kustomisasi (masih menggunakan Matplotlib)
    # Tambahkan garis vertikal untuk menandai batas konvergensi
    ax.axvline(x=6, color='coral', linestyle='--', linewidth=2, label='Batas Konvergensi (Iterasi 6)')

    # Atur judul dan label
    ax.set_title('Konvergensi Pemilihan Bidang Sesar per Iterasi', fontsize=16, pad=20)
    ax.set_xlabel('Jumlah Iterasi', fontsize=12)
    ax.set_xticks([x+1 for x in range(len(konvergensi)+1)])
    ax.set_ylabel('Stabilitas Solusi (%)', fontsize=12)

    # Atur batas sumbu (axis limits)
    ax.set_xlim(0.5, len(konvergensi)+1.5)
    ax.set_ylim(0, 105)

    # Tampilkan legenda
    ax.legend()

    # Menampilkan plot
    plt.tight_layout()
    if figName:
        plt.savefig("/mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Figures/konvergensi{}.png".format(figName))
        plt.show()
    else:
        plt.show()

def plot_shape_ratio(ShapeRatio, figName=False):
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns

    tabel_ShapeRatio = pd.DataFrame({
        "iterasi ke" : [x+1 for x in range(len(ShapeRatio))],
        "persen ShapeRatio" : ShapeRatio
    })

    # Atur tema/gaya plot menggunakan Seaborn
    sns.set_theme(style="whitegrid", palette="viridis")

    # Buat plot
    # Menggunakan plt.subplots() memberikan kontrol yang lebih baik atas ukuran gambar
    fig, ax = plt.subplots(figsize=(10, 6))

    # Gunakan sns.lineplot untuk menggambar garis
    # marker='o' untuk memberikan tanda pada setiap titik data
    sns.lineplot(
        data=tabel_ShapeRatio,
        x='iterasi ke',
        y='persen ShapeRatio',
        marker='o',
        linewidth=2.5,
        ax=ax
    )

    # 4. Tambahkan kustomisasi (masih menggunakan Matplotlib)
    # Tambahkan garis vertikal untuk menandai batas ShapeRatio
    ax.axvline(x=6, color='coral', linestyle='--', linewidth=2, label='Batas ShapeRatio (Iterasi 6)')

    # Atur judul dan label
    ax.set_title('ShapeRatio Pemilihan Bidang Sesar per Iterasi', fontsize=16, pad=20)
    ax.set_xlabel('Jumlah Iterasi', fontsize=12)
    ax.set_xticks([x+1 for x in range(len(ShapeRatio)+1)])
    ax.set_ylabel('Stabilitas Solusi (%)', fontsize=12)

    # Atur batas sumbu (axis limits)
    ax.set_xlim(0.5, len(ShapeRatio)+1.5)
    ax.set_ylim(0, 1.05)

    # Tampilkan legenda
    ax.legend()

    # Menampilkan plot
    plt.tight_layout()
    if figName:
        plt.savefig("/mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Figures/konvergensi{}.png".format(figName))
        plt.show()
    else:
        plt.show()