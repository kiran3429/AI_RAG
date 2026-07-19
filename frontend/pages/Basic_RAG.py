import streamlit as st

from components.upload import upload_component
from components.chat import chat_component

from services.api import upload_pdf, ask_question

st.title("📄 Basic RAG")

# --------------------
# Upload Section
# --------------------

uploaded_file = upload_component()

if uploaded_file:
    if st.button("Upload"):
        with st.spinner("Uploading PDF..."):
            response = upload_pdf(uploaded_file)
        st.success(response["message"])

# --------------------
# Chat Section
# --------------------

st.divider()

question, ask = chat_component()

if ask and question:

    with st.spinner("Thinking..."):

        response = ask_question(question)

    st.success(response["answer"])