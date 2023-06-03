import streamlit as st
def button_click():
    st.write(st.session_state)

if st.button("Say hello !",key ='myBotton',on_click=button_click):
    st.write("Hello there~")
#else:
#    st.write('Goodbye.')

st.divider()

agree = st.checkbox('I agree.')
if agree:
    st.write('Great!!')
