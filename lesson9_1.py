#建立.py
#網頁要用瀏覽器看
# streamlit>Docs>API reference
import streamlit as st
st.write("""# Hello! """)

#streamlit網頁主要在顯示抓到的資料，非顯示網頁製作的東西
#支援 Markdown語法
st.write("> **Li Jhen** ")
st.divider()
"*Welcome wolrd*"
st.divider()
st.title("這是title")
st.header("Header")
st.subheader('subheader')
st.caption('說明 from streamlit 說明書 text elements')
st.code('a=123')
st.divider()
- 1
- 1.1
- 2
- 3