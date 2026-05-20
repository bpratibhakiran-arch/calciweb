import streamlit as st

st.title("Calculator")

num1 = st.number_input("Enter first no. : ")
num2 = st.number_input("Enter second no. : ")
add = st.button("Add")
sub = st.button("Subtract")

if add:
    result = (num1 + num2)
    st.markdown(f"""Answer = {result}""")

elif sub:
    result = (num1 - num2)
    st.markdown(f"""Answer = {result}""")