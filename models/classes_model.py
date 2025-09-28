from core.config import settings
from sqlalchemy import Column, Integer, String, Boolean, Float, Text, ForeignKey, Date
from sqlalchemy.orm import relationship

class ClassModel(settings.DBBaseModel):
    __tablename__ = 'turma'

    id_turma: int = Column(Integer(), primary_key=True, autoincrement=True)
    nome_turma: str = Column(String(100))
    padrinho: str = Column(String(100))
    qtd_alunos: int = Column(Integer())
    laboratorio: int = Column(String(100))
