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

    return Mean, Confidence_Interval

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