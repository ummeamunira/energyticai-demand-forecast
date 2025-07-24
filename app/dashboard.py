import streamlit as st
import pandas as pd
import plotly.express as px

# Load forecast
forecast_df = pd.read_csv('outputs/forecast.csv', parse_dates=['timestamp'])
forecast_df.set_index('timestamp', inplace=True)

st.set_page_config(page_title="Alberta Energy Demand", layout="wide")

st.title("🔋 Alberta Hourly Electricity Demand Forecast")

st.markdown("""
This dashboard shows forecasted electricity demand using historical trends and machine learning.
""")

# Plot forecast
fig = px.line(forecast_df, y='Forecasted Power Demand', title='Forecasted Demand (MW)')
st.plotly_chart(fig, use_container_width=True)

# Display data
st.dataframe(forecast_df.tail(48))
