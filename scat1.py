#1/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt


def ampD(E,a=1,u0=20):
    """
    Compute scate tering cumplitude
    for gvin energy and set hidth
    and dipth of the well
    2m=1
    h=1
    """
    k=np.emath.sqrt(E)
    kp=np.emath.sqrt(E+u0)
    return 2*np.exp(-1j*k*a)/(2*np.cos(kp*a)-1j*(k/kp+kp/k)*np.sin(kp*a))

def ampD2(E,a=1,u0=20):
    """

    Ветвь с особеностями!!!!!!!!!!!

    Compute scate tering cumplitude
    for gvin energy and set hidth
    and dipth of the well
    2m=1
    h=1
    """
    k=np.emath.sqrt(E)
    kp=np.emath.sqrt(E+u0)
    return 2*np.exp(1j*k*a)/(2*np.cos(kp*a)+1j*(k/kp+kp/k)*np.sin(kp*a))

def spectre(E,a=1,u0=20):
    kap=np.emath.sqrt(-E)
    kp=np.emath.sqrt(E+u0) 
    return 2*np.cos(kp*a)+(kap/kp-kp/kap)*np.sin(kp*a)
