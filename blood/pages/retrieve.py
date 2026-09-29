import streamlit as st
from donor_db import DonorCreateRetrieveUpdateDelete

st.title("Retrieve Donor")

donor_id = st.number_input(
    "Enter Donor ID",
    min_value=1,
    step=1
)

btn = st.button("Retrieve")

if btn:

    b = DonorCreateRetrieveUpdateDelete()

    record = b.retrieve(donor_id)

    if record:

        st.write("ID =", record[0])
        st.write("Name =", record[1])
        st.write("Blood Group =", record[2])
        st.write("Phone =", record[3])
        st.write("City =", record[4])
        st.write("Last Donation =", record[5])

    else:

        st.error("No donor found")