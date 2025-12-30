# Regional Sales Predictor

## Overview
This project provides a predictive BI solution to analyze regional sales performance and forecast future trends. By combining historical sales data with external market signals (holidays, promotions, economic conditions), the model provides actionable insights to optimize inventory and marketing strategies.

---

## Features
- Visualize historical sales data per region and product.
- Forecast future sales using time series models (Prophet, LSTM).
- Compare regional performance and identify underperforming areas.
- Explore prescriptive insights, e.g., stock recommendations before peak seasons.
- Interactive dashboard built with Streamlit.

---

## Dataset
The dataset contains sample sales records with the following columns:
- `date`: Sale date
- `region`: Region where the product was sold (East, West, North, South)
- `product`: Product name
- `sales_amount`: Revenue generated
- `units_sold`: Number of units sold
- `promo_active`: Whether a promotion was active (0 = No, 1 = Yes)
- `holiday`: Whether the date was a holiday (0 = No, 1 = Yes)

> For demonstration purposes, this repo contains a sample dataset with 50 records. You can replace it with your complete dataset.

---

## Installation
1. Clone the repository:
```bash
git clone https://github.com/<your-username>/regional-sales-forecasting.git
```
cd regional-sales-forecasting
Install dependencies:

```bash
Copy code
pip install -r requirements.txt
```
Run the Streamlit app:

```bash
Copy code
streamlit run App.py
```
Usage
Use the sidebar to select regions and products.

View historical sales and forecasts in interactive charts.

Download predictions for further analysis.

Technologies
Python

Pandas & NumPy

Prophet & LSTM (for time series forecasting)

Streamlit (for dashboard)

Matplotlib & Plotly (for interactive charts)

Future Enhancements
Add real-time sales data integration.

Incorporate external signals like competitor pricing.

Enable scenario analysis for multiple forecasting strategies.

Author
Aayush Kumbharkar
LinkedIn
