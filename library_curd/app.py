import streamlit as st
from librarydb import BookListCreateRetrieveUpdateDelete

st.title("welcome to library app")
b=BookListCreateRetrieveUpdateDelete()

tab1,tab2,tab3,tab4,tab5=st.tabs(['add','read','retrieve','update','delete'])

with tab1:
    st.write("add")
with tab2:
    st.write("read")
with tab3:
    st.write("retrieve")
with tab4:
    st.write("update")
with tab5:
    st.write("delete")