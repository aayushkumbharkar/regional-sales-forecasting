# app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet

# Page config
st.set_page_config(page_title="Regional Sales Forecast Dashboard", layout="wide")
st.title("📊 Regional Sales Forecast & Insights")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("sales_data.csv")
    df['date'] = pd.to_datetime(df['date'])
    return df

df = load_data()

# Sidebar selection
regions = df['region'].unique()
selected_region = st.sidebar.selectbox("Select Region", regions)

products = df['product'].unique()
selected_product = st.sidebar.selectbox("Select Product", products)

# Filtered data
region_product_data = df[(df['region'] == selected_region) & (df['product'] == selected_product)]
region_product_data = region_product_data.sort_values('date')

# Historical sales plot
st.subheader(f"Historical Sales – {selected_region} | {selected_product}")
fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(region_product_data['date'], region_product_data['sales_amount'], marker='o', linestyle='-')
ax.set_xlabel("Date")
ax.set_ylabel("Sales Amount")
ax.set_title("Historical Sales Trend")
plt.xticks(rotation=45)
st.pyplot(fig)

# Prophet forecast
st.subheader("30-Day Forecast")

prophet_df = region_product_data[['date', 'sales_amount']].rename(columns={'date':'ds', 'sales_amount':'y'})

model = Prophet()
model.fit(prophet_df)

future = model.make_future_dataframe(periods=30)
forecast = model.predict(future)

fig2 = model.plot(forecast)
st.pyplot(fig2)

# Forecast table
st.subheader("Forecasted Sales Data")
st.dataframe(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(30).reset_index(drop=True))

# Business insights
past_avg = region_product_data['sales_amount'].mean()
future_avg = forecast.tail(30)['yhat'].mean()
growth = ((future_avg - past_avg) / past_avg) * 100

st.subheader("Business Recommendation")
if growth > 10:
    st.success("📈 Expected growth is high – Increase inventory and push marketing")
elif growth < -5:
    st.error("📉 Expected decline – Run promotions or reduce stock")
else:
    st.info("➡️ Stable sales – Maintain current strategy")

st.metric("Expected Growth (%)", f"{growth:.2f}")

# Footer
st.caption("Model: Facebook Prophet | Forecast Horizon: 30 Days")
