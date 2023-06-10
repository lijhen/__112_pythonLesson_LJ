import streamlit as st
import pandas as pd
codeFrame = pd.read_csv('codeSearch.csv',usecols=['code','name'])
codeSeries = codeFrame['code'].astype(str)+ codeFrame['name']
with st.sidebar:
        selected_codes = st.multiselect("請選擇您要查詢的股票號碼：",
                                        options=codeSeries,
                                        max_selections=4)
for code in selected_codes:
        code = code[:4]+'.TW'
        st.write(code)
#pip install yfinance
