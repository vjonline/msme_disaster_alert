import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

# Load dataset
df = pd.read_csv("data/weather_data.csv")

# Optional: Print first rows to debug
print(df.head())

# Select only numeric feature columns
features = df[["rain_1h", "wind_speed", "pressure", "humidity"]]

# Ensure all values are numeric
features = features.apply(pd.to_numeric, errors='coerce')

# Drop any rows with missing/NaN values
features.dropna(inplace=True)

# Train Isolation Forest
model = IsolationForest(n_estimators=100, contamination=0.1, random_state=42)
model.fit(features)

# Save model
joblib.dump(model, "model.pkl")
print("✅ Model trained and saved as model.pkl")
