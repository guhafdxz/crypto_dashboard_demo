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
active_ico_projects_df =  pd.read_excel('./pages/Active_ICO.xlsx')
latest_coin_events_df =pd.read_excel('./pages/coin_event_detail.xlsx')
trending_coin_events_df=pd.read_excel('./pages/event_trending.xlsx')
fundraising_projects_df=pd.read_excel('./pages/fundraising_information.xlsx')
st.title('This is a  :blue[crypto_dashboard] app demo :sunglasses:')
tab1, tab2,tab3,tab4,tab5 = st.tabs(["Upcoming ICOs","Active ICOs", "Latest coin events","Trending coin events",'Fundrasing projects'])

with tab1:   
    st.header(':green[upcoming ico] projects and details')
    st.dataframe(upcoming_projects_df)
with tab2:   
    st.header(':red[active ico] projects and details')
    st.dataframe(active_ico_projects_df)

with tab3:   
    st.header(':green[latest] coin event')
    st.dataframe(latest_coin_events_df)

with tab4:   
    st.header(':red[trending] coin events')
    st.dataframe(trending_coin_events_df)

with tab5:   
    st.header(':green[latest] fundraising projects and details')
    st.dataframe(fundraising_projects_df)




    
    
