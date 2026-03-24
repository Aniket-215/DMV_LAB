import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

df = pd.read_csv('movies_cleaned.csv')
df.columns = df.columns.str.strip()

x = df['movieId']

y = x * 0.5 + np.random.normal(0, 50, len(x))

data = pd.DataFrame({'x': x, 'y': y})

data_clean = data.dropna()

kmeans = KMeans(n_clusters=3, random_state=0)
data_clean['cluster'] = kmeans.fit_predict(data_clean[['x', 'y']])

Q1 = data_clean['y'].quantile(0.25)
Q3 = data_clean['y'].quantile(0.75)
IQR = Q3 - Q1
outliers = data_clean[(data_clean['y'] < Q1 - 1.5*IQR) | (data_clean['y'] > Q3 + 1.5*IQR)]

plt.scatter(data_clean['x'], data_clean['y'], c=data_clean['cluster'])
plt.scatter(outliers['x'], outliers['y'], color='red', label='Outliers')

plt.xlabel('Movie ID')
plt.ylabel('Generated Y')
plt.title('Cluster + Outliers + Correlation')
plt.legend()
plt.show()