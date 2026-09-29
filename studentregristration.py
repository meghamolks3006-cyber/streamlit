import streamlit as st
from datetime import date

st.title("Student Registration")

name = st.text_input("Enter your name")
st.write(name)

age = st.number_input("Enter your age")
st.write(age)

dob = st.date_input(
    "Enter your date",
    min_value=date(1990, 2, 2),
    max_value=date.today(),
    value=date(2026, 1, 2)
)

email = st.text_input("Enter your email")
st.write(email)

gender = st.radio("Gender", ("Male", "Female"))
st.write(gender)

course = st.selectbox("Courses", ("Python", "Dotnet", "Testing"))
st.write(course)

btn = st.button("Submit")
print(btn)

if btn:
    st.write(name)
    st.write(age)
    st.write(dob)
    st.write(email)
    st.write(gender)
    st.write(course)