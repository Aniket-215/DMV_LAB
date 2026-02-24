import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig, ax = plt.subplots()
ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-1.5, 1.5)

x = np.linspace(0, 2 * np.pi, 200)
line, = ax.plot(x, np.sin(x), lw=2)

def update(frame):
    y = np.sin(x + frame * 0.1)
    line.set_ydata(y)
    return line,

ani = animation.FuncAnimation(
    fig,
    update,
    frames=200,
    interval=30,
    blit=True
)

plt.show()
