import numpy as np

filename = "data/reslimits__poi_r.npz"
data = np.load(filename)
lst = data.files
for item in lst:
    for elem in data[item]:
        #print("$" + str(round(elem[1]*1000,2)) + "^{+" + str(round(elem[2]*1000,2)) + "}_{-" + str(round(elem[3]*1000,2)) + "}$")
        print(elem)

