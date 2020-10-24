import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider

def tangente(x0, x):
    '''
    devuelve la recta tangente a+b*x a partir de elegir
    donde toca a la parabola x**2
    x0: lugar donde toca
    '''
    # calculo de la recta tangente a la parabola
    b = 2 * x0
    a = - x0**2
    # devuelvo todos los puntos de la recta
    return a + b * x

## %% primero testeo para ver que se ve bien
#fig, ax = plt.subplots()
#plt.title("testeo estatico para ver que da")
#x = np.arange(0.0, 50)
#y = x**2
#G = plt.plot(x, y, "-b", lw=2)
#x0 = 25
#plt.plot(x, tangente(x0, x), "-b", lw=1)
#plt.plot(x, tangente(x0 + 10, x), "-b", lw=1)
#plt.plot(x, tangente(x0 - 10, x), "-b", lw=1)
#initial_x0 = 25 # donde meter la tangente
## saco los valores de la recta tangente
#plt.grid("true")

# %% ahora hago la animacion con slider

fig, ax = plt.subplots()
plt.title("animeichon")
x = np.arange(0.0, 50)
y = x**2
G = plt.plot(x, y, "-b", lw=2)
ax =plt.axis([0,50,0,2500])

initial_x0 = 25 # donde meter la tangente
# saco los valores de la recta tangente
t = tangente(initial_x0, x)
l, = plt.plot(x, t, "-r", lw=1)
initial_x0 = 25
plt.grid("true")

axamp = plt.axes([0.1, 0.03, 0.8, 0.02])

# Slider
samp = Slider(axamp,"donde toca", 
              0, 50, valinit=initial_x0)

def update(val):
    # x0 is the current value of the slider
    x0 = samp.val
    # nueva tangente
    t = tangente(x0, x)
    # update curve
    l.set_ydata(t)
    # redraw canvas while idle
    fig.canvas.draw_idle()
    
# call update function on slider value change
samp.on_changed(update)


plt.show()
