import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad
from numpy import sqrt, sin, cos, pi, exp, inf


def  Int_1(a):
    def Int1(x,a):
        return sqrt(x)/(1+exp(a+x))
    return quad(Int1,0,inf, args=(a))[0]

def  Int_2(a):
    def Int2(x,a):
        return sqrt(x)/exp(a+x)
    return quad(Int2,0,inf, args=(a))[0]

Int_1v=np.vectorize(Int_1)
Int_2v=np.vectorize(Int_2)

def ratio(a):
    return Int_2v(a)/Int_1v(a)-1

a=np.linspace(0,10,1000)
y=ratio(a)
plt.plot(a,y)
#plt.plot(a,(y>=0.1)*0.1)
plt.axhline(y = 0.1, color = 'r', linestyle = '-')
plt.axvline(x = a[y<0.1][0], color = 'r', linestyle = '-')

l="(1.22,0.1)"

plt.text(1.3,0.11,l)
plt.text(0.25,2.5,"The error<0.1 for $(E_C - E_F)/K_BT$>1.22 ")
plt.xlabel("$(E_C - E_F)/K_BT$")
plt.ylabel('Error')
plt.title('Reative error in determination of electron density')
plt.grid()
plt.show()

plt.savefig('q2.jpg')