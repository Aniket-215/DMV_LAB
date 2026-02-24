import numpy as np
import matplotlib.pyplot as plt

x_input = input("Enter X values separated by space: ")
y_input = input("Enter Y values separated by space: ")

x_axis = np.array(list(map(int, x_input.split())))
y_axis = np.array(list(map(int, y_input.split())))

plt.figure(figsize=(8, 5))
plt.plot(x_axis, y_axis, marker='o')

plt.title("Dynamic Line Chart")
plt.xlabel("x-axis")
plt.ylabel("y-axis")

plt.show()
