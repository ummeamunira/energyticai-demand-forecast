import streamlit as st

st.set_page_config(page_title="EnergyticAI", layout="wide")

st.title("⚡ EnergyticAI: Alberta Electricity Demand Dashboard")
st.markdown("""
Welcome! This dashboard showcases **hourly electricity demand forecasts** for Alberta, 
alongside weather, generation, and price dynamics.
""")
import pandas as pd
import plotly.express as px

# Example placeholder data (replace with real forecast later)
df = pd.DataFrame({
    'timestamp': pd.date_range('2025-01-01', periods=48, freq='h'),
    'demand_forecast': [8000 + i*10 + (i%24)*50 for i in range(48)]
})

fig = px.line(df, x='timestamp', y='demand_forecast', title='48-Hour Demand Forecast')
st.plotly_chart(fig, use_container_width=True)
st.sidebar.title("Navigation")
page = st.sidebar.radio("Select a section:", ["Overview", "Demand Forecast", "Price Trends"])
