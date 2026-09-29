import streamlit as st

num1 = st.number_input("Enter number1", min_value=0)
num2 = st.number_input("Enter number2", min_value=0)

btn=st.button("add")

if btn:
    s=num1+num2


st.write("Sum =", s)