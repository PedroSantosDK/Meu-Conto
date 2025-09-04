from __init__ import db
from sqlalchemy import Column, Text, Integer

class Livros(db.Model):
    __tablename__ = "Livros"

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    titulo = Column(Text, unique=True, nullable=False)
    historia = Column(Text, unique=True, nullable=False)