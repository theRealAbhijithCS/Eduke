import joblib
import numpy as np

# Load trained model and scaler
model = joblib.load('ml/final_model.pkl')
scaler = joblib.load('ml/scaler.pkl')

def predict_performance(attendance, internal_marks, class_participation, academic_activities, sleep_time, study_time):
    # Convert input to numpy array
    input_data = np.array([[attendance, internal_marks, class_participation, academic_activities, sleep_time, study_time]])

    # Scale input using saved scaler
    input_data_scaled = scaler.transform(input_data)

    # Make prediction
    predicted_marks = model.predict(input_data_scaled)[0]

    # Ensure prediction is within 0-100
    predicted_marks = max(0, min(100, predicted_marks))  

    return round(predicted_marks, 2)

# Example usage
if __name__ == "__main__":
    result = predict_performance(54, 20, 82, 50, 66.7, 50)
    print(f"Predicted Final Marks: {result}")
