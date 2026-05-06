import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import seaborn as sns
import matplotlib.pyplot as plt

# 1. READ THE CSV
df = pd.read_csv('retail_practice_data_cleaned.csv')


df['Product_Category'] = df['Product_Category'].replace('electrnics', 'Electronics')
df['Customer_Age'] = df['Customer_Age'].fillna(df['Customer_Age'].median())
df_clean = df[df['Total_Spent'] < 50000].copy() # Removing the 99k outlier

X = df_clean[['Customer_Age', 'Total_Spent']]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

kmeans = KMeans(n_clusters=3, random_state=42)
df_clean['Segment'] = kmeans.fit_predict(X_scaled)

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df_clean, x='Customer_Age', y='Total_Spent', hue='Segment', palette='viridis')
plt.title('Customer Segments in Jamnagar Retail Store')
plt.show()

print(df_clean.groupby('Segment')[['Customer_Age', 'Total_Spent']].mean())