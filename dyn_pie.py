import matplotlib.pyplot as plt

labels_input = input("Enter labels separated by space: ")
sizes_input = input("Enter values separated by space: ")

labels = labels_input.split()
sizes = list(map(int, sizes_input.split()))

plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Pie Chart (User Input)")
plt.show()
