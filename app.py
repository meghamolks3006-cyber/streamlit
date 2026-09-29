import streamlit as st

num1 = st.number_input("Enter number1", min_value=0)
num2 = st.number_input("Enter number2", min_value=0)

st.write(num1)
st.write(num2)

name = st.text_input("Enter your name")
st.write(name)

date = st.date_input("Enter your date")
st.write(date)


btn=st.button("Click ")
print(btn)


if btn:
    st