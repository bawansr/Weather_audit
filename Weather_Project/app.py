import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 1. Set up the Page
st.set_page_config(page_title="Weather Auditor", page_icon="🌦️")

st.title("🌦️ Colombo Weather Auditor")
st.write("""
This dashboard compares the **OpenWeatherMap Forecast** against the **Actual Temperature** measured in Colombo.
It proves whether the weather app is accurate or "lying."
""")

# 2. Load Data
# We use @st.cache_data so it loads fast and doesn't reload every time you click
@st.cache_data
def load_data():
    df = pd.read_csv("weather_audit.csv")
    df['timestamp_now'] = pd.to_datetime(df['timestamp_now'])
    return df

try:
    df = load_data()

    # 3. Metrics (The "Big Numbers" at the top)
    latest_actual = df['actual_temp_now'].iloc[-1]
    latest_forecast = df['forecast_for_tomorrow'].iloc[-1]
    
    col1, col2 = st.columns(2)
    col1.metric("Latest Actual Temp", f"{latest_actual} °C")
    col2.metric("Latest Forecast", f"{latest_forecast} °C")

    # 4. The Chart
    st.subheader("Accuracy Over Time")
    
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df['timestamp_now'], df['actual_temp_now'], label='Actual', marker='o', color='blue')
    ax.plot(df['timestamp_now'], df['forecast_for_tomorrow'], label='Forecast', linestyle='--', color='red')
    
    ax.set_ylabel("Temperature (°C)")
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    # Instead of plt.show(), we use st.pyplot(fig)
    st.pyplot(fig)

    # 5. Show the raw data (Optional)
    with st.expander("See Raw Data"):
        st.dataframe(df)

except FileNotFoundError:
    st.error("Data file not found. Please ensure weather_audit.csv is in the repository.")