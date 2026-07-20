import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

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

def vectorstore():
    return FAISS.load_local(
        VECTORSTORE_DIR,
        embeddings,
        allow_dangerous_deserialization=True
    )    