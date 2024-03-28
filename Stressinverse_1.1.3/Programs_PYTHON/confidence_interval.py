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

