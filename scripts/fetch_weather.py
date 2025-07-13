import os
import requests #used to send request to api to get resoponses
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
API_KEY=os.getenv("WEATHER_API_KEY")
CITY = "Gangtok"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL).json()
data = {
    "datetime": datetime.now(),
    "rain_1h": response.get("rain", {}).get("1h", 0),
    "wind_speed": response.get("wind", {}).get("speed", 0),
    "pressure": response.get("main", {}).get("pressure", 0),
    "humidity": response.get("main", {}).get("humidity", 0)
}

df = pd.DataFrame([data])#creates a new pandas DataFrame from 'data' dict. this dict is wrapped in a list to make it single-row DataFrame
df.to_csv("data/weather_data.csv", mode='a', header=False, index=False)
#mode='a' - appends dataframe as new row to csv file
#header=false - column names are not written 