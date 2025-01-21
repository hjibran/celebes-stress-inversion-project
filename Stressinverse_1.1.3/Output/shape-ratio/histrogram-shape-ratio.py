import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme()

palette = {1: "#E63946", 2: "#457B9D", 3: "#F4A261", 4: "#8338EC", 5: "#2A9D8F",
           6: "#E63946", 7: "#457B9D", 8: "#F4A261", 9: "#8338EC", 10: "#2A9D8F",
           11: "#E63946", 12: "#457B9D", 13: "#F4A261", 14: "#8338EC", 15: "#2A9D8F",
}

# Tentukan lebar bin
bin_width = 1/20  # Lebar bin
bins = np.arange(0, 1 + bin_width, bin_width)  # Membuat array batas bin dengan lebar tertentu


def plot_histogram(area):
    data = pd.read_csv("/mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Output/shape-ratio/{}.csv".format(area))

    ax = sns.histplot(data, x="shape ratio", 
                      hue="klaster", 
                      bins=bins, 
                      element="bars", 
                      palette=palette
    )

    plt.xlim(0,1)
    sns.move_legend(ax, "upper left")
    plt.show()

plot_histogram("utara1-5")
plot_histogram("utara6-8")
plot_histogram("utara9-12")
plot_histogram("selatan1")
plot_histogram("selatan2-4")
plot_histogram("maluku1-4")
plot_histogram("maluku5-7")
plot_histogram("sula")
plot_histogram("sangihe")
plot_histogram("ntt")