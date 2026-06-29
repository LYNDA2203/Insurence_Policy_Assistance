import os
import uvicorn

from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request

from app.rag import (
    build_vector_database,
    ask_question
)

from app.utils import (
    save_uploaded_file,
    create_upload_directory
)


app = FastAPI(
    title="Insurance Policy Q&A Assistant",
    version="1.0.0"
)

# Enable CORS

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create uploads folder

create_upload_directory()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    )

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    if not file.filename.endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    filepath = save_uploaded_file(file)

    build_vector_database(filepath)

    return {
        "status": "success",
        "message": "PDF uploaded and indexed successfully."
    }


@app.post("/ask")
async def ask(data: dict):

    question = data.get("question")

    if not question:
        raise HTTPException(
            status_code=400,
            detail="Question is required."
        )

    answer = ask_question(question)

    return {
        "question": question,
        "answer": answer
    }


if __name__ == "__main__":

    
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )