import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from sympy import symbols, solve, Eq

Nd=10**17
Na=10**16

def nc(T,r_dse=1.09):
    return 2.54*(10**19)*(r_dse**1.5)*((T/300)**1.5)

def nv(T,r_dsh=1.15):
    return 2.54*(10**19)*(r_dsh**1.5)*((T/300)**1.5)

def Eg(T,alpha=4.73*(10**(-4)),beta=636,Eg_o=1.17):
    return Eg_o-alpha*T*T/(beta+T) 

def Ef(T,Ec,Ev=0,r_ds=1.055):
    return (Ec+Ev)/2+KbT(T)*sp.log(r_ds)

def KbT(T):
    return 26*(10**-3)*(T/300)

def e(T,Ec):
    return nc(T)*sp.exp((Ef(T,Ec)-Ec)/KbT(T))

def h(T,Ec):
    return nv(T)*sp.exp((-Ef(T,Ec))/KbT(T))

def nd_i(T,Ed,Ec):
    return Nd/(1+2*sp.exp((Ed-Ef(T,Ec))/KbT(T)))

def na_i(T,Ea,Ec):
    return Na/(1+4*sp.exp((Ef(T,Ec)-Ea)/KbT(T)))


T=300
Ec,Ed,Ea=symbols('Ec Ed Ea')

eq1=Eq(na_i(T,Ea,Ec)+e(T,Ec)-nd_i(T,Ed,Ec)-h(T,Ec),0)
eq2=Eq(Ec-Ed-50*(10**-3),0)
eq3=Eq(Ea-25*(10**-3),0)

solve((eq1,eq2,eq3),(Ec,Ed,Ea))
