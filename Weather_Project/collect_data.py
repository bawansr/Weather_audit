import requests
import pandas as pd
from datetime import datetime
import os

# --- CONFIGURATION ---
API_KEY = "21e55fef9387992e4f3c3aaa7b3b7428"
CITY = "Colombo"
# Endpoint 1: Current Weather
CURRENT_URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
# Endpoint 2: Forecast
FORECAST_URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

CSV_FILE = "weather_audit.csv"

def get_data():
    # 1. Get Current Weather and Forecast
    resp_current = requests.get(CURRENT_URL)
    resp_forecast = requests.get(FORECAST_URL)
    
    if resp_current.status_code == 200 and resp_forecast.status_code == 200:
        curr_data = resp_current.json()
        fore_data = resp_forecast.json()
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # EXTRACT: Current Temp
        actual_temp = curr_data['main']['temp']
        
        # EXTRACT: Forecast (Approx 24 hours from now)
        # We grab the 8th item in the list (3 hours * 8 = 24 hours)
        forecast_24h = fore_data['list'][8]['main']['temp']
        forecast_time = fore_data['list'][8]['dt_txt']
        
        # 3. Organize
        record = {
            "timestamp_now": timestamp,
            "actual_temp_now": actual_temp,
            "forecast_for_tomorrow": forecast_24h,
            "forecast_target_time": forecast_time
        }
        return record
    else:
        print("Error fetching data!")
        return None

def save_to_csv(record):
    df = pd.DataFrame([record])
    
    # If file doesn't exist, create it with headers
    if not os.path.isfile(CSV_FILE):
        df.to_csv(CSV_FILE, index=False, header=True)
    # If file exists, append without headers
    else:
        df.to_csv(CSV_FILE, mode='a', index=False, header=False)
    
    # Success message
    print(f"--- SUCCESS ---")
    print(f"Right now in {CITY}: {record['actual_temp_now']} C")
    print(f"Forecast for tomorrow: {record['forecast_for_tomorrow']} C")
    print("Data saved to weather_audit.csv")

if __name__ == "__main__":
    data = get_data()
    if data:
        save_to_csv(data)