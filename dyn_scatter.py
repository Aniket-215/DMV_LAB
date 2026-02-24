import matplotlib.pyplot as plt

x_input = input("Enter X values separated by space: ")
y_input = input("Enter Y values separated by space: ")

x = list(map(int, x_input.split()))
y = list(map(int, y_input.split()))

plt.scatter(x, y, color='red')
plt.title("Scatter Plot (User Input)")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.show()

