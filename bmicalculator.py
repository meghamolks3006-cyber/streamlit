import streamlit as st

st.title(" BMI Calculator")

weight=st.number_input("Weight (kg)",min_value=0)
height=st.number_input("Height (cm)",min_value=0)

if st.button("Calculate BMI"):
    height=height/100
    bmi=weight/(height**2)

    st.write("BMI is",bmi)

    if bmi<18.5:
        st.write("underweight")
    elif 18.5<=bmi<25:
        st.write("normal")
    elif 25<=bmi<30:
        st.write("overweight")
    else:
        st.write("obesity")