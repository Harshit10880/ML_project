import numpy as np
import pandas as pd 

df = pd.read_csv('retail_practice_data.csv')
print(df.head())
print(df.isnull().sum())
print(df.describe())
print(df.shape)
print(df['Quantity'].value_counts())
print(df['Product_Category'].value_counts())

print(df["Customer_Age"].head())

ave = df['Customer_Age'].mean()

df['Customer_Age'] = df['Customer_Age'].fillna(ave)
print(df['Customer_Age'].head())
print(df['Customer_Age'].isnull().sum())
# print(df.info())
print(df.isnull().sum())


# payment method
print(df['Payment_Method'].value_counts())
# fill missing values with mode 
mode_payment = df['Payment_Method'].mode()[0]
df['Payment_Method'] = df['Payment_Method'].fillna(mode_payment)    

print(df['Payment_Method'].isnull().sum())
print(df['Payment_Method'].value_counts())


print(df['Return_Status'].value_counts())
# df.to_csv('retail_practice_data_cleaned.csv', index=False)