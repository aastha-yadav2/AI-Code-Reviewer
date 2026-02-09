from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter

import os


def create_vector_db():

    files = [
        "rag_data/clean_code.txt",
        "rag_data/solid.txt",
        "rag_data/security.txt",
        "rag_data/performance.txt"
    ]

    docs = []

    for file in files:
        loader = TextLoader(file)
        docs.extend(loader.load())

    splitter = CharacterTextSplitter(chunk_size=200, chunk_overlap=20)
    split_docs = splitter.split_documents(docs)

    embeddings = HuggingFaceEmbeddings()

    db = Chroma.from_documents(
        split_docs,
        embeddings,
        persist_directory="db"
    )

    

    return db



def get_relevant_knowledge(query):

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")


    db = Chroma(
        persist_directory="db",
        embedding_function=embeddings
    )

    docs = db.similarity_search(query, k=3)

    context = ""

    for d in docs:
        context += d.page_content + "\n"

    return context
