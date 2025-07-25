# app/schemas.py
from pydantic import BaseModel

class PokemonBase(BaseModel):
    nombre: str
    tipo: str
    numero_pokedex: int

class PokemonCreate(PokemonBase):
    pass

class Pokemon(PokemonBase):
    id: int

    class Config:
        orm_mode = True
