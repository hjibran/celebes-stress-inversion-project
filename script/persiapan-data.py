# ----------------------------------------------------------------#
# this code was created to determine the seed value that          # 
# will be used in each cluster                                    #
# the best seed is the seed with  mean standar deviation          #
# ----------------------------------------------------------------#
import pandas as pd

data = pd.read_csv("/mnt/d/celebes-stress-inversion-project/data/siap-olah/data-gabungan.csv")


hasil = data[data['depth']<=50]
hasil.to_csv("/mnt/d/celebes-stress-inversion-project/data/siap-olah/gempa50km.csv", index=False)

hasil = hasil[hasil['str1']>=0]
hasil.to_csv("/mnt/d/celebes-stress-inversion-project/data/siap-olah/fm50km.csv", index=False)

aki = hasil.iloc[:, [3, 2, 4, 6, 7, 8, 5]]
aki.columns = ["longitude", "latitude", "depth", "strike", "dip", "rake", "magnitude"]
#aki.rename(
#    columns={"lon": "longitude", "lat": "latitude", "depth": "depth", "str1": "strike", "dip1": "dip", "rake1": "rake","mw": "magnitude"},
#    inplace=True
#)
aki.to_csv("/mnt/d/celebes-stress-inversion-project/data/siap-olah/aki.csv", index=False)