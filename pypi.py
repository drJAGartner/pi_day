##### ##### ##### ##### #####
# pypi.py
# numeric estimation in numpy
# because I can't eat your
# treats
##### ##### ##### ##### #####

import numpy as np
import matplotlib.pyplot as plt
from random import random as ayn
from math import sqrt

def estimate_pi(n_itt):
    n_in = 0.
    for j in range(n_itt):
        x = ayn()
        y = ayn()
        r = sqrt(x*x+y*y)
        if r <=1:
            n_in = n_in + 1.
    return 4.*n_in/float(n_itt)

if __name__ == "__main__":
    n_itt = [1000, 10000, 100000]#, 1000000]
    dist_pi = []
    for n in n_itt:
        l_pi = []
        for _ in range(1000):
            l_pi.append(estimate_pi(n))
        dist_pi.append(np.array(l_pi))

    bins = np.linspace(3.04, 3.24, 100)
    plt.figure()
    plt.hist(dist_pi[0], bins, normed=0, fill=False, edgecolor="purple", label="N=1,000", linewidth=3)
    plt.hist(dist_pi[1], bins, normed=0, fill=True, color="blue", edgecolor="blue", label="N=10,000", linewidth=2)
    plt.hist(dist_pi[2], bins, normed=1, fill=False, edgecolor="red", label="N=100,000", linewidth=1)
    plt.axvline(x=3.14159265359, color='g', linestyle='dashed', label="pi",linewidth=2)
    #plt.hist(dist_pi[3], bins, normed=1, fill=False, edgecolor="green", label="N=1,000,000", linewidth=1)
    #plt.yscale('log')
    plt.xlabel("Estimated Pi Value")
    plt.ylabel("Frequency")
    plt.title('Estimating Pi by Throwing Darts')
    plt.legend(loc="upper left")
    plt.show()


