from fastapi import APIRouter, UploadFile, File
import shutil
import os

from rag_types.Basic_rag.rag import create_vectorstore

router = APIRouter()

UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/uploads")
async def upload(file: UploadFile = File(...)):

    path = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    create_vectorstore(path)

    return {
        "message": "Uploaded Successfully"
    }