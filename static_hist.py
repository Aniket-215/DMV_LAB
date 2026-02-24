import numpy as np
import matplotlib.pyplot as plt

data = np.array([12, 15, 13, 17, 19, 21, 22, 25, 30, 18, 16, 14, 20])
bins = 5

plt.figure(figsize=(8, 5))
plt.hist(data, bins=bins, color='blue', edgecolor='black')

plt.title("Static Histogram")
plt.xlabel("Values")
plt.ylabel("Frequency")

plt.show()
