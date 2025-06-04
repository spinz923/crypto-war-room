
import streamlit as st
import pandas as pd
import datetime as dt

# Password protection
def check_password():
    def password_entered():
        if st.session_state["password"] == "warroomaccess":
            st.session_state["password_correct"] = True
            del st.session_state["password"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        st.text_input("Enter password:", type="password", on_change=password_entered, key="password")
        return False
    elif not st.session_state["password_correct"]:
        st.text_input("Enter password:", type="password", on_change=password_entered, key="password")
        st.error("Password incorrect")
        return False
    else:
        return True

if check_password():
    st.title("🚀 Crypto War Room")
    st.markdown("Simulated trade generated below.")

    now = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    df = pd.DataFrame([{
        "Time": now,
        "Symbol": "BTC/USD",
        "Action": "BUY",
        "Confidence": "91.4%",
        "Simulated PnL": "+$128.67",
        "Strategy": "MACD"
    }])
    st.table(df)
