import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import joblib
import os

st.set_page_config(page_title="Stock Market Predictor", layout="wide")

st.title("📊 Stock Market Prediction App")

# Upload CSV File
uploaded_file = st.file_uploader("Upload Stock Market CSV", type=["csv"])

# Load data
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("✅ File uploaded successfully")
else:
    st.info("⬆ Upload a CSV file to begin")
    st.stop()

# Show data
st.subheader("🔍 Raw Data")
st.dataframe(df.head(20))

# Plot closing prices
if "Close" in df.columns:
    st.subheader("📉 Closing Price Trend")
    fig, ax = plt.subplots()
    ax.plot(df['Close'], label='Closing Price', color='orange')
    ax.set_title("Stock Closing Price Over Time")
    ax.set_xlabel("Time")
    ax.set_ylabel("Price")
    ax.legend()
    st.pyplot(fig)
else:
    st.warning("❗ 'Close' column not found in dataset.")

# Dummy prediction logic for example
st.subheader("📈 Predict Future Prices (Demo)")

future_days = st.slider("Select number of days to predict:", min_value=1, max_value=30, value=7)

if st.button("Run Prediction"):
    try:
        last_close = df['Close'].values[-1]
        predictions = [last_close + np.random.randn()*2 for _ in range(future_days)]
        st.success(f"Generated predictions for next {future_days} days.")

        pred_df = pd.DataFrame({
            "Day": list(range(1, future_days + 1)),
            "Predicted Price": predictions
        })

        st.line_chart(pred_df.set_index("Day"))
        st.dataframe(pred_df)

    except Exception as e:
        st.error(f"Prediction failed: {e}")
