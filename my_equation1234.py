# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from scipy.integrate import odeint
import numpy as np
def f(u,t):
  return (u[1],-0.2*u[1]-t**3+t+0.33*np.cos(1.2*t))
x0=[0.24,0]
ts=np.linspace(0,120,100)
us=odeint(f,x0,ts)
xs=us[:,0]
plt.figure(figsize=(10,6))
plt.plot(ts,xs,"-")
plt.plot(ts,xs,"ro")
plt.xlabel("x_values")
plt.ylabel("yvalues")
plt.title("Differntial Equation Plot")
plt.show()

## For second one
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import numpy as np
def f(u,t):
  return (u[1],(-0.2*u[1])-t**3+t)
x0=[0.24,0]
ts=np.linspace(0,120,100)
us=odeint(f,x0,ts)
xs=us[:,0]
plt.figure(figsize=(10,6))
plt.plot(ts,xs,"-")
plt.plot(ts,xs,"ro")
plt.xlabel("x_values")
plt.ylabel("yvalues")
plt.title("Differntial Equation Plot")
plt.show()

