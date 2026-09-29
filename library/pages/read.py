import streamlit as st

from librarydb import BookListCreateRetrieveUpdateDelete

st.title("Read New Record")

b = BookListCreateRetrieveUpdateDelete()

records = b.list()

if records:
    st.table(records)
else:
    st.write("No records found")