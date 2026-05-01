import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

df = pd.read_csv('retail_practice_data_cleaned.csv')



# Trying things out with the StandardScaler

scaler = StandardScaler()
# Formula applied: z = (x - mean) / std_dev
df['Age_Standardized'] = scaler.fit_transform(df[['Customer_Age']])

# Check the results
# print(df[['Customer_Age', 'Age_Standardized']].head())
pd.options.display.float_format = '{:.4f}'.format
print(df[['Customer_Age', 'Age_Standardized']].head())


# One-hot encoding for Payment_Method

df = pd.get_dummies(df, columns=['Payment_Method'], prefix='Pay', dtype=int)
print(df[['Pay_Cash', 'Pay_Credit Card', 'Pay_Debit Card', 'Pay_E-wallet']].head())

df['Product_Category'] = df['Product_Category'].replace('electrnics', 'Electronics')
df = pd.get_dummies(df, columns=['Product_Category'], prefix='Cat', dtype=int)

df['Return_Status'] = df['Return_Status'].map({'Yes': 1, 'No': 0})



# Visulization differences
feature_columns = ['Customer_Age', 'Quantity', 'Unit_Price',
                   'Pay_Cash', 'Pay_Credit Card', 'Pay_Debit Card', 'Pay_E-wallet',
                   'Cat_Beauty', 'Cat_Clothing', 'Cat_Electronics', 'Cat_Grocery', 'Cat_Home']
X = df[feature_columns]
y = df['Return_Status']

print("X head:")
display(X.head())
print("\ny head:")
display(y.head())