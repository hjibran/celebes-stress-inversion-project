import numpy as np
import matplotlib.pyplot as plt

# Mendefinisikan variabel input
segment_theta = np.array([31, 49, 49])
segment_delta = np.array([22, -7, 7])
error_theta = np.array([19, 13, 20])
error_delta = np.array([18, 20, 16])

# Membuat array sudut theta
theta = np.arange(0, 90.01, 0.01)  # dari 0 sampai 90 dengan step 0.01

# Membuat array rasio stress drop
stress_drop_ratio = np.arange(-1, 1.01, 0.2)
# Menghapus nilai 0 dalam array yang terbentuk
stress_drop_ratio = np.delete(stress_drop_ratio, 5)

# Menghitung komponen trigonometri
A = 2 * np.sin(np.radians(theta)) * np.cos(np.radians(theta))  # sin2(theta)
B = np.cos(np.radians(theta))**2 - np.sin(np.radians(theta))**2  # cos2(theta)

# Inisialisasi array untuk delta_theta
delta_theta = np.zeros((len(theta), len(stress_drop_ratio)))

# Menghitung delta_theta untuk setiap nilai stress_drop_ratio
for i in range(len(stress_drop_ratio)):
    nominator = 1 - (stress_drop_ratio[i] * A) - np.sqrt(stress_drop_ratio[i]**2 + 1 - (2 * stress_drop_ratio[i] * A))
    denominator = stress_drop_ratio[i] * B
    # atand di MATLAB -> arctangent dalam derajat di Python
    delta_theta[:, i] = np.degrees(np.arctan(nominator / denominator))

# Mengganti NaN dengan 0
delta_theta = np.nan_to_num(delta_theta)

# Membuat plot
plt.figure(figsize=(10, 8))

# Plot garis untuk setiap stress_drop_ratio
for i in range(1, len(stress_drop_ratio)):
    plt.plot(theta, delta_theta[:, 0], 'k')
    plt.plot(theta, delta_theta[:, i], 'k')

# Plot errorbar
plt.errorbar(segment_theta[0], segment_delta[0], yerr=error_delta[0], fmt='o', color='red', 
             markersize=7, markerfacecolor='red', linewidth=0.65)
plt.errorbar(segment_theta[0], segment_delta[0], xerr=error_theta[0], fmt='o', color='red',
             markersize=7, markerfacecolor='red', linewidth=0.65)

plt.errorbar(segment_theta[1], segment_delta[1], yerr=error_delta[1], fmt='o', color='blue',
             markersize=7, markerfacecolor='blue', linewidth=0.65)
plt.errorbar(segment_theta[1], segment_delta[1], xerr=error_theta[1], fmt='o', color='blue',
             markersize=7, markerfacecolor='blue', linewidth=0.65)

plt.errorbar(segment_theta[2], segment_delta[2], yerr=error_delta[2], fmt='o', color='magenta',
             markersize=7, markerfacecolor='magenta', linewidth=0.65)
plt.errorbar(segment_theta[2], segment_delta[2], xerr=error_theta[2], fmt='o', color='magenta',
             markersize=7, markerfacecolor='magenta', linewidth=0.65)

# Menambahkan teks
plt.text(59, 40, r'$\Delta\tau/\tau = 1$')

# Label dan ukuran plot
plt.xlabel(r'$\theta$ (degrees)', fontsize=15)
plt.ylabel(r'$\Delta\theta$ (degrees)', fontsize=15)
plt.ylim([-45, 45])
plt.xlim([0, 90])

plt.grid(True)
plt.tight_layout()
plt.show()