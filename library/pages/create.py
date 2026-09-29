import streamlit as st
from librarydb import BookListCreateRetrieveUpdateDelete

st.title("Add New Record")

title = st.text_input("Enter book title")

a = st.text_input("Enter author name")

pg = st.number_input("Enter number of pages", min_value=1)

p = st.number_input("Enter price", min_value=0)

l = st.selectbox(
    "Select language",
    ("English", "Malayalam")
)

btn = st.button("Add")

if btn:
    b = BookListCreateRetrieveUpdateDelete()

    b.create(title, a, pg, p, l)

    st.success("Record created successfully")