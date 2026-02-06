from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
import os

VECTORSTORE_PATH = "vectorstore/corep_rules"

def load_vectorstore():
    """
    Loads the FAISS vectorstore from disk
    """
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    if not os.path.exists(VECTORSTORE_PATH):
        raise FileNotFoundError(
            "Vectorstore not found. Run build_vectorstore.py first."
        )

    vectorstore = FAISS.load_local(
        VECTORSTORE_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )

    return vectorstore


def retrieve_rules(question: str, k: int = 4):
    """
    Retrieves top-k relevant regulatory text chunks
    """
    vectorstore = load_vectorstore()
    docs = vectorstore.similarity_search(question, k=k)
    return docs


# ---------------- TEST RUN ----------------
if __name__ == "__main__":
    query = "How should retained earnings be reported in CET1?"
    results = retrieve_rules(query)

    print("\n🔍 Retrieved Regulatory References:\n")
    for i, doc in enumerate(results, 1):
        print(f"--- Rule {i} ---")
        print(doc.page_content)
        print("-" * 50)