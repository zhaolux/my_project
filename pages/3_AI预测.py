import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import plotly.express as px
from db import get_conn

st.title("🤖 AI销量预测")

conn = get_conn()
username = st.session_state["user"]
df = pd.read_sql(f"SELECT * FROM sales_data WHERE username='{username}'", conn)

if not df.empty and "date" in df.columns and "quantity" in df.columns:
    df["date"] = pd.to_datetime(df["date"])
    trend = df.groupby("date")["quantity"].sum()

    X = np.arange(len(trend)).reshape(-1,1)
    y = trend.values
    model = LinearRegression()
    model.fit(X, y)

    future_days = st.slider("预测天数", 1, 30, 7)
    future_X = np.arange(len(trend)+future_days).reshape(-1,1)
    future_y = model.predict(future_X)

    fig = px.line(y=future_y, title="未来销量预测")
    st.plotly_chart(fig)
