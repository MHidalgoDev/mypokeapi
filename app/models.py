from sqlalchemy import Column, Integer, String
from .database import Base

class Pokemon(Base):
    __tablename__ = "pokemons"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, index=True, nullable=False)
    tipo = Column(String, index=True, nullable=False)
    numero = Column(Integer, unique=True, index=True, nullable=False)
