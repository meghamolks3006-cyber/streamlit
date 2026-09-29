import streamlit as st

from librarydb import BookListCreateRetrieveUpdateDelete

st.title("Update Record")

i = st.number_input("Enter Id", min_value=0)

title = st.text_input("Enter Title")
author = st.text_input("Enter Author")
price = st.number_input("Enter Price", min_value=0)
pages = st.number_input("Enter Pages", min_value=0)
language = st.text_input("Enter Language")

btn = st.button("Update")

if btn:
    b = BookListCreateRetrieveUpdateDelete()

    records = b.update(i, title, author, price, pages, language)

    print(records)

    if records:
        st.success("Record Updated Successfully")
    else:
        st.error("No Record Found")