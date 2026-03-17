import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("movies.csv")

df.columns = df.columns.str.strip()

print("=== First 5 Rows ===")
print(df.head())

print("\n=== Data Info ===")
print(df.info())

print("\n=== Missing Values Count ===")
print(df.isnull().sum())

print("\n=== Any Missing Values? ===")
print(df.isnull().any())

missing_rows = df[df.isnull().any(axis=1)]
print("\n=== Rows with Missing Values ===")
print(missing_rows)

print("\n=== Duplicate movieId Count ===")
print(df['movieId'].duplicated().sum())

print("\n=== Duplicate Rows ===")
print(df[df.duplicated()])

print("\n=== movieId Statistics ===")
print(df['movieId'].describe())

df['title_length'] = df['title'].astype(str).str.len()

print("\n=== Title Length Stats ===")
print(df['title_length'].describe())

title_outliers = df[(df['title_length'] > 50) | (df['title_length'] < 3)]
print("\n=== Title Length Outliers ===")
print(title_outliers[['movieId','title','title_length']])

df['genres'] = df['genres'].fillna("Unknown")

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("movies.csv")

df.columns = df.columns.str.strip()

print("=== First 5 Rows ===")
print(df.head())

print("\n=== Data Info ===")
print(df.info())

print("\n=== Missing Values ===")
print(df.isnull().sum())

df['genres'] = df['genres'].fillna("Unknown")

genre_counts = df['genres'].value_counts().head(10)

plt.figure()
plt.pie(genre_counts, labels=genre_counts.index, autopct='%1.1f%%')
plt.title("Genre Distribution (Pie Chart)")
plt.show()

plt.figure()
genre_counts.plot(kind='bar')
plt.title("Genre Distribution (Bar Chart)")
plt.xlabel("Genres")
plt.ylabel("Count")
plt.show()

plt.figure()
plt.step(range(len(genre_counts)), genre_counts.values)
plt.title("Genre Distribution (Stair Chart)")
plt.xlabel("Genre Index")
plt.ylabel("Count")
plt.show()

df_cleaned = df.drop_duplicates()

df_cleaned['title'] = df_cleaned['title'].fillna("Unknown")
df_cleaned['genres'] = df_cleaned['genres'].fillna("Unknown")

df_cleaned.to_csv("movies_cleaned.csv", index=False)

print("\nCleaned dataset saved as 'movies_cleaned.csv'")

genre_distribution = df['genres'].value_counts().head(5)

plt.figure()
plt.pie(genre_distribution, labels=genre_distribution.index, autopct='%1.1f%%')
plt.title("Top Movie Genres Distribution")
plt.show()

print("\n=== DATA QUALITY SUMMARY ===")
print("Missing Values:\n", df.isnull().sum())
print("Duplicate movieId:", df['movieId'].duplicated().sum())
print("Total Rows:", len(df))
print("Unique Titles:", df['title'].nunique())
print("Unique Genres:", df['genres'].nunique())

df_cleaned = df.drop_duplicates()

df_cleaned['title'] = df_cleaned['title'].fillna("Unknown")
df_cleaned['genres'] = df_cleaned['genres'].fillna("Unknown")

df_cleaned.to_csv("movies_cleaned.csv", index=False)

print("\nCleaned dataset saved as 'movies_cleaned.csv'")