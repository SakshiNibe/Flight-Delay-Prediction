import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load dataset
data = pd.read_csv("dataset/flights.csv")

print("Dataset Loaded Successfully!")
print(data)

# Input features
X = data[
    [
        "Airline",
        "Source",
        "Destination",
        "Day",
        "Month",
        "Departure_Time"
    ]
]

# Target
# 0 = On Time
# 1 = Delayed
y = data["Delay"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create Random Forest model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# Train model
model.fit(X_train, y_train)

# Test model
prediction = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, prediction)

print("Model Accuracy:", accuracy)

# Save model
joblib.dump(model, "model.pkl")

print("Model Saved Successfully!")