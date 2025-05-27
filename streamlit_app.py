
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
    st.markdown("Welcome to your crypto trading command center.")

    st.subheader("📈 Latest Simulated Trade")
    df = pd.DataFrame({
        "Time": [dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
        "Symbol": ["BTC/USD"],
        "Action": ["BUY"],
        "Confidence": ["87%"],
        "Simulated PnL ($)": ["+$122.45"]
    })
    st.table(df)

    st.success("Simulated trade alert sent. Daily performance tracking active.")
