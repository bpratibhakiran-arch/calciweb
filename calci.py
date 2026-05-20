import streamlit as st

st.title("Hello")

data1 = st.text_input("Enter your name : ")
classdata = st.selectbox("Enter your class :",(1,2,3,4,5,6,7,8,9,10,11,12))
button = st.button("Done")

if button:
    st.markdown("Your name is",data1)
    st.markdown("You study in class",classdata)