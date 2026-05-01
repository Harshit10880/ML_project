import pandas as pd
import numpy as np

np.random.seed(42)

n_rows = 500
categories = ['Electronics', 'Clothing', 'Home', 'Grocery', 'Beauty']
pay_methods = ['Credit Card', 'Cash', 'E-wallet', 'Debit Card']

data = {
    'Transaction_ID': [f'T{2000 + i}' for i in range(n_rows)],
    'Date': pd.date_range(start='2026-01-01', periods=n_rows, freq='h').strftime('%Y-%m-%d'),
    'Customer_ID': [f'C{np.random.randint(1000, 9999)}' for _ in range(n_rows)],
    'Product_Category': [np.random.choice(categories) for _ in range(n_rows)],
    'Quantity': [np.random.randint(1, 10) for _ in range(n_rows)],
    'Unit_Price': np.round(np.random.uniform(10.0, 500.0, n_rows), 2),
    'Payment_Method': [np.random.choice(pay_methods) for _ in range(n_rows)],
    'Return_Status': [np.random.choice(['Yes', 'No']) for _ in range(n_rows)],
    'Customer_Age': [np.random.randint(18, 75) for _ in range(n_rows)]
}

df = pd.DataFrame(data)
df['Total_Spent'] = np.round(df['Quantity'] * df['Unit_Price'], 2)


df.loc[df.sample(25).index, 'Customer_Age'] = np.nan  
df.loc[df.sample(15).index, 'Payment_Method'] = np.nan
df.loc[50, 'Total_Spent'] = 99999.99                  
df.loc[100, 'Product_Category'] = 'electrnics'        
df = pd.concat([df, df.sample(10)], ignore_index=True)

df.to_csv('retail_practice_data.csv', index=False)
print("Success! 'retail_practice_data.csv' has been created with all rows.")