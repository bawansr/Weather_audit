# Weather_audit
I built a data audit pipeline to verify weather app accuracy. It automatically collects OpenWeatherMap’s 24-hour forecasts and compares them with next-day actual temperatures. Using Pandas and a Streamlit dashboard, it analyzes errors over time and reveals the real gap between predictions and reality
# 🌦️ Automated Weather Accuracy Auditor

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](PASTE_YOUR_STREAMLIT_LINK_HERE)

> **"Is my weather app lying to me?"** > An automated data pipeline that tracks, logs, and visualizes the accuracy of weather forecasts in Colombo, Sri Lanka.

---

## 📌 Project Overview
Companies and individuals rely on external data providers (APIs) for critical decisions. But how reliable is that data? 

This project is an end-to-end **ETL (Extract, Transform, Load) Pipeline** that:
1.  **Extracts** real-time temperature and 24-hour forecasts daily via the OpenWeatherMap API.
2.  **Transforms** and normalizes the data using Pandas.
3.  **Loads** the historical log into a CSV database.
4.  **Visualizes** the "Reality Gap" (Forecast vs. Actual) on an interactive Streamlit dashboard.

## 📊 Live Dashboard
I have deployed the visualization to the cloud. You can interact with the latest data here:
**[👉 Click to View Live App](PASTE_YOUR_STREAMLIT_LINK_HERE)**

![Dashboard Screenshot](final_chart.png)

## 🛠️ Tech Stack
* **Language:** Python 3.10
* **Frontend:** Streamlit (for web deployment)
* **Data Manipulation:** Pandas
* **API Integration:** OpenWeatherMap & Open-Meteo
* **Automation:** Cron / Task Scheduler (for daily data ingestion)

## 📂 Repository Structure
```text
├── app.py               # The frontend Streamlit application
├── collect_data.py      # The backend script that fetches API data
├── weather_audit.csv    # The database (Time-series logs)
├── requirements.txt     # Dependencies for cloud deployment
└── final_chart.png      # Static export of the analysis
