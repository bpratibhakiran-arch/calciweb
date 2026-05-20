import streamlit as st

st.title("Hello")

num1 = st.number_input("Enter first no. : ")
num2 = st.number_input("Enter second no. : ")
add = st.button("Add")
sub = st.button("Subtract")

if add:
    st.markdown("Answer =",(num1 + num2))