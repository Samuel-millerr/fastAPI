from fastapi import APIRouter, Form, UploadFile, File, status, Depends, HTTPException
from typing import List

router = APIRouter()

@router.post("/")
async def create_upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename}

@router.post("/savefile")
async def save_upload_file(file: UploadFile = File(...)):
    with open(f"api/v1/routes/uploads/{file.filename}", "wb") as f:
        f.write(file.file.read())

    return {"message": f"File {file.filename} saved successfully"}

@router.post("/multiplefiles")
async def multiple_files(files: List[UploadFile] = File(...)):
    return {f"filenames": [file.filename for file in files]}