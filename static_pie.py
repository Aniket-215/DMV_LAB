import matplotlib.pyplot as plt

labels = ['A', 'B', 'C', 'D']
sizes = [25, 35, 20, 20]

plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Pie Chart")
plt.show()
