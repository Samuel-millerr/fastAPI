from core.config import settings
from sqlalchemy import Column, Integer, String, LargeBinary

class FileModel(settings.DBBaseModel):
    __tablename__ = "files"

    id: int = Column(Integer(), primary_key=True, index=True, autoincrement=True)
    filmename: str = Column(String(255), index=True, nullable=False)
    content_type: str = Column(String(255), nullable=False)
    content = Column(LargeBinary(), nullable=False)