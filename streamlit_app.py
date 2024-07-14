import streamlit as st
from datetime import timedelta, datetime

st.set_page_config(
    page_title="Date Differ",
    page_icon="📅",
)

st.title("📅 Date Differ")
st.caption("Calculate the difference in years + days between two dates")

col1, col2 = st.columns(2)

with col1:
    start_date = st.date_input(
        'Start Date', 
        datetime.today().date() - timedelta(days=10125),
    )

with col2:
    end_date = st.date_input(
        'End Date', 
        datetime.today().date(),
    )

date_diff = end_date - start_date
days_diff = date_diff.days

if days_diff > 365:
    years = days_diff // 365
    days = days_diff % 365
    st.write(f"**Date Difference**: `{years}` years, `{days}` days")
else:
    st.write(f"**Date Difference**: `{days_diff}` days")