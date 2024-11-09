#1/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt


def findZero(fn,l=-1,r=1,b=-1,t=1,eps=1e-12):
    """
    Find zero of givenfunction in given widow
    """
    N=10
    dx=(r-l)/(N-1)
    dy=(t-b)/(N-1)
    while dx>eps or dy>eps:
        x=np.linspace(l,r,N)
        y=np.linspace(b,t,N)
        XX,YY=np.meshgrid(x,y)
        W=fn(XX,YY)
        mn=np.min(W)
        ij=(W==mn)
        x0,y0=XX[ij],YY[ij]
        x0,y0=x0[0],y0[0]   #min vidaet masiv
        if mn<eps:
            return np.array([x0,y0])
        l=x0-0.5*dx
        r=x0+0.5*dx
        b=y0-0.5*dy
        t=y0+0.5*dy
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


def ampC1(E,a=1,u0=20):
  k=np.emath.sqrt(E)
  kp=np.emath.sqrt(E+u0)
  return np.exp(1j*(k-kp)*a)*(1+k/kp)*ampD(E,a,u0)*0.5


def ampC2(E,a=1,u0=20):
  k=np.emath.sqrt(E)
  kp=np.emath.sqrt(E+u0)
  return np.exp(1j*(k+kp)*a)*(1-k/kp)*ampD(E,a,u0)/2


def ampB(E,a=1,u0=20):
  k=np.emath.sqrt(E)
  kp=np.emath.sqrt(E+u0)
  return 1j*np.sin(kp*a)*(kp/k-k/kp)*np.exp(1j*k*a)*ampD(E,a,u0)*0.5


def spectre(E,a=1,u0=20):
    kap=np.emath.sqrt(-E)
    kp=np.emath.sqrt(E+u0) 
    return 2*np.cos(kp*a)+(kap/kp-kp/kap)*np.sin(kp*a)


def psi(x,E,a=1,u0=20):
    """
    Calculate wave function of scattaring beam
    """
    D=ampD(E,a,u0)
    C1=ampC1(E,a,u0)
    C2=ampC2(E,a,u0)
    B=ampB(E,a,u0)

    ind1=x<0
    ind2=(x>=0)&(x<a)
    ind3=x>a
    
    k=np.emath.sqrt(E)
    kp=np.emath.sqrt(E+u0)

    x1=x[ind1]
    x2=x[ind2]
    x3=x[ind3]

    z1=np.exp(1j*k*x1)+B*np.exp(-1j*k*x1)
    z2=C1*np.exp(1j*kp*x2)+C2*np.exp(-1j*kp*x2)
    z3=D*np.exp(1j*k*x3)

    return np.r_[z1,z2,z3]
