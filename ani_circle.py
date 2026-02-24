import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Create figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')

# Optional: draw the sine path for reference
x = np.linspace(0, 2 * np.pi, 400)
ax.plot(x, np.sin(x), '--', color='gray', alpha=0.5)

# Create the circle
circle = plt.Circle((0, 0), 0.15, fill=True, color='blue')
ax.add_patch(circle)

# Animation update function
def update(frame):
    x_pos = frame * 0.05
    y_pos = np.sin(x_pos)
    circle.center = (x_pos, y_pos)
    return circle,

# Animate
ani = animation.FuncAnimation(
    fig,
    update,
    frames=200,
    interval=30,
    blit=True
)

plt.show()
