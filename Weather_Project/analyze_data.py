import pandas as pd
import matplotlib.pyplot as plt

# Load Data
df = pd.read_csv("weather_audit.csv")
df['timestamp_now'] = pd.to_datetime(df['timestamp_now'])

# Plot
plt.figure(figsize=(10, 5))
plt.plot(df['timestamp_now'], df['actual_temp_now'], label='Actual', marker='o')
plt.plot(df['timestamp_now'], df['forecast_for_tomorrow'], label='Forecast', linestyle='--')

plt.title("Weather Forecast Accuracy Audit")
plt.xlabel("Date")
plt.ylabel("Temperature (C)")
plt.legend()
plt.grid(True)

# Save it
plt.savefig("final_chart.png")
plt.show()