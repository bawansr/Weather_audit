import requests
import pandas as pd 
from datetime import datetime, timedelta

##Colombo coordinates bcz to get the history we are using OPen_Meteo they ask coordinates not the names
LAT = 6.9271 ## Latitude (LAT) → how far north/south you are
LON = 79.8612 ## Longitude (LON) → how far east/west you are

print("Fetching historical data from Open-Meteo")

##Calculate the dates (Last 14 days)
end_date = datetime.now().strftime("%Y-%m-%d")
start_date = (datetime.now() - timedelta(days=14)).strftime("%Y-%m-%d")

##THe url no api needed 
url = f"https://archive-api.open-meteo.com/v1/archive?latitude={LAT}&longitude={LON}&start_date={start_date}&end_date={end_date}&daily=temperature_2m_mean&timezone=auto"

response = requests.get(url)
data = response.json()

# 3. Process the data
history_list = []

if "daily" in data:
    dates = data['daily']['time']
    temps = data['daily']['temperature_2m_mean']
    
    for i in range(len(dates)):
        # We are rebuilding the structure to match your specific CSV format
        # Note: We can't get the "Forecast" from the past (that data is lost in time)
        # So we simulate a small variance to keep the code working, or just leave it blank.
        # For this exercise, we will assume the forecast was slightly off.
        
        actual = temps[i]
        
        record = {
            "timestamp_now": dates[i] + " 12:00:00", # Approx noon
            "actual_temp_now": actual,
            "forecast_for_tomorrow": actual, # Placeholder (we don't have past forecasts)
            "forecast_target_time": "N/A"
        }
        history_list.append(record)
##Save to CSv 
df = pd.DataFrame(history_list)
df.to_csv("weather_audit.csv", index=False)

print("--- SUCCESS ---")
print(f"Downloaded {len(history_list)} days of REAL history for Colombo.")