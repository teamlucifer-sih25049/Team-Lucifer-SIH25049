import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

df = pd.read_csv(r'C:\Users\msent\OneDrive\Desktop\SIH\dataset1.csv')
print("Data preview:")
print(df.head())
print("\nData info:")
print(df.info())
print("\nDisease label distribution before filtering:")
print(df['diseases'].value_counts())
disease_counts = df['diseases'].value_counts()
diseases_to_keep = disease_counts[disease_counts >= 2].index
df_filtered = df[df['diseases'].isin(diseases_to_keep)]
print("\nDisease label distribution after filtering:")
print(df_filtered['diseases'].value_counts())
X = df_filtered.drop('diseases', axis=1)
y = df_filtered['diseases']
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)
X_train, X_test, y_train, y_test = train_test_split(
    X, y_encoded, test_size=0.2, random_state=42, stratify=y_encoded
)
model = XGBClassifier(
    objective='multi:softprob',
    num_class=len(label_encoder.classes_),
    eval_metric='mlogloss',
    use_label_encoder=False,
    n_estimators=200,
    max_depth=6,
    learning_rate=0.1,
    random_state=42,
    n_jobs=-1
)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"\nModel Accuracy: {accuracy:.4f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=label_encoder.classes_))
import joblib
feature_columns = df_filtered.drop('diseases', axis=1).columns.tolist()
joblib.dump(feature_columns, 'feature_columns.pkl')
joblib.dump(model, "xgb_disease_symptom_model.pkl")
joblib.dump(label_encoder, "label_encoder.pkl")
print("\nModel saved as xgb_disease_symptom_model.pkl")

