import streamlit as st
import pandas as pd
import yfinance as yf
codeFrame = pd.read_csv('codeSearch.csv',usecols=['code','name'])
codeSeries = codeFrame['code'].astype(str)+ codeFrame['name']
with st.sidebar:
        selected_codes = st.multiselect("請選擇您要查詢的股票號碼：",
                                        options=codeSeries,
                                        max_selections=4)


@st.cache_data
def fetch_stock_dataFrame(id):
        stock_dataFrame = yf.download(id,start='2021-1-1')
        return stock_dataFrame

for code in selected_codes:
        code1 = code[:4]+'.TW'
        code_stock_dataFrame = fetch_stock_dataFrame(code1)
        code_stock_dataFrame_sorted = code_stock_dataFrame.sort_index(ascending=False)
        
        st.subheader(code)
        st.dataframe(code_stock_dataFrame_sorted,width=2048)
        st.line_chart(code_stock_dataFrame,y='Adj Close')
        st.divider()
#pip install yfinance
