
import streamlit as st
import pandas as pd
import datetime as dt
import gspread
from oauth2client.service_account import ServiceAccountCredentials

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

def log_trade_to_sheet(trade):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_dict(st.secrets.to_dict(), scope)
    client = gspread.authorize(creds)
    sheet = client.open_by_key("15KZYl20YZ9zesfFUPyW0b4gUcoBqS_FVi4aT-9lii5A")
    worksheet = sheet.worksheet("TradeLog")
    worksheet.append_row(trade)

if check_password():
    st.title("🚀 Crypto War Room")
    st.markdown("Welcome to your live crypto trading dashboard.")

    now = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    symbol = "BTC/USD"
    action = "BUY"
    confidence = "91.4%"
    pnl = "+$128.67"
    strategy = "MACD"

    trade = [now, symbol, action, confidence, pnl, strategy]
    df = pd.DataFrame([trade], columns=["Time", "Symbol", "Action", "Confidence", "Simulated PnL", "Strategy"])
    st.table(df)

    try:
        log_trade_to_sheet(trade)
        st.success("✅ Trade logged to Google Sheet successfully.")
    except Exception as e:
        st.error(f"❌ Failed to log trade: {e}")
