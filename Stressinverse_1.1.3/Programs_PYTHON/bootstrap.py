#!/home/haidir/celebes-stress-inversion-project/venv/bin/python3
import numpy as np
from random import choice
import types
import confidence_interval as ci

contoh = np.array([139.8404617,139.5509069,140.2941841,138.0727561,137.5543228,
136.3292709,139.3187813,139.0754201,138.5592962,137.8894997,
137.5289169,138.179811,138.6063408,138.0417674,139.0196074,
138.4957115,138.2404931,138.5660065,139.7184881,138.3882046,
136.6430711,136.7286167,137.3018151,139.2585973,136.7454619,
138.7214654,141.3734539,138.7666373,139.0971023,137.5288694,
139.8228765,140.0984881,138.1534703,137.6635055,137.6091939,
139.315861,138.870009,138.8389118,138.0448621,139.4225608,
137.2671086,137.364386,138.7562721,140.6625756,138.3558322,
138.0893663,138.7671487,136.7426409,138.7263486,138.1758609,
137.1221386,138.4007119,140.407878,138.7013422,140.1676841,
137.7232701,138.6576684,137.9787072,137.3467515,137.5039464,
138.7880458,138.6504448,138.643881,139.0449739,137.9259992,
139.5551287,137.7740983,140.4241506,139.9298328,136.2713557,
139.2086609,138.1657272,137.0927241,138.4759881,138.5264332,
138.2942946,138.3003477,140.3267768,136.8246696,140.4494547,
136.7753224,136.749507,139.4048077,137.8931022,137.9498288,
138.5566384,137.6837278,137.6760053,137.7099792,139.0362539,
137.7287419,138.8605043,137.7060014,137.9607956,138.413662,
138.4651883,137.9048642,139.7318014,138.5947903,138.4864743,
137.978646,137.5165186,137.194014,138.6722278,138.4060127,
139.7663088,138.3507065,138.822104,138.3484701,139.057067,
139.3905219,138.3020218,138.4267419,138.6385593,139.059055,
138.0855548,137.664766,140.6079055,137.8134235,138.4300083,
137.7041374,138.3954073,137.3008784,138.6475394,139.162509,
138.9117658,137.3210628,138.8109531,138.20969,138.3430065,
136.489531,138.1341353,138.015084,138.0042836,138.1422752,
138.3549716,140.3992438,138.3097388,139.2988608,139.6199617,
139.0978489,136.9466609,139.3392177,138.3994973,140.0041135,
137.8086615,140.1696519,139.4023288,138.5739068,138.1751365,
139.6407287,139.5376693,139.5845885,139.4386068,139.2384451,
139.6038876,139.7747582,138.3302384,139.7563113,138.9656871,
138.9408651,139.0436228,137.7769263,139.3755461,140.1655087,
138.8191582,137.1368022,137.7101829,137.1144857,136.2938898,
138.9723313,136.8934644,138.6665652,139.4642699,137.8894636,
137.8196851,138.9943738,138.4895173,140.1199864,139.4752989,
138.2398026,138.6084416,139.6479932,138.0138942,138.2201749,
139.355235,139.3472609,138.8537975,139.470698,137.7708647,
138.0224184,137.2562247,139.4427676,140.2571354,139.333542,
138.4974314,140.736437,139.2204794,137.72382,138.7647699,
138.4407529,138.7655346,139.0026509,138.7740719,138.0149957,
137.5326336,139.3534668,137.9579313,138.2358226,141.0656116,
138.4970618,139.2371444,140.350854,139.4269913,138.799751,
139.129337,139.0330179,140.3159617,138.8977962,137.8740783,
138.0905401,138.913436,138.5376782,139.62189,134.9519367,
138.5214804,138.3046534,137.02061,139.9898175,137.1750417,
139.8668537,139.4152852,139.7703792,139.2422196,137.1710893,
137.4977807,137.7796002,137.4256016,139.564599,138.7533349,
137.7692263,138.5175498,137.7057261,137.454863,140.5897316,
138.4687847,138.3409197,138.5401375,137.9240039,138.9262956])

def bootstrap(sample, iteration):
    indx = [i for i in range(len(sample))]
    means=[]
    for i in range(iteration):
        bootstraping = np.array([choice(indx) for i in range(len(sample))])
        value = sample[bootstraping]
        mean = sum(value)/len(value)
        means.append(mean)
    return(means)    

def histrogram(sample, bin):
    import matplotlib.pyplot as plt
    import numpy as np

    # Membuat histogram
    plt.hist(sample, bins=bin, edgecolor='black')

    # Memberikan label pada sumbu
    plt.xlabel('Nilai')
    plt.ylabel('Frekuensi')
    plt.title('Histogram')

    # Menampilkan plot
    plt.show()

rerata = bootstrap(contoh,10000)

mean, CI = ci.confidence_interval(contoh)
print('{:.3f} +_ {:.3f}'.format(mean, CI))

histrogram(contoh,25)