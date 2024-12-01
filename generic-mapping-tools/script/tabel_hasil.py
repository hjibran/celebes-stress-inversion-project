import pandas as pd
import numpy as np

def midelval(down, up):
    if down < up:
        return (down+up)/2
    else:
        down1=down+360
        hasil=(down1+up)/2
        if hasil < 360:
            return hasil
        else:
            return hasil-360

azimuth1=[]; azimuth2=[]; azimuth3=[]; plunge1=[]; plunge2=[]; plunge3=[]; shaperatio=[]; shmax=[]

for i in range(10):
    data = pd.read_csv('/mnt/d/celebes-stress-inversion-project/Stressinverse_1.1.3/Output/eps0.50pts15/cls{}/output_error.csv'.format(i))
    azimuth1_25 = data['2.5%'][0]; plunge1_25 = data['2.5%'][1]; azimuth2_25 = data['2.5%'][2];plunge2_25 = data['2.5%'][3];azimuth3_25 = data['2.5%'][4];plunge3_25 = data['2.5%'][5];shmax_25 = data['2.5%'][6];shaperatio_25 = data['2.5%'][7]
    azimuth1_975 = data['97.5%'][0]; plunge1_975 = data['97.5%'][1]; azimuth2_975 = data['97.5%'][2]; plunge2_975 = data['97.5%'][3]; azimuth3_975 = data['97.5%'][4]; plunge3_975 = data['97.5%'][5]; shmax_975 = data['97.5%'][6]; shaperatio_975 = data['97.5%'][7]
    azimuth1_error = data['half width 95% percentil'][0]; plunge1_error = data['half width 95% percentil'][1]; azimuth2_error = data['half width 95% percentil'][2]; plunge2_error = data['half width 95% percentil'][3]; azimuth3_error = data['half width 95% percentil'][4]; plunge3_error = data['half width 95% percentil'][5]; shmax_error = data['half width 95% percentil'][6]; shaperatio_error = data['half width 95% percentil'][7]
    azimuth1.append("{:.3f} ± {:.3f}".format(midelval(azimuth1_25,azimuth1_975),azimuth1_error)); plunge1.append("{:.3f} ± {:.3f}".format(midelval(plunge1_25,plunge1_975),plunge1_error)); azimuth2.append("{:.3f} ± {:.3f}".format(midelval(azimuth2_25, azimuth2_975),azimuth2_error)); plunge2.append("{:.3f} ± {:.3f}".format(midelval(plunge2_25, plunge2_975),plunge2_error)); azimuth3.append("{:.3f} ± {:.3f}".format(midelval(azimuth3_25,azimuth3_975),azimuth3_error)); plunge3.append ("{:.3f} ± {:.3f}".format(midelval(plunge3_25,plunge3_975),plunge3_error)); shaperatio.append("{:.3f} ± {:.3f}".format(midelval(shaperatio_25,shaperatio_975),shaperatio_error)); shmax.append("{:.3f} ± {:.3f}".format(midelval(shmax_25,shmax_975),shmax_error))

tabel = pd.DataFrame(data={'az1':azimuth1, 'pl1':plunge1, 'az2':azimuth2, 'pl2':plunge2, 'az3':azimuth3, 'pl3':plunge3, 'shp':shaperatio, 'sh':shmax})
tabel.to_excel('tabel_hasil50.xlsx')