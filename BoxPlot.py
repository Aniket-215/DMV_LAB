import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('movies_cleaned.csv')

df.columns = df.columns.str.strip()

data = df['movieId']

plt.boxplot(data.dropna())
plt.xlabel('Movie ID')
plt.title('Box Plot of Movie IDs')
plt.xlabel("Values")
plt.ylabel("Movies ID")
plt.show()
