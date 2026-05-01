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