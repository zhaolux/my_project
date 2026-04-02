import streamlit as st
from db import get_conn

def login():
    st.sidebar.subheader("🔐 登录")
    username = st.sidebar.text_input("用户名")
    password = st.sidebar.text_input("密码", type="password")

    if st.sidebar.button("登录"):
        conn = get_conn()
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = c.fetchone()
        if user:
            st.session_state["user"] = username
            st.success("登录成功")
        else:
            st.error("用户名或密码错误")

def register():
    st.sidebar.subheader("📝 注册")
    new_user = st.sidebar.text_input("新用户名")
    new_pass = st.sidebar.text_input("新密码", type="password")

    if st.sidebar.button("注册"):
        conn = get_conn()
        c = conn.cursor()
        c.execute("INSERT INTO users VALUES (?,?)", (new_user, new_pass))
        conn.commit()
        st.success("注册成功")
