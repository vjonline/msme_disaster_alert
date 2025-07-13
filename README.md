# MSME Disaster Risk Alert System 🌩️📲

An AI-powered hyperlocal weather anomaly detection and SMS alert system built to protect MSMEs in hilly and coastal regions.

## 🚀 Features

- 📡 Real-time weather data from OpenWeatherMap
- 🧠 AI-based anomaly detection using Isolation Forest
- 🌐 Hyperlocal location support (e.g., Gangtok sub-regions)
- 📲 SMS alerts with Twilio (demo mode enabled for safety)
- 📊 Streamlit dashboard to visualize weather and risks
- 📝 Alert logging to CSV

## 📦 Tech Stack

- Python, Pandas, Scikit-Learn
- Streamlit
- Twilio API
- dotenv for env management

## 🛠️ How to Run Locally

1. Clone this repo:
   ```bash
   git clone https://github.com/vjonline/msme_disaster_alert.git
   cd msme-disaster-alert

2. Create a .env file in the root
    ```bash
    TWILIO_SID=your_twilio_sid
    TWILIO_AUTH_TOKEN=your_auth_token
    TWILIO_PHONE=+1YourTwilioTrialNumber
    TO_PHONE=+91YourPhoneNumber
    DEMO_MODE=True

3. Install required dependencies 
    ```bash
    pip install -r requirements.txt

4. Run the Streamlit dashboard
    ```bash
    streamlit run app.py

## 🖥️ Dashboard Highlights

- 📍 Sub-region selection (e.g., Tadong, MG Marg)
- 📊 Real-time weather info: rainfall, wind, pressure, humidity
- 🧠 AI Risk Level: “Anomaly” or “Normal” (via Isolation Forest)
- 📩 Simulated SMS alerts based on current risk
- 📈 View recent alerts with timestamps and messages

## ⚠️ Limitations & Future Scope

- 🔒 **Two-way SMS reply system was not implemented** due to regulatory restrictions such as DLT registration requirements in India and limitations of trial accounts on Twilio.
- 🌐 Weather data is currently available only for Gangtok (demo location); multi-city support can be added with more historical training data.
- 📶 Offline or low-connectivity fallback mechanisms (e.g., radio alerts or local caching) are not part of this MVP but are valuable next steps for rural MSMEs.

## 📄 License
This project is shared under the
Creative Commons BY-NC-ND 4.0 License.

You are free to view and evaluate the code. However, reuse, redistribution, or modification is not allowed without explicit permission from the author.

## 👨‍💻 Author
Vinamra Jain
Solo Developer | B.Tech CSE Student
Built for MSME Idea Hackathon 5.0