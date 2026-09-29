import streamlit as st
from donor_db import DonorCreateRetrieveUpdateDelete

st.title("Delete Donor")

donor_id = st.number_input(
    "Enter Donor ID",
    min_value=1,
    step=1
)

btn = st.button("Delete")

if btn:

    b = DonorCreateRetrieveUpdateDelete()

    result = b.delete(donor_id)

    if result:
        st.success("Donor deleted successfully")
    else:
        st.error("No donor found")