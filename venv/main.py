import streamlit as st
from langhchain_main import get_qa_chain, create_vector_db
import os
st.title("Q&A Retrieval 🌱")

# st.write(f"Current working directory: {os.getcwd()}")
btn = st.button("Create Knowledgebase")
if btn:
    create_vector_db()

question = st.text_input("Question: ")

if question:
    chain = get_qa_chain()
    response = chain(question)

    st.header("Answer")
    st.write(response["result"])