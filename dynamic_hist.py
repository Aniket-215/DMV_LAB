import numpy as np
import matplotlib.pyplot as plt

data_input = input("Enter values separated by space: ")
data = np.array(list(map(int, data_input.split())))

bins = int(input("Enter number of bins: "))

plt.figure(figsize=(8, 5))
plt.hist(data, bins=bins, color='blue', edgecolor='black')

plt.title("Dynamic Histogram")
plt.xlabel("Values")
plt.ylabel("Frequency")

plt.show()
