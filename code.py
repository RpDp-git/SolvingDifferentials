import numpy as np
import matplotlib.pyplot as plt

def f_x_y(x):
    return np.cos(x)
h=0.1
x0,y0=0,0
sol_euler=np.zeros((3,100))
sol_rk=np.zeros((2,100))

i=1
# Euler Method
while i<=100:
    dy=f_x_y(x0)
    y1=y0+(h*dy)
    x1=x0+h
    sol_euler[0][i-1]=x1
    sol_euler[1][i-1]=y1
    sol_euler[2][i-1]=np.sin(x1) # Actual solution
    x0,y0=x1,y1
    i+=1
# Runge-Kutta 4th Order method
i=1
x0,y0=0,0
while i<=100:
    k1=h*f_x_y(x0)
    k2=h*f_x_y(x0+(h/2))
    k3=h*f_x_y(x0+(h/2))
    k4=h*f_x_y(x0+(h))
    x1=x0+h
    y1=y0+((1/6)*(k1+(2*k2)+(2*k3)+k4))
    sol_rk[0][i-1]=x1
    sol_rk[1][i-1]=y1
    x0,y0=x1,y1
    i+=1

plt.plot(sol_euler[0],sol_euler[1],"bx",label="Euler_Method",markersize=3)
plt.plot(sol_euler[0],sol_euler[2],"r-",label="Analytical Sol")
plt.plot(sol_rk[0],sol_rk[1],"go",label="RungeKutta_Method",markersize=3)
plt.legend(loc="lower right")
plt.show()
