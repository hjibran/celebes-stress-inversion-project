import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.interpolate import griddata
import plotly.graph_objects as go
import plotly.express as px

# ============================================================================
# METODE 1: Menggunakan Matplotlib dengan data kontur
# ============================================================================

def plot_soil_layers_matplotlib():
    """Plot 2 lapisan tanah menggunakan matplotlib"""
    
    # Contoh data kontur lapisan 1 (permukaan atas)
    # Format: [x, y, z] koordinat dari kontur
    x1 = np.array([0, 10, 20, 30, 40, 50, 0, 10, 20, 30, 40, 50])
    y1 = np.array([0, 0, 0, 0, 0, 0, 10, 10, 10, 10, 10, 10])
    z1 = np.array([100, 98, 95, 92, 90, 88, 102, 100, 97, 94, 92, 90])  # elevasi lapisan 1
    
    # Contoh data kontur lapisan 2 (bawah)
    x2 = np.array([0, 10, 20, 30, 40, 50, 0, 10, 20, 30, 40, 50])
    y2 = np.array([0, 0, 0, 0, 0, 0, 10, 10, 10, 10, 10, 10])
    z2 = np.array([85, 83, 80, 77, 75, 73, 87, 85, 82, 79, 77, 75])  # elevasi lapisan 2
    
    # Buat grid untuk interpolasi
    xi = np.linspace(x1.min(), x1.max(), 50)
    yi = np.linspace(y1.min(), y1.max(), 50)
    Xi, Yi = np.meshgrid(xi, yi)
    
    # Interpolasi data kontur ke grid
    Z1 = griddata((x1, y1), z1, (Xi, Yi), method='cubic')
    Z2 = griddata((x2, y2), z2, (Xi, Yi), method='cubic')
    
    # Plot 3D
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Plot lapisan 1 (atas)
    surf1 = ax.plot_surface(Xi, Yi, Z1, alpha=0.7, cmap='terrain', 
                           linewidth=0, antialiased=True, label='Lapisan 1')
    
    # Plot lapisan 2 (bawah)
    surf2 = ax.plot_surface(Xi, Yi, Z2, alpha=0.7, cmap='viridis', 
                           linewidth=0, antialiased=True, label='Lapisan 2')
    
    # Tambahkan kontur asli sebagai titik
    ax.scatter(x1, y1, z1, color='red', s=30, label='Data Lapisan 1')
    ax.scatter(x2, y2, z2, color='blue', s=30, label='Data Lapisan 2')
    
    # Pengaturan plot
    ax.set_xlabel('X (m)')
    ax.set_ylabel('Y (m)')
    ax.set_zlabel('Elevasi (m)')
    ax.set_title('Visualisasi 3D - 2 Lapisan Tanah')
    
    # Colorbar
    fig.colorbar(surf1, ax=ax, shrink=0.5, aspect=5, label='Lapisan 1')
    
    plt.tight_layout()
    plt.show()

# ============================================================================
# METODE 2: Menggunakan Plotly (Interaktif)
# ============================================================================

def plot_soil_layers_plotly():
    """Plot interaktif menggunakan Plotly"""
    
    # Data sama seperti sebelumnya
    x1 = np.array([0, 10, 20, 30, 40, 50, 0, 10, 20, 30, 40, 50])
    y1 = np.array([0, 0, 0, 0, 0, 0, 10, 10, 10, 10, 10, 10])
    z1 = np.array([100, 98, 95, 92, 90, 88, 102, 100, 97, 94, 92, 90])
    
    x2 = np.array([0, 10, 20, 30, 40, 50, 0, 10, 20, 30, 40, 50])
    y2 = np.array([0, 0, 0, 0, 0, 0, 10, 10, 10, 10, 10, 10])
    z2 = np.array([85, 83, 80, 77, 75, 73, 87, 85, 82, 79, 77, 75])
    
    # Interpolasi
    xi = np.linspace(min(x1.min(), x2.min()), max(x1.max(), x2.max()), 30)
    yi = np.linspace(min(y1.min(), y2.min()), max(y1.max(), y2.max()), 30)
    Xi, Yi = np.meshgrid(xi, yi)
    
    Z1 = griddata((x1, y1), z1, (Xi, Yi), method='cubic')
    Z2 = griddata((x2, y2), z2, (Xi, Yi), method='cubic')
    
    # Buat plot
    fig = go.Figure()
    
    # Surface lapisan 1
    fig.add_trace(go.Surface(
        x=Xi, y=Yi, z=Z1,
        colorscale='Earth',
        name='Lapisan 1 (Atas)',
        opacity=0.8,
        showscale=True
    ))
    
    # Surface lapisan 2
    fig.add_trace(go.Surface(
        x=Xi, y=Yi, z=Z2,
        colorscale='Viridis',
        name='Lapisan 2 (Bawah)',
        opacity=0.8,
        showscale=False
    ))
    
    # Scatter points data asli
    fig.add_trace(go.Scatter3d(
        x=x1, y=y1, z=z1,
        mode='markers',
        marker=dict(size=5, color='red'),
        name='Data Lapisan 1'
    ))
    
    fig.add_trace(go.Scatter3d(
        x=x2, y=y2, z=z2,
        mode='markers',
        marker=dict(size=5, color='blue'),
        name='Data Lapisan 2'
    ))
    
    # Layout
    fig.update_layout(
        title='Visualisasi 3D Interaktif - 2 Lapisan Tanah',
        scene=dict(
            xaxis_title='X (m)',
            yaxis_title='Y (m)',
            zaxis_title='Elevasi (m)',
            camera=dict(eye=dict(x=1.5, y=1.5, z=1.2))
        ),
        width=800,
        height=600
    )
    
    fig.show()

# ============================================================================
# METODE 3: Dari file data kontur
# ============================================================================

def load_and_plot_from_file():
    """Membaca data kontur dari file dan plot 3D"""
    
    # Contoh membaca dari CSV
    # Asumsi format CSV: x, y, z_layer1, z_layer2
    
    # Jika data dalam format shapefile atau format GIS lain
    # import geopandas as gpd
    # gdf = gpd.read_file('kontur_lapisan.shp')
    
    # Contoh data manual
    data = np.array([
        [0, 0, 100, 85],
        [10, 0, 98, 83],
        [20, 0, 95, 80],
        [30, 0, 92, 77],
        [0, 10, 102, 87],
        [10, 10, 100, 85],
        [20, 10, 97, 82],
        [30, 10, 94, 79]
    ])
    
    x = data[:, 0]
    y = data[:, 1]
    z1 = data[:, 2]  # lapisan 1
    z2 = data[:, 3]  # lapisan 2
    
    # Sama seperti metode sebelumnya untuk plotting
    xi = np.linspace(x.min(), x.max(), 30)
    yi = np.linspace(y.min(), y.max(), 30)
    Xi, Yi = np.meshgrid(xi, yi)
    
    Z1 = griddata((x, y), z1, (Xi, Yi), method='cubic')
    Z2 = griddata((x, y), z2, (Xi, Yi), method='cubic')
    
    # Plot dengan matplotlib
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    surf1 = ax.plot_surface(Xi, Yi, Z1, alpha=0.7, cmap='terrain')
    surf2 = ax.plot_surface(Xi, Yi, Z2, alpha=0.7, cmap='viridis')
    
    ax.set_xlabel('X (m)')
    ax.set_ylabel('Y (m)')
    ax.set_zlabel('Elevasi (m)')
    ax.set_title('Lapisan Tanah dari Data File')
    
    plt.show()

# ============================================================================
# METODE 4: Dengan ketebalan lapisan
# ============================================================================

def plot_with_thickness():
    """Plot dengan menampilkan ketebalan lapisan"""
    
    # Data contoh
    x = np.linspace(0, 50, 20)
    y = np.linspace(0, 20, 10)
    X, Y = np.meshgrid(x, y)
    
    # Elevasi permukaan atas
    Z_top = 100 - 0.1*X - 0.05*Y + 2*np.sin(X/10) + np.cos(Y/5)
    
    # Ketebalan lapisan 1
    thickness1 = 10 + 2*np.sin(X/8) + np.cos(Y/6)
    
    # Elevasi batas lapisan 1-2
    Z_mid = Z_top - thickness1
    
    # Ketebalan lapisan 2
    thickness2 = 15 + 3*np.sin(X/12) + 1.5*np.cos(Y/8)
    
    # Elevasi dasar lapisan 2
    Z_bottom = Z_mid - thickness2
    
    # Plot
    fig = plt.figure(figsize=(15, 5))
    
    # Subplot 1: Surface plot
    ax1 = fig.add_subplot(131, projection='3d')
    ax1.plot_surface(X, Y, Z_top, alpha=0.7, cmap='terrain', label='Permukaan')
    ax1.plot_surface(X, Y, Z_mid, alpha=0.7, cmap='viridis', label='Batas Lapisan')
    ax1.plot_surface(X, Y, Z_bottom, alpha=0.7, cmap='copper', label='Dasar')
    ax1.set_title('3 Permukaan')
    ax1.set_xlabel('X (m)')
    ax1.set_ylabel('Y (m)')
    ax1.set_zlabel('Elevasi (m)')
    
    # Subplot 2: Ketebalan lapisan 1
    ax2 = fig.add_subplot(132)
    contour1 = ax2.contourf(X, Y, thickness1, levels=15, cmap='Blues')
    ax2.set_title('Ketebalan Lapisan 1')
    ax2.set_xlabel('X (m)')
    ax2.set_ylabel('Y (m)')
    plt.colorbar(contour1, ax=ax2, label='Ketebalan (m)')
    
    # Subplot 3: Ketebalan lapisan 2
    ax3 = fig.add_subplot(133)
    contour2 = ax3.contourf(X, Y, thickness2, levels=15, cmap='Reds')
    ax3.set_title('Ketebalan Lapisan 2')
    ax3.set_xlabel('X (m)')
    ax3.set_ylabel('Y (m)')
    plt.colorbar(contour2, ax=ax3, label='Ketebalan (m)')
    
    plt.tight_layout()
    plt.show()

# ============================================================================
# Jalankan contoh
# ============================================================================

if __name__ == "__main__":
    print("Pilih metode visualisasi:")
    print("1. Matplotlib (statis)")
    print("2. Plotly (interaktif)")
    print("3. Dari data file")
    print("4. Dengan ketebalan lapisan")
    
    choice = input("Masukkan pilihan (1-4): ")
    
    if choice == "1":
        plot_soil_layers_matplotlib()
    elif choice == "2":
        plot_soil_layers_plotly()
    elif choice == "3":
        load_and_plot_from_file()
    elif choice == "4":
        plot_with_thickness()
    else:
        print("Menjalankan semua contoh...")
        plot_soil_layers_matplotlib()
        # plot_soil_layers_plotly()  # Uncomment jika ingin plotly
        plot_with_thickness()