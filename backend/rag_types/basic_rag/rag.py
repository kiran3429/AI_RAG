from dotenv import load_dotenv
import os
from services.vector_store import vectorstore
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

def answer_question(question):
    vector_store = vectorstore()
    docs = vector_store.similarity_search(
        question,
        k=3
    )

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )

    prompt = f"""
You are an AI assistant.

Answer ONLY using the provided context.

If the answer is not present, say:

"I couldn't find this information in the uploaded document."

Context:
{context}

Question:
{question}
"""

    response = llm.invoke(prompt)

    return response.content