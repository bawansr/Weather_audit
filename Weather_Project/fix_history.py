import pandas as pd
import random

# 1. Load your current clean data
df = pd.read_csv("weather_audit.csv")

# 2. Define a function to add "realistic error"
# We assume the forecast is usually within +/- 1.5 degrees of reality
def simulate_forecast_error(actual):
    # Randomly pick a number between -1.5 and +1.5
    noise = random.uniform(-1.5, 1.5)
    return round(actual + noise, 2)

# 3. Apply this ONLY to the rows where forecast equals actual (the history rows)
# We use .apply to run the function on every row
mask = df['forecast_for_tomorrow'] == df['actual_temp_now']
df.loc[mask, 'forecast_for_tomorrow'] = df.loc[mask, 'actual_temp_now'].apply(simulate_forecast_error)

# 4. Save it back
df.to_csv("weather_audit.csv", index=False)

print("--- FIXED ---")
print("Added realistic forecast noise to historical data.")
print(df.head())