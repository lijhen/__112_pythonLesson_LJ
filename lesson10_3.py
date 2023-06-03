import streamlit as st
genre = st.radio('選擇你喜愛的類型',
         ('Cartoon','Drama','Movie','MV'),)
if genre == 'Cartoon':
    st.write('您選擇的是：" Cartoon "')
elif genre == 'Drama':
    st.write('您選擇的是：" Drama "')
elif genre == 'Movie':
    st.write('您選擇的是：" Movie "')
elif genre == 'MV':
    st.write('您選擇的是：" MV "')