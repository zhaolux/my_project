import streamlit as st
import pandas as pd
from db import get_conn

st.title("📊 数据分析")

file = st.file_uploader("上传 CSV", type=["csv"])

if file:
    df = pd.read_csv(file)
    st.dataframe(df)

    st.subheader("基本统计")
    st.write(df.describe())

    # 上传数据保存到数据库
    username = st.session_state["user"]
    conn = get_conn()
    df["username"] = username
    df.to_sql("sales_data", conn, if_exists="append", index=False)
    st.success("数据已保存")
