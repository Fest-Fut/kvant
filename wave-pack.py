#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt

def choose(n,k):
    """
    return number of combinetion from n by k
    """

    if k<n-k:
        return np.prod(np.arange(n,n-k,-1)/np.arange(k,0,-1))
    return np.prod(np.arange(n,k,-1)/np.arange(n-k,0,-1))

def weight(n):
    """
    return list of binomial weight
    """
    return[choose(n,k)/2**n for k in np.arange(n+1)]

def bnSampling(n):
    """
    return luts of n+1 point in [0,1] (normirovka)
    """
    x=np.arange(n+1)/n
    y=weight(n)
    return x,y


