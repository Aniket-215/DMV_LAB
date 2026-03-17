import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

speed = float(input("Enter circle speed (example 0.05): "))
frames = int(input("Enter number of frames (example 200): "))

fig, ax = plt.subplots()
ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')

x = np.linspace(0, 2 * np.pi, 400)
ax.plot(x, np.sin(x), '--', color='Red', alpha=0.5)

circle = plt.Circle((0, 0), 0.15, color='Green')
ax.add_patch(circle)

def update(frame):
    x_pos = frame * speed
    y_pos = np.sin(x_pos)
    circle.center = (x_pos, y_pos)
    return circle,

ani = animation.FuncAnimation(
    fig,
    update,
    frames=frames,
    interval=30,
    blit=True
)

plt.title("Dynamic Animated Circle")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()
