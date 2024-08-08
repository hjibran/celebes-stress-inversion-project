#!/home/haidir/celebes-stress-inversion-project/venv/bin/python3
#*************************************************************************#
#                                                                         #
#  function confidence_interval                                           #
#                                                                         #
#  return the 95% Confidence interval of bootstrap                        #
#                                                                         #
#  input: the distribution list of bootstrap                              #
#                                                                         #
#                                                                         #
#*************************************************************************#

def confidence_interval(distribution):

    import math as m

    #----------------------------------------------------------------------
    #Menghitung Rata-rata
    #----------------------------------------------------------------------

    Mean = sum(distribution)/len(distribution)

    #----------------------------------------------------------------------
    #Menghitung nilai Variant
    #----------------------------------------------------------------------

    v = 0
    for i in range(len(distribution)):
        v += (distribution[i] - Mean)**2
    variant = v/(len(distribution)-1)

    #----------------------------------------------------------------------
    #Menghitung Standar Deviasi
    #----------------------------------------------------------------------

    standar_deviation = m.sqrt(variant)

    #----------------------------------------------------------------------
    #Menghitung 95% Confidence Interval
    #----------------------------------------------------------------------

    Confidence_Interval = 1.960*standar_deviation/m.sqrt(len(distribution))

    result = [Mean, Confidence_Interval]

    return result

#*************************************************************************#
#                                                                         #
#  function histogram                                                     #
#                                                                         #
#  show the histogram of bootsrap data                                    #
#                                                                         #
#  input: the distribution list of bootstrap and how many bin             #
#                                                                         #
#                                                                         #
#*************************************************************************#

def histogram(samp1, samp2, samp3, samp4, samp5, samp6, bin):

    import matplotlib.pyplot as plt

    #----------------------------------------------------------------------
    #Membuat subplot
    #----------------------------------------------------------------------

    fig, ((ax1, ax2), (ax3, ax4), (ax5, ax6)) = plt.subplots(3, 2)

    #----------------------------------------------------------------------
    #Memplot masing-masing histigram
    #----------------------------------------------------------------------

    ax1.hist(samp1, bins = bin)
    ax1.set(xlabel='Azimut Sigma 1 Distribution', ylabel='Frekuensi')
    ax2.hist(samp2, bins = bin)
    ax2.set(xlabel='Plunge Sigma 1 Distribution', ylabel='Frekuensi')
    ax3.hist(samp3, bins = bin)
    ax3.set(xlabel='Azimut Sigma 2 Distribution', ylabel='Frekuensi')
    ax4.hist(samp4, bins = bin)
    ax4.set(xlabel='Plunge Sigma 2 Distribution', ylabel='Frekuensi')
    ax5.hist(samp5, bins = bin)
    ax5.set(xlabel='Azimut Sigma 3 Distribution', ylabel='Frekuensi')
    ax6.hist(samp6, bins = bin)
    ax6.set(xlabel='Plunge Sigma 3 Distribution', ylabel='Frekuensi')
    
    #----------------------------------------------------------------------
    #Menampilkan Plot
    #----------------------------------------------------------------------

    plt.show()

#--------------------------------------------------------------------------
#--------------------------------------------------------------------------

def histo(azim, plun, bin):

    import matplotlib.pyplot as plt
    import numpy as np

    #----------------------------------------------------------------------
    #Membuat subplot
    #----------------------------------------------------------------------

    fig, ((ax1, ax2)) = plt.subplots(1, 2)
    fig.set_figheight(2.5)
    fig.set_figwidth(6.25)
    
    #----------------------------------------------------------------------
    #Memplot masing-masing histigram
    #----------------------------------------------------------------------

    ax1.hist(azim, bins = bin)
    ax1.set(xlabel='Azimut Distribution', ylabel='Frekuensi')
    conint1 = np.percentile(azim, [2.5, 97.5])
    y1 = np.linspace(0,50)
    x1 = [conint1 for i in y1]
    ax1.plot(x1,y1)
    avr_az = sum(azim)/len(azim)
    avr_azim = [avr_az for i in y1]
    ax1.plot(avr_azim,y1)

    ax2.hist(plun, bins = bin)
    ax2.set(xlabel='Plunge Distribution', ylabel='Frekuensi')
    conint2 = np.percentile(plun, [2.5, 97.5])
    y2 = np.linspace(0,50)
    x2 = [conint2 for i in y2]
    ax2.plot(x2,y2)
    avr_pl = sum(plun)/len(plun)
    avr_plun = [avr_pl for i in y2]
    ax2.plot(avr_plun,y2)

    
    #----------------------------------------------------------------------
    #Menampilkan Plot
    #----------------------------------------------------------------------

    plt.show()

#--------------------------------------------------------------------------
#--------------------------------------------------------------------------

def hist(shap, bin):

    import matplotlib.pyplot as plt
    import numpy as np

    #----------------------------------------------------------------------
    #Membuat subplot
    #----------------------------------------------------------------------

    fig, ((ax1)) = plt.subplots(1, 1)
    fig.set_figheight(2.5)
    fig.set_figwidth(3.75)

    #----------------------------------------------------------------------
    #Memplot masing-masing histigram
    #----------------------------------------------------------------------

    ax1.hist(shap, bins = bin)
    ax1.set(xlabel='Shape Ratio', ylabel='Frekuensi')
    
    conint = np.percentile(shap, [2.5, 97.5])
    y = np.linspace(0,50)
    x = [conint for i in y]
    ax1.plot(x,y)
    avr_sh = sum(shap)/len(shap)
    avr_shap = [avr_sh for i in y]
    ax1.plot(avr_shap,y)


    #----------------------------------------------------------------------
    #Menampilkan Plot
    #----------------------------------------------------------------------

    plt.show()


