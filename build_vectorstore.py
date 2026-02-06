from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from load_documents import load_documents
import os

def build_vectorstore():
    docs = load_documents()

    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.from_documents(docs, embeddings)
    os.makedirs("vectorstore", exist_ok=True)
    vectorstore.save_local("vectorstore/corep_rules")

    print("Vectorstore created successfully (FREE embeddings)")

if __name__ == "__main__":
    build_vectorstore()