import streamlit as st
import pandas as pd
import plotly.express as px
from db import get_conn

st.title("📈 可视化分析")

conn = get_conn()
username = st.session_state["user"]
df = pd.read_sql(f"SELECT * FROM sales_data WHERE username='{username}'", conn)

if not df.empty:
    col = st.selectbox("选择字段绘制柱状图", df.columns)
    fig = px.histogram(df, x=col)
    st.plotly_chart(fig)

    if "product" in df.columns:
        pie = px.pie(df, names="product")
        st.plotly_chart(pie)
