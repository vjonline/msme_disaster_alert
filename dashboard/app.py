import streamlit as st
import pandas as pd
import os
import joblib
from datetime import datetime

# Load latest weather data
weather_path = "data/weather_data.csv"
if os.path.exists(weather_path):
    all_weather = pd.read_csv(weather_path)
else:
    all_weather = pd.DataFrame(columns=["datetime", "city", "sub_region", "rain_1h", "wind_speed", "pressure", "humidity"])

# Load trained Isolation Forest model
model_path = "model.pkl"
if os.path.exists(model_path):
    model = joblib.load(model_path)
else:
    model = None

# Load alert logs (with error handling for malformed CSV)
log_path = "logs/alerts_log.csv"
try:
    logs = pd.read_csv(log_path, on_bad_lines='skip')
except Exception:
    logs = pd.DataFrame(columns=["datetime", "city", "risk_level", "message"])

# Color helper for risk level
def color_risk_level(risk):
    color_map = {
        "Anomaly": "<span style='color:red'><b>🔴 Anomaly</b></span>",
        "Normal": "<span style='color:green'><b>🟢 Normal</b></span>"
    }
    return color_map.get(risk, risk)

# Page layout
st.set_page_config(page_title="MSME Risk Alert Dashboard", layout="centered")
st.title("MSME Disaster Risk Alert System for Coastal & Hilly Areas")
st.markdown("**AI-powered hyperlocal alerts to protect MSMEs from natural disasters.**")

# City and sub-region selection
st.sidebar.title("Select Location")
location = st.sidebar.selectbox("Choose a City/Region", ["Gangtok - Hilly", "Mumbai - Coastal", "Shillong - Hilly"])
sub_region = st.sidebar.selectbox("Select Area within Gangtok", ["Tadong", "MG Marg", "Ranka"]) if location == "Gangtok - Hilly" else "-"

city_map = {
    "Gangtok - Hilly": "Gangtok",
    "Mumbai - Coastal": "Mumbai",
    "Shillong - Hilly": "Shillong"
}
selected_city = city_map[location]

# Show weather and prediction only for Gangtok
if selected_city != "Gangtok":
    st.subheader(f"Current Weather in {location}")
    st.info("Weather data and AI-based alert demo is currently available only for Gangtok.")
else:
    # Filter relevant data
    filtered_df = all_weather[(all_weather["city"] == selected_city) & (all_weather["sub_region"] == sub_region)]

    st.subheader(f"Current Weather in {sub_region}, {location}")
    if not filtered_df.empty and model is not None:
        latest_row = filtered_df.tail(1).iloc[0]
        st.write(latest_row[["datetime", "rain_1h", "wind_speed", "pressure", "humidity"]])

        # Prepare features and predict with Isolation Forest
        features = pd.DataFrame([latest_row[["rain_1h", "wind_speed", "pressure", "humidity"]]])
        prediction = model.predict(features)[0]
        risk_level = "Anomaly" if prediction == -1 else "Normal"

        st.markdown(f"### 🛑 Risk Level: {color_risk_level(risk_level)}", unsafe_allow_html=True)

        if risk_level == "Anomaly":
            st.markdown("**⚠️ AI detected an unusual weather pattern.**")
        else:
            st.markdown("✅ Weather conditions appear normal.")

        # Simulated SMS alert message
        st.subheader("📲 Simulated SMS Alert")
        rain = latest_row["rain_1h"]
        wind = latest_row["wind_speed"]
        pressure = latest_row["pressure"]
        timestamp = latest_row["datetime"]

        alert_message = f"""⚠️ Alert for {sub_region}, {selected_city} at {timestamp}
Rain: {rain} mm | Wind: {wind} km/h | Pressure: {pressure} hPa

Secure goods, unplug equipment, cover inventory.
Move valuables to higher shelves. Stay safe."""
        st.code(alert_message, language='text')

        # AI logic explanation
        st.subheader("🧠 How the AI Works")
        st.markdown("""
        - Trained with Isolation Forest on weather features:
          **rainfall, wind speed, pressure, and humidity**
        - Detects unusual (outlier) patterns, not fixed thresholds.
        - Triggers alerts when new data is different from past trends.
        """)
    else:
        st.warning("No recent weather data available or model not loaded.")

# Logs - filtered and styled
st.subheader("📊 Recent Alerts Log")
filtered_logs = logs[logs["city"] == selected_city]
if not filtered_logs.empty:
    styled_logs = filtered_logs.copy()
    styled_logs["risk_level"] = styled_logs["risk_level"].apply(color_risk_level)
    st.write(styled_logs.to_html(escape=False, index=False), unsafe_allow_html=True)
    st.download_button("📥 Download Alert Log as CSV", data=filtered_logs.to_csv(index=False), file_name=f"{selected_city}_alerts_log.csv", mime="text/csv")
else:
    st.info("No alerts have been logged for this location.")

# About Section
st.sidebar.markdown("---")
st.sidebar.markdown("**👨‍💻 About the Project**")
st.sidebar.markdown("This solution was developed as an **individual project** for the MSME Idea Hackathon 5.0 by **Vinamra Jain**.\n\n**Focus:** AI-powered hyperlocal alerts for disaster preparedness in MSMEs located in vulnerable coastal and hilly regions.")
