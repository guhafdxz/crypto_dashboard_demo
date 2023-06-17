#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 22:42:41 2023
@author: crypto_2024
"""

import streamlit as st
import pandas as pd



st.set_page_config(
    page_title='Event demo',
    page_icon="",
)

upcoming_projects_df = pd.read_excel('./pages/Upcoming_ICO.xlsx')
active_projects_df =  pd.read_excel('./pages/Active_ICO.xlsx')
coin_event_df =pd.read_excel('./pages/coin_event_detail.xlsx')

fundraising_projects_df=pd.read_excel('./pages/fundraising_information.xlsx')
st.title('This is a  :blue[crypto_dashboard] app demo :sunglasses:')
tab1, tab2,tab3 = st.tabs(["upcoming_ico", "latest_coin_event",'Fundrasing_projects'])

with tab1:   
    st.header(':green[upcoming_ico] projects and details')
    st.dataframe(upcoming_projects_df)
with tab2:   
    st.header(':green[latest] coin event')
    st.dataframe(coin_event_df)
with tab3:   
    st.header(':green[latest] fundraising projects and details')
    st.dataframe(fundraising_projects_df)

    
    
