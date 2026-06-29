import os
import shutil

from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.config import settings

def create_upload_directory():

    os.makedirs(settings.UPLOAD_FOLDER,exist_ok=True)

def save_uploaded_file(file):

    filepath = os.path.join(settings.UPLOAD_FOLDER,file.filename)

    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(file.file,buffer)

    return filepath

def extract_text_from_pdf(pdf_path):

    loader = PyMuPDFLoader(pdf_path)

    documents = loader.load()

    return documents

def split_documents(documents):

    splitter = RecursiveCharacterTextSplitter(

        chunk_size=settings.CHUNK_SIZE,

        chunk_overlap=settings.CHUNK_OVERLAP

    )

    chunks = splitter.split_documents(documents)

    return chunks

def clean_text(text):

    text = text.replace("\n", " ")

    text = text.replace("\t", " ")

    text = " ".join(text.split())

    return text

def delete_uploaded_file(filepath):

    if os.path.exists(filepath):

        os.remove(filepath)
    