#1/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt


def findZero(fn,l=-1,r=1,b=-1,t=1,aeps=1e-12,beps=1e-11):
    """
    Find zero of givenfunction in given widow
    """
    N=10
    dx=(r-l)/(N-1)
    dy=(t-b)/(N-1)
    while dx>beps or dy>beps:
        x=np.linspace(l,r,N)
        y=np.linspace(l,t,N)
        XX,YY=np.meshgrid(x,y)
        W=fn(XX,YY)
        mn=np.min(W)
        ij=(W==mn)
        x0,y0=XX[ij],YY[ij]
        x0,y0=x0[0],y0[0]   #min vidaet masiv
        if mn<aeps:
            return np.array([x0,y0])
        l=xo-0.5*dx
        r=xo+0.5*dx
        b=xo-0.5*dy
        t=xo+0.5*dy
        dx=(r-l)/(N-1)  # dx=dx/(N-1)
        dy=(t-b)/(N-1)  # dx=dx/(N-1)

    print("[EROR] funtuion seems cloes not have zero in given range")
    return (0,0)

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

def psi(x):
    """
    plot wave function
    """
    pass

