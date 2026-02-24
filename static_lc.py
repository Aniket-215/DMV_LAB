import numpy as np
import matplotlib.pyplot as plt

x_axis = [10, 20, 30, 40, 50]
y_axis = [5, 7, 11, 15, 28]

plt.figure(figsize=(8, 5))
plt.plot(x_axis, y_axis, marker='o')

plt.title("Static Line Chart")
plt.xlabel("x-axis")
plt.ylabel("y-axis")

plt.show()
