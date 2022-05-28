import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1/(1+np.exp(x))

def fds(T,Ef=0,n=1000):
    KbT=0.026*T/300
    x=np.linspace(-0.2,Ef+0.2,n)-Ef
    y=sigmoid(x/KbT)
    return x,y

x,y =fds(300)
plt.plot(x,y)
x,y =fds(150)
plt.plot(x,y)
x,y =fds(0.01)
plt.plot(x,y)
plt.grid()
plt.legend(['T = 300K','T = 150K','T = 0K'])
plt.show()
