# Coding: utf-8

_all_ = [ 'tunable_parameter' ]

import csv
import argparse

import matplotlib; import matplotlib.pyplot as plt
import mplhep as hep
plt.style.use(hep.style.ROOT)

def tunable_parameter():
    param, ratio = [], []
    with open('data/tunable_parameter_copy.csv', newline='') as csvfile:
        r = csv.reader(csvfile, delimiter=',')
        next(r)
        for row in r:
            param.append(float(row[0]))
            ratio.append(float(row[1]))

    fig, ax = plt.subplots(1, figsize=(12,6))
    plt.subplots_adjust(wspace=0, hspace=0)

    # hep.cms.lumitext("Bye-splits algorithm", fontsize=19)

    # plots
    ax.plot([0., 1.], [ratio[-1],ratio[-1]], '-', linewidth=3, label="CMSSW", color="blue")
    ax.plot(param, ratio, '.', markersize=20, label="Bye-splits", color="red")

    # grid
    ax.grid()
    lines = ax.get_xgridlines() + ax.get_ygridlines()
    for line in lines:
        line.set_dashes([8, 4])  # dash length, space between dashes

    ax.set_ylabel(r"Ratio of cluster splits", fontsize=20)
    ax.set_xlabel(r"Tunable parameter $\lambda$", fontsize=20)
    leg = ax.legend(loc="lower right")
    for line in leg.get_lines():
        line.set_linewidth(5)
    plt.tight_layout()
    fig.savefig("TunableParameter.pdf")
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Plot tunable parameter of bye-splits HGCAL algorithm.",
                                     formatter_class=argparse.RawTextHelpFormatter)
    FLAGS = parser.parse_args()
    tunable_parameter()
