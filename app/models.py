# app/models.py
from sqlalchemy import Column, Integer, String
from app.database import Base

class Pokemon(Base):
    __tablename__ = "pokemons"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    tipo = Column(String, index=True)
    numero_pokedex = Column(Integer, unique=True, index=True)
