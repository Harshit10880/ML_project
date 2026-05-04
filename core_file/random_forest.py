from sklearn.ensemble import RandomForestClassifier

rf_model = RandomForestClassifier(n_estimators=100, random_state=42)

rf_model.fit(X_train, y_train)


# rf_pred = rf_model.predict(X_test)
# print(f"Random Forest Accuracy: {accuracy_score(y_test, rf_pred) * 100:.2f}%")

# pending more implementation of random forest regression for the second problem, but here is the basic setup for classification.