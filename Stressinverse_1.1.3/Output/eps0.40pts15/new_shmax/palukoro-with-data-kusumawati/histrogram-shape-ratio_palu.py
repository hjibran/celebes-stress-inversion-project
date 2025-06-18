import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme()

palette = {1: "#E63946", 2: "#457B9D", 3: "#F4A261", 4: "#8338EC", 5: "#2A9D8F",
           6: "#E63946", 7: "#457B9D", 8: "#F4A261", 9: "#8338EC", 10: "#2A9D8F",
           11: "#E63946", 12: "#457B9D", 13: "#F4A261", 14: "#8338EC", 15: "#2A9D8F",
           'Before': "#E63946", 'After': "#E63946"
}

# Tentukan lebar bin
bin_width = 1/20  # Lebar bin
bins = np.arange(0, 1 + bin_width, bin_width)  # Membuat array batas bin dengan lebar tertentu


def plot_histogram(area):
    print(area)
    data = pd.read_csv("/mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Output/eps0.40pts15/new_shmax/palukoro-with-data-kusumawati/shaperatio{}.csv".format(area))

    ax = sns.histplot(data, x="Shape Ratio", 
                      hue="Cluster", 
                      bins=bins, 
                      element="bars", 
                      palette=palette
    )

    plt.xlim(0,1)
    sns.move_legend(ax, "upper left")
    plt.show()

plot_histogram("A-Bbefore")
plot_histogram("A-Bafter")
plot_histogram("A-Dbefore")
plot_histogram("A-Dafter")