import streamlit as st
from donor_db import DonorCreateRetrieveUpdateDelete

st.title("All Donors")

b = DonorCreateRetrieveUpdateDelete()

records = b.list()

if records:
    st.table(records)
else:
    st.write("No donors found")