from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

def load_documents():
    base_path = os.path.join(os.getcwd(), "Data")

    loaders = [
        TextLoader(os.path.join(base_path, "own_funds_cet1.txt")),
        TextLoader(os.path.join(base_path, "c01_instructions.txt"))
    ]

    documents = []
    for loader in loaders:
        documents.extend(loader.load())

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    return splitter.split_documents(documents)