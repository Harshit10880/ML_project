from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

reg_model = LinearRegression()
reg_model.fit(X_train_scaled, y_train)
y_pred_final = np.maximum(0, y_pred)

results = pd.DataFrame({
    'Actual_Spent': y_test.values,
    'AI_Prediction': y_pred
})

results['Error'] = results['Actual_Spent'] - results['AI_Prediction']
print(results.head(10).round(2))

error = mean_absolute_error(y_test, y_pred)
print(f"On average, our prediction is off by: ${error:.2f}")