import matplotlib.pyplot as plt
import math

def f(x):
  y=math.cos(x)
  return y

def p(x):
  z=math.sin(x)
  return z

N=500 #jumper of jumps
A=0 #inicio
B=4*3.1416 #END

dx=(B-A)/N
x=range(N)
values=range(N+1)
x=A
X=[]
Y=[]
Z=[]
for jump in values:
    x=A+jump*dx
    y=f(x)
    z=p(x)
    X.append(x)
    Y.append(y)
    Z.append(z)
    print(x,y)

plt.plot(X,Y)
plt.scatter(X,Y,color="green")
plt.plot(X,Z)
plt.scatter(X,Z,color="red")
plt.show()