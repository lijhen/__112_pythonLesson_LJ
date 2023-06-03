import streamlit as st

title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)

number = st.number_input('Insert a number')
st.write('The current number is ', number)

import datetime
import streamlit as st

d = st.date_input(
    "When\'s your birthday",
    datetime.date(1990,1,1))
st.write('Your birthday is:', d)