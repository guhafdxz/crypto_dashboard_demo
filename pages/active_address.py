import streamlit as st
import pandas as pd


st.set_page_config(
    page_title='Active address demo',
    page_icon="",
)

active_address=pd.read_excel('./pages/chain_daily_active_address.xlsx')
active_address.index=active_address.iloc[:,0]
active_address=active_address.iloc[:,1:]
st.line_chart(active_address)
