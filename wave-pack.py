#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim

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

def betas(N): 
  bt=np.array([choose(N-1,k)/2**(N-1) for k in np.arange(N)])

  return bt

def psi(x,t,El,Eh,N,bt):
  """
  вычислить волновую функцию с энергией от El до Eh
  """
  
  E=np.linspace(El,Eh,N)
  k=np.sqrt(E)
  return np.sum([bt[l]*np.exp(1j*k[l]*x-1j*E[l]*t) for l in np.arange(N)], axis=0)

def animPsi(xmin=-3,xmax=5,tmax=100,El=3,Eh=5,N=2,bt=1,mode='r',dx=1e-2,dt=1e-2):
  """
  нарисовать эвольцию волнового мокета построеного из N мод в интервале [El;Eh]
  """
  xx=np.arange(xmin,xmax+dx,dx)
  y1=-1.0
  y2=1.0
  tm_tmpl="t=%03.2f"
  
  ps=lambda x,t: psi(x,t,El,Eh,N,bt)
  lbl="Time development of"
  
  lbl+=r" |ψ|²"
  f=lambda t: np.abs(ps(xx,t))**2
  y1=0.
  y2=1.1*np.amax(f(0))
  lbl+=f" with{N} modes"
  
  fig, ax=plt.subplots()
  line, =ax.plot(xx,f(0))
  tm_x=0.45
  tm_y=-0.10
  tm_txt=ax.text(tm_x,tm_y,'',transform=ax.transAxes)
  
  def init():
    ax.set_xlim(xmin,xmax)
    ax.set_ylim(y1,y2)
    return line,

  def animate(t):
    line.set_ydata(f(t))
    tm_txt.set_text(tm_tmpl % t)
    return line,tm_txt

  ani=anim.FuncAnimation(fig,animate,frames=np.arange(0,tmax+dt,dt),init_func=init,interval=10, repeat=False,blit=True,save_count=1500)

  #lbl+=f"\n{text}"
  plt.title(lbl)
  plt.grid(True)
  plt.show()
  
  return ani
