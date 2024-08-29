# Coding: utf-8

_all_ = [ 'br_dependence' ]

"""
Parameterisation taken from https://arxiv.org/pdf/1607.04251
"""

import os
import argparse
import numpy as np

import matplotlib; import matplotlib.pyplot as plt
plt.style.use('tableau-colorblind10')
import mplhep as hep
plt.style.use(hep.style.ROOT)

def c1(particle):
    return {'gamma': 0.0049,
            'Z': 0.0083,
            'W': 0.0073,
            'fermion': 0.,
            'gluon': 0.0066}[particle]

def br_single_higgs(particle):
    return {'b': 0.5809,
            'W': 0.2153,
            'gluon': 0.0818,
            'tau': 0.0627,
            'c': 0.0288,
            'Z': 0.02641,
            'gamma': 0.2270,
        }[particle]

def br_parameterisation(x, particle):
    return (x-1)*(c1(particle)-2E-3) / (1 + 2E-3*(x-1))
    
def br_dependence(mode):
    x = np.linspace(-20.5, 20.5, 1000)

    if mode == 'h':
        particles = {'fermion', 'gluon', 'W', 'Z', 'gamma'}
        labels = {'gamma'  : r"$H\rightarrow\gamma\gamma$",
                  'Z'      : r"$H\rightarrow ZZ$",
                  'W'      : r"$H\rightarrow WW$",
                  'fermion': r"$H\rightarrow f\bar{f}$",
                  'gluon'  : r"$H\rightarrow gg$"}
    else:
        particles = {'fermion', 'W', 'Z', 'gamma'}
        labels = {'gamma'  : r"$HH \rightarrow f\bar{f}\, \gamma\gamma$",
                  'Z'      : r"$HH \rightarrow f\bar{f}\, ZZ$",
                  'W'      : r"$HH \rightarrow f\bar{f}\, WW$",
                  'fermion': r"$HH \rightarrow f\bar{f}\, f\bar{f}$"}
        

    if mode == 'h':
        brs = {k: br_parameterisation(x, k) for k in particles}
    else:
        brs = {'fermion': br_parameterisation(x, 'fermion')**2,
               'gamma': br_parameterisation(x, 'fermion')*br_parameterisation(x, 'gamma'),
               'Z': br_parameterisation(x, 'fermion')*br_parameterisation(x, 'Z'),
               'W': br_parameterisation(x, 'fermion')*br_parameterisation(x, 'W'),
               }

    fig, ax = plt.subplots(1)
    plt.subplots_adjust(wspace=0, hspace=0)
    suffix = "Single" if mode=='h' else "Double"
    hep.cms.lumitext(suffix + " Higgs", fontsize=19)

    # horizontal lines
    line_opt = dict(color="grey", linestyle="--")        
    if mode == 'h':
        values = [-10., -5., 0., 5., 10.]
    else:
        values = [0.,]
    for val in values:
        ax.axhline(y=val, **line_opt)
    ax.axvline(x=0., **line_opt)

    # curves
    for k in particles:
        ax.plot(x, 100*brs[k], '-', linewidth=3, label=labels[k])

    ax.set_ylabel(r"$\delta BR$ [%]", fontsize=20)
    ax.set_xlabel(r"$\kappa_{\lambda}$", fontsize=20)
    leg = ax.legend(loc="lower right")
    for line in leg.get_lines():
        line.set_linewidth(5)
    fig.savefig("BRdependence_" + suffix + "Higgs.pdf")
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="draw cuts on top of signal or MC distributions",
                                     formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('--mode', choices=('h', 'hh'), default='hh', type=str, help='single or double Higgs process.')
    FLAGS = parser.parse_args()

    br_dependence(FLAGS.mode)