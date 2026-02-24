import matplotlib.pyplot as plt

categories_input = input("Enter categories separated by space: ")
values_input = input("Enter values separated by space: ")

categories = categories_input.split()
values = list(map(int, values_input.split()))

plt.bar(categories, values, color='orange')
plt.title("Bar Chart (User Input)")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()
