import streamlit as st

st.title("Calculator")

num1 = st.number_input("Enter first no. : ")
num2 = st.number_input("Enter second no. : ")
add = st.button("Add")
sub = st.button("Subtract")
mul = st.button("Multiply")
div = st.button("Divide")
pow = st.button("Power")
per = st.button("Percentage")

if add:
    result = (num1 + num2)
    st.markdown(f"""Answer = {result}""")

elif sub:
    result = (num1 - num2)
    st.markdown(f"""Answer = {result}""")
    
elif mul:
    result = (num1 * num2)
    st.markdown(f"""Answer = {result}""")

elif div:
    result = (num1 / num2)
    st.markdown(f"""Answer = {result}""")

elif pow:
    result = (num1 ** num2)
    st.markdown(f"""Answer = {result}""")

elif per:
    result = ((num1 / 100) * num2)
    st.markdown(f"""Answer = {result}""")
