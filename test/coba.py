import matplotlib.pyplot as plt

data = pd.read_txt("./1.coh")

fig, ((ax1, ax2, ax3, ax4, ax5, ax6, ax7), (ax8, ax9, ax10, ax11, ax12, ax13, ax14)) = plt.subplots(2, 7)

ax1.hist(x1, y1)
ax2.hist(x2, y2)
ax3.hist(x3, y3)
ax4.hist(x4, y4)
ax5.hist(x5, y5)
ax6.hist(x6, y6)
ax7.hist(x7, y7)
ax8.hist(x8, y8)
ax9.hist(x9, y9)
ax10.hist(x10, y10)
ax11.hist(x11, y11)
ax12.hist(x12, y12)
ax13.hist(x13, y13)
ax14.hist(x14, y14)

plt.show()