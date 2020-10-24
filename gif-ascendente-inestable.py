import numpy as np
import matplotlib.pyplot as plt
import random
from matplotlib import pyplot as plt
import gif

A=np.arange(10,40,0.3)
B=np.arange(5,0,-0.05)
C=np.arange(4,1,-0.03)
j = 25

@gif.frame
def puntito(i):
        global j
        b = 20/3
        a = -(1/6)
        t = a*j + b
        plt.scatter(j,t)
        plt.plot(A,B,"red")
        plt.plot(A,C,"g--")
        plt.ylabel("Altura (km)")
        plt.xlabel("Temperatura (K)")
        plt.title("pendiente inestable")
        plt.yticks([])
        plt.xticks([])
        j = j - 0.5
        # plt.show()

pepito = list()
for i in range(14):
    frame = puntito(i)
    pepito.append(puntito(i))
    
gif.save(pepito, "parcela ascendente - inestable.gif", duration=100)
