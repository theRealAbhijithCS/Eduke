import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load dataset
df = pd.read_csv('ml/Eduke_FInal_training_Data.csv')

# Separate features and target variable
X = df.drop(columns=['Final Marks'])  
y = df['Final Marks']

# Apply Min-Max Scaling (Normalize features between 0 and 1)
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Save trained model and scaler
joblib.dump(model, 'ml/final_model.pkl')
joblib.dump(scaler, 'ml/scaler.pkl')

# Evaluate model
y_pred = model.predict(X_test)

print("Model Performance:")
print("Mean Absolute Error (MAE):", round(mean_absolute_error(y_test, y_pred), 2))
print("Mean Squared Error (MSE):", round(mean_squared_error(y_test, y_pred), 2))
print("R² Score:", round(r2_score(y_test, y_pred), 2))
print("✅ Model training complete and saved as 'ml/final_model.pkl'.")
