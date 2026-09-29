import streamlit as st

from librarydb import BookListCreateRetrieveUpdateDelete

st.title("Retrieve Book")

book_id = st.number_input("Enter Book ID", min_value=1, step=1)

btn = st.button("Retrieve")

if btn:

    b = BookListCreateRetrieveUpdateDelete()

    record = b.retrieve(book_id)

    if record:

        st.write("Book ID =", record[0])
        st.write("Title =", record[1])
        st.write("Author =", record[2])
        st.write("Price =", record[3])
        st.write("Pages =", record[4])
        st.write("Language =", record[5])

    else:
        st.write("No record found")