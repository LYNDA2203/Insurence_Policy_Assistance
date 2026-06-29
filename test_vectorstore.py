from app.utils import extract_text_from_pdf, split_documents
from app.vectorstore import create_vector_store

pdf_path = "uploads/New-Jeevan-Amar-Sales-Brochure.pdf"

documents = extract_text_from_pdf(pdf_path)

chunks = split_documents(documents)

create_vector_store(chunks)

print("Vector store created successfully!")