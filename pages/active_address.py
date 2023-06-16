import streamlit as st
import pandas as pd


st.set_page_config(
    page_title='Active address demo',
    page_icon="",
)

active_address=pd.read_excel('./chain_daily_active_address.xlsx')

st.line_chart(active_address)
