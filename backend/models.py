from sqlalchemy import Column, Integer, String
from database import Base, engine

class User(Base):
    __tablename__ = "user"

    id: int = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username: str = Column(String(255), unique=True, index=True)
    hashed_password = Column(String(255))

User.metadata.create_all(bind=engine)