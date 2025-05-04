import streamlit as st
import pandas as pd
from optimizer import load_bookings, load_requests, suggest_slots

st.set_page_config(page_title="AI Booking Optimizer", layout="wide")

st.title("🏟️ Sports Complex – AI Booking Optimizer")
st.markdown("Upload your **historical bookings** and **new booking requests**, then let the system suggest best-fit slots to avoid conflicts.")

# Upload files
hist_file = st.file_uploader("📁 Upload Historical Bookings CSV", type="csv", key="hist")
req_file = st.file_uploader("📁 Upload New Booking Requests CSV", type="csv", key="req")

if hist_file and req_file:
    hist_df = pd.read_csv(hist_file)
    req_df = pd.read_csv(req_file)

    st.subheader("📊 Uploaded Historical Bookings")
    st.dataframe(hist_df)

    st.subheader("📋 New Booking Requests")
    st.dataframe(req_df)

    st.subheader("⚙️ Optimization Suggestions")
    suggestions = suggest_slots(hist_df, req_df)
    st.dataframe(suggestions)

    csv = suggestions.to_csv(index=False).encode("utf-8")
    st.download_button("📥 Download Suggested Schedule", data=csv, file_name="optimized_schedule.csv", mime="text/csv")

else:
    st.info("Upload both CSV files to begin.")
