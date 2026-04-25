import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\om\OneDrive\Desktop\UM Assignments\wine_quality_dataser\Wine Quality Dataset.csv")

#print(df.describe())
#print(df.head())
#print(df.isnull().sum())
#print(df.corr())

#plt.figure(figsize=(10,6))
#sns.heatmap(df.corr(), annot=True)
#plt.show()

#high_quality = df[df['quality'] >= 7]
#print(high_quality)

#print(df.shape)
#print(df.index)
#print(df.columns)
print(df.info)