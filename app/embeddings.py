from langchain_huggingface import HuggingFaceEmbeddings
from app.config import settings



def load_embedding_model():
    """
    Load and return the HuggingFace embedding model.
    """

    embeddings = HuggingFaceEmbeddings(
        model_name=settings.EMBEDDING_MODEL
    )

    return embeddings

_embedding_model = HuggingFaceEmbeddings(
    model_name=settings.EMBEDDING_MODEL
)


def get_embedding_model():
    return _embedding_model