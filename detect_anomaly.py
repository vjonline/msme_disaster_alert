import pandas as pd
import joblib
from utils.sms_sender import send_sms, load_recipients

# Load trained model
model = joblib.load("model.pkl")

# Load the latest weather data
df = pd.read_csv("data/weather_data.csv", header=0)

# Make sure the relevant columns are numeric
df[["rain_1h", "wind_speed", "pressure", "humidity"]] = df[["rain_1h", "wind_speed", "pressure", "humidity"]].apply(pd.to_numeric, errors="coerce")

# Drop rows with NaN (if any)
df.dropna(subset=["rain_1h", "wind_speed", "pressure", "humidity"], inplace=True)

# Get the last row
latest_full_row = df.iloc[-1]
latest_features = latest_full_row[["rain_1h", "wind_speed", "pressure", "humidity"]].values.reshape(1, -1)

# Predict using the model
prediction = model.predict(latest_features)  # -1 = anomaly

# Load recipients
recipients = load_recipients("data/recipients.txt")

# Extract dynamic values from latest row
sub_region = latest_full_row.get("sub_region", "your area")
city = latest_full_row.get("city", "Unknown")
timestamp = latest_full_row.get("datetime", "Unknown time")
rain = latest_full_row["rain_1h"]
wind = latest_full_row["wind_speed"]
pressure = latest_full_row["pressure"]

# Send SMS if anomaly detected
if prediction[0] == -1:
    print("🚨 Anomaly Detected - Alert Triggered!")
    
    alert_message = (
    f"⚠️ Risk alert for {sub_region}, {city} at {timestamp}. "
    "Heavy rain or wind expected. "
    "Secure goods, unplug electronics, and move items to higher shelves."
)


    
    print("Sending to:", recipients)
    #print("Message:\n", alert_message)
    
    send_sms(alert_message, recipients)

else:
    print("✅ Weather conditions normal.")
