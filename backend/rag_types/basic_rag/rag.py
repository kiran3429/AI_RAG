from dotenv import load_dotenv
import os

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

embeddings = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5"
)

VECTORSTORE_DIR = "vectorstores"

os.makedirs(VECTORSTORE_DIR, exist_ok=True)


def create_vectorstore(pdf_path):

    loader = PyPDFLoader(pdf_path)

    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(docs)

    vector_store = FAISS.from_documents(
        chunks,
        embeddings
    )

    vector_store.save_local(VECTORSTORE_DIR)

    print("✅ Vector Store Created")


def answer_question(question):

    vector_store = FAISS.load_local(
        VECTORSTORE_DIR,
        embeddings,
        allow_dangerous_deserialization=True
    )

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