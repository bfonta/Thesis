import numpy as np

filename = "data/reslimits__poi_r.npz"
data = np.load(filename)
lst = data.files
for item in lst:
    for elem in data[item]:
        # convert to latex format
        #print("$" + str(round(elem[1]*1000,2)) + "^{+" + str(round(elem[2]*1000,2)) + "}_{-" + str(round(elem[3]*1000,2)) + "}$")

        # convert to json format
        mes = '"' + str(elem[0]) + '": {\n'
        mes += '    "limit_m2": ' + str(elem[5]) + ',\n'
        mes += '    "limit_m1": ' + str(elem[3]) + ',\n'
        mes += '    "limit_p1": ' + str(elem[2]) + ',\n'
        mes += '    "limit_p2": ' + str(elem[4]) + ',\n'
        mes += '    "observed": X,\n'
        mes += '    "limit": ' + str(elem[1]) + ',\n'
        mes += '},\n'
        print(mes)

