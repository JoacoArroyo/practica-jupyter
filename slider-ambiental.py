import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider

def relocalizacion(x0):
        b = 20/3
        a = -(1/6)
        t = a*x0 + b
        return t

fig, ax = plt.subplots()
plt.title("Pendiente Neutra")
A = np.arange(10,40,0.3)
B = np.arange(5,0,-0.05)
t = 2.5
initial_x0 = 25 # primera parcela

G = plt.plot(A, B, "-r", lw=2)
plt.ylabel("Altura (km)")
plt.xlabel("Temperatura (K)")
plt.yticks([])
plt.xticks([])
l = plt.plot(initial_x0,t,"o",
                 color="purple",
                 ms=15,
                 alpha=0.75,
                 lw=2)[0]
ax =plt.axis([0,50,0,5])

axamp = plt.axes([0.1, 0.03, 0.8, 0.02])

# Slider
samp = Slider(axamp,"mover parcela", 
              10, 40, valinit=initial_x0)

def update(val):
    # x0 is the current value of the slider
    x0 = samp.val
    # armado de recta
    t = relocalizacion(x0)
    # update curve
    l.set_ydata (t)
    l.set_xdata (x0)
    # redraw canvas while idle
    fig.canvas.draw_idle()
    
# call update function on slider value change
samp.on_changed(update)


plt.show()
