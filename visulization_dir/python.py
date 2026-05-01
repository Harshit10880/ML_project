import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# visulization charts
# 1. Boxplot for Total_Spent to identify outliers

sns.set_theme(style="whitegrid")
plt.figure(figsize=(15, 10))

plt.subplot(2, 2, 1)
sns.boxplot(x=df['Total_Spent'])
plt.title('Identifying Price Outliers')


# 2 . Histogram for Customer_Age to see distribution and missing values

plt.subplot(2, 2, 2)
sns.histplot(df['Customer_Age'].dropna(), bins=20, kde=True, color='skyblue')
plt.title('Customer Age Distribution')


# 3 . Countplot for Product_Category to see sales distribution across categories

plt.subplot(2, 2, 3)
sns.countplot(y=df['Product_Category'], order=df['Product_Category'].value_counts().index)
plt.title('Sales by Product Category')


# 4 . Heatmap for correlation between numeric features

plt.subplot(2, 2, 4)
# use numeric columns for correlation
numeric_df = df.select_dtypes(include=['float64', 'int64'])
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation between Numeric Features')