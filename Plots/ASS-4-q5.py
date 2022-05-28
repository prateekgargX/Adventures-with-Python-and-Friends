from cv2 import sqrt
import numpy as np
import matplotlib.pyplot as plt

def nc(T,r_dse=1.09):
    return 2.54*(10**19)*(r_dse**1.5)*((T/300)**1.5)

def nv(T,r_dsh=1.15):
    return 2.54*(10**19)*(r_dsh**1.5)*((T/300)**1.5)

def Eg(T,alpha=4.73*(10**(-4)),beta=636,Eg_o=1.17):
    return Eg_o-alpha*T*T/(beta+T) 

def KbT(T):\
    return 26*(10**-3)*(T/300)

def n_i(T):
    return np.sqrt(nc(T)*nv(T))*np.exp(-Eg(T)/KbT(T)/2)

def e(T,Nd=10**17,Na=10**16):
    return (Nd-Na)/2+sqrt(((Nd-Na)/2)**2+n_i(T)**2)

def h(T,Nd=10**17,Na=10**16):
    return (Na-Nd)/2+sqrt(((Nd-Na)/2)**2+n_i(T)**2)

t=np.linspace(200,1000,1000)

y=e(t)
plt.plot(t,y)
y=h(t)
print(y)
plt.plot(t,y)
plt.grid()
plt.xlabel("$T$")
plt.ylabel('Number')
plt.title('Q6')
plt.show()
plt.legend(["electrons","holes"])
plt.savefig("q5.png")

