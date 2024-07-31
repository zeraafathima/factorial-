import streamlit as st 
st.title('factorial application')
st.header("created by fathima")
x=st.number_input(label="enter a number",value=0)

clicked=st.button('submit')
if clicked:
    z=1
    for i in range (1,x+1):
        z=i*z

    st.subheader(z)