import pandas as pd
import joblib
model = joblib.load("xgb_disease_symptom_model.pkl")
label_encoder = joblib.load("label_encoder.pkl")
feature_columns = joblib.load("feature_columns.pkl")

symptoms_to_ask = [
    'anxiety and nervousness', 'depression', 'shortness of breath',
    'headache', 'fever', 'nausea', 'cough', 'fatigue', 'dizziness', 'chest pain'
]


new_data_dict = {feature: 0 for feature in feature_columns}

for symptom in symptoms_to_ask:
    while True:
        answer = input(f"Does the patient have '{symptom}'? (yes/no): ").strip().lower()
        if answer in ['yes', 'no']:
            new_data_dict[symptom] = 1 if answer == 'yes' else 0
            break
        else:
            print("Please answer 'yes' or 'no'.")


new_data = pd.DataFrame([new_data_dict], columns=feature_columns)


pred_encoded = model.predict(new_data)
predicted_disease = label_encoder.inverse_transform(pred_encoded)

print("\nPredicted disease:", predicted_disease[0])
