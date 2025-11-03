from fastapi import APIRouter, Form, UploadFile, File, status, Depends, HTTPException
from fastapi.responses import StreamingResponse, Response
from typing import List

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.files_model import FileModel
from core.deps import get_session

router = APIRouter()

# @router.post("/")
# async def create_upload_file(file: UploadFile = File(...)):
#     return {"filename": file.filename}

# @router.post("/savefile")
# async def save_upload_file(file: UploadFile = File(...)):
#     with open(f"api/v1/routes/uploads/{file.filename}", "wb") as f:
#         f.write(file.file.read())

#     return {"message": f"File {file.filename} saved successfully"}

# @router.post("/multiplefiles")
# async def multiple_files(files: List[UploadFile] = File(...)):
#     return {f"filenames": [file.filename for file in files]}

@router.post("/upload_db")
async def upload_file_to_db(file: UploadFile = File(...), db: AsyncSession = Depends(get_session)):
    try: 
        content = await file.read()
        new_file = FileModel(
            filmename = file.filename,
            content_type = file.content_type,
            content = content
        )

        db.add(new_file)
        await db.commit()

        await db.refresh(new_file)

        return {"id": new_file.id, "filename": new_file.filmename, "content_type": new_file.content_type}
    
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.get("/download/{id_file}")
async def download_file(id_file: int, db: AsyncSession = Depends(get_session)):
    try: 
        async with db as session:
            query = select(FileModel).filter(FileModel.id == id_file)
            result = await session.execute(query)
            file_db = result.scalar_one_or_none()

        if not file_db:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = "file not found")
        
        async def file_iterator(data: bytes):
            yield data

        return StreamingResponse(
            file_iterator(file_db.content),
            media_type = file_db.content_type,
            headers = {
                "Content-Disposition": f"attachment; filename={file_db.filmename}"
            }
        )
        
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Erro ao realizar o download: {e}")