'''
def fault_mechanism(strike, dip, rake):

    import subprocess

    # Menjalankan perintah Bash menggunakan subprocess.run()
    result = subprocess.run(
        ['bash', '-c', "echo {} {} {} {} {} {} {} X Y {} | python3 /mnt/d/celebes-stress-inversion-project/FMC-master/FMC.py -i AR "\
         .format("10", "10", "10", strike, dip, rake, "4.0", "tes")],  # Perintah Bash yang ingin dijalankan
        stdout=subprocess.PIPE,  # Menangkap output dari perintah
        stderr=subprocess.PIPE,  # Menangkap error (jika ada)
        text=True  # Agar hasilnya berupa string (bukan bytes)
    )
    
    hasil = result.stdout; words = hasil.rsplit(' ', 1)
    word = words[-1].strip()


    return word
 
def simpson_index(strike, dip, rake, sigma):

    import os
    import numpy as np
    import pandas as pd

    type = fault_mechanism(strike, dip, rake)
    R = (sigma[1]-sigma[0])/(sigma[2]-sigma[0])

    if type == "N":
        k = 0
        AR = (k+0.5)+((-1**k)*(R-0.5))
    elif type == "N-SS":
        k = 0
        AR = (k+0.5)+((-1**k)*(R-0.5))
    elif type == "SS-N":
        k = 1
        AR = (k+0.5)+((-1**k)*(R-0.5))
    elif type == "SS":
        k = 1
        AR = (k+0.5)+((-1**k)*(R-0.5))
    elif type == "SS-R":
        k = 1
        AR = (k+0.5)+((-1**k)*(R-0.5))
    elif type == "R-SS":
        k = 2
        AR = (k+0.5)+((-1**k)*(R-0.5))
    elif type == "R":
        k = 2
        AR = (k+0.5)+((-1**k)*(R-0.5))    

    return AR

'''

def fault_mechanism(strike, dip, rake):

    import subprocess

    # Menjalankan perintah Bash menggunakan subprocess.run()
    result = subprocess.run(
        ['bash', '-c', "echo {} {} {} {} {} {} {} X Y {} | python3 /mnt/d/celebes-stress-inversion-project/FMC-master/FMC.py -i AR "\
         .format("10", "10", "10", strike, dip, rake, "4.0", "tes")],  # Perintah Bash yang ingin dijalankan
        stdout=subprocess.PIPE,  # Menangkap output dari perintah
        stderr=subprocess.PIPE,  # Menangkap error (jika ada)
        text=True  # Agar hasilnya berupa string (bukan bytes)
    )
    
    hasil = result.stdout; words = hasil.rsplit(' ', 1)
    word = words[-1].strip()

    if word == "N":
        k = 0
    elif word == "N-SS":
        k = 0
    elif word == "SS-N":
        k = 1
    elif word == "SS":
        k = 1
    elif word == "SS-R":
        k = 1
    elif word == "R-SS":
        k = 2
    elif word == "R":
        k = 2 

    return k
 
def simpson_index(k, sigma):

    import os
    import numpy as np
    import pandas as pd

    R = (sigma[1]-sigma[0])/(sigma[2]-sigma[0])
    AR = (k+0.5)+((-1**k)*(R-0.5))

    return AR