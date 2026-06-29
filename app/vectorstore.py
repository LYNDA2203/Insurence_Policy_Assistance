import os

from langchain_community.vectorstores import FAISS

from app.embeddings import get_embedding_model
from app.config import settings


def create_vector_store(chunks):
    """
    Create and save a FAISS vector database.
    """

    embeddings = get_embedding_model()

    vector_db = FAISS.from_documents(
        documents=chunks,
        embedding=embeddings
    )

    vector_db.save_local(settings.VECTOR_DB)

    return vector_db


def load_vector_store():
    """
    Load the saved FAISS vector database.
    """

    embeddings = get_embedding_model()

    vector_db = FAISS.load_local(
        settings.VECTOR_DB,
        embeddings,
        allow_dangerous_deserialization=True
    )

    return vector_db


def search_documents(question):
    """
    Retrieve the most relevant document chunks.
    """

    vector_db = load_vector_store()

    documents = vector_db.similarity_search(
        question,
        k=settings.TOP_K
    )

    return documents