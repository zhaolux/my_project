import streamlit as st
from db import create_tables
from auth import login, register

st.set_page_config(page_title="企业级数据分析平台", layout="wide")
create_tables()

menu = st.sidebar.selectbox("菜单", ["登录", "注册"])

if menu == "登录":
    login()
elif menu == "注册":
    register()

if "user" in st.session_state:
    st.title(f"欢迎 {st.session_state['user']} 🎉")
    st.write("左侧选择页面进入数据分析 / 可视化 / AI预测")
