import streamlit as st


def upload_component():

    uploaded_file = st.file_uploader(
        "Choose a PDF",
        type=["pdf"]
    )

    if uploaded_file is not None:
        st.success(f"Selected: {uploaded_file.name}")

    return uploaded_file