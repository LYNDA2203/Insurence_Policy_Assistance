import google.generativeai as genai

from app.config import settings

from app.utils import (
    extract_text_from_pdf,
    split_documents
)

from app.vectorstore import (
    create_vector_store,
    search_documents
)

from app.prompt import get_prompt


genai.configure(
    api_key=settings.GOOGLE_API_KEY
)

model = genai.GenerativeModel(
    settings.LLM_MODEL
)


def build_vector_database(pdf_path):
    """
    Build FAISS vector database from uploaded PDF.
    """

    documents = extract_text_from_pdf(pdf_path)

    chunks = split_documents(documents)

    create_vector_store(chunks)


def retrieve_context(question):
    """
    Retrieve relevant chunks.
    """

    documents = search_documents(question)

    context = ""

    for doc in documents:

        page = doc.metadata.get("page", 0)

        context += (
            f"Page {page + 1}\n"
            f"{doc.page_content}\n\n"
        )

    return context


def generate_answer(question):
    """
    Generate grounded answer using Gemini.
    """

    context = retrieve_context(question)

    prompt = get_prompt(
        context=context,
        question=question
    )

    response = model.generate_content(prompt)

    return response.text


def ask_question(question):
    """
    Main entry point for question answering.
    """

    return generate_answer(question)