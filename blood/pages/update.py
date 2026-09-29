import streamlit as st
from donor_db import DonorCreateRetrieveUpdateDelete

st.title("Update Donor")

donor_id = st.number_input(
    "Enter Donor ID",
    min_value=1,
    step=1
)

name = st.text_input("Enter Donor Name")

blood_group = st.selectbox(
    "Select Blood Group",
    ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
)

phone = st.text_input("Enter Phone Number")

city = st.text_input("Enter City")

last_donation = st.date_input("Last Donation Date")

btn = st.button("Update")

if btn:

    b = DonorCreateRetrieveUpdateDelete()

    result = b.update(
        donor_id,
        name,
        blood_group,
        phone,
        city,
        last_donation
    )

    if result:
        st.success("Donor updated successfully")
    else:
        st.error("No donor found")