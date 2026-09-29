import streamlit as st
from donor_db import DonorCreateRetrieveUpdateDelete

st.title("Add New Donor")

name = st.text_input("Enter Donor Name")

blood_group = st.selectbox(
    "Select Blood Group",
    ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
)

phone = st.text_input("Enter Phone Number")

city = st.text_input("Enter City")

last_donation = st.date_input("Last Donation Date")

btn = st.button("Add Donor")

if btn:

    b = DonorCreateRetrieveUpdateDelete()

    try:
        b.create(
            name,
            blood_group,
            phone,
            city,
            last_donation
        )

        st.success("Donor added successfully")

    except Exception as e:
        st.error(str(e))