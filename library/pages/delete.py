import streamlit as st

from librarydb import BookListCreateRetrieveUpdateDelete

st.title("Delete Record")

i = st.number_input("Enter Id", min_value=0)

btn = st.button("Delete")

if btn:
    b = BookListCreateRetrieveUpdateDelete()

    records = b.delete(i)

    print(records)

    if records:
        st.success("Record Deleted Successfully")
    else:
        st.error("No Record Found")