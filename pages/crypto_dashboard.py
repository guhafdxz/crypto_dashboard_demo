#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 22:42:41 2023
@author: crypto_2024
"""
import streamlit as st
import pandas as pd



upcoming_projects_df = pd.read_excel('./pages/Upcoming_ICO.xlsx')
upcoming_projects_df['project_type']=upcoming_projects_df['project_type'].apply(lambda x:x[x.index('(')+1:x.index(')')]) 
fundraising_projects_df=pd.read_excel('./pages/fundraising_project_detail.xlsx')
latest_event_df =pd.read_excel('./pages/crypto_event_outline1686847458.xlsx')
latest_event_df=latest_event_df.iloc[:,1:]
st.title('This is a  :blue[crypto_dashboard] app demo :sunglasses:')
tab1, tab2,tab3 = st.tabs(["upcoming_ico", "latest_coin_event",'Fundrasing_projects'])

with tab1:   
    st.header(':green[upcoming_ico] projects and details')
    st.dataframe(upcoming_projects_df)
with tab2:   
    st.header(':green[latest] coin event]')
    st.dataframe(latest_event_df)

with tab3:   
    st.header(':green[latest] fundraising projects and details')
    st.dataframe(fundraising_projects_df)

    
    
