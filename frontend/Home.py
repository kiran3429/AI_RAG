import streamlit as st

from services.api import get_rags

st.set_page_config(
    page_title="RAG Studio",
    layout="wide"
)

rags = get_rags()

st.title("🚀 RAG Studio")

st.subheader("Available RAG Architectures")

for rag in rags:

    with st.container():

        st.markdown(f"## {rag['name']}")

        st.write(rag["description"])