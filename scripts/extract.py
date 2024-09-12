import numpy as np

filename = "/home/bruno/Downloads/reslimits__poi_r.npz"
data = np.load(filename)
lst = data.files
for item in lst:
    for elem in data[item]:
        print(round(elem[1]*1000,2))
