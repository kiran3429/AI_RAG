import streamlit as st


def chat_component():

    st.subheader("💬 Ask a Question")

    question = st.text_input(
        "Enter your question"
    )

    ask = st.button("Ask")

    return question, ask