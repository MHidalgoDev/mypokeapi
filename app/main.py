from fastapi import FastAPI, Depends, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
import os

from . import models, schemas, crud
from .database import SessionLocal, engine, Base

app = FastAPI()

# Crear tablas
Base.metadata.create_all(bind=engine)

# Montar static en /static
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    return FileResponse(os.path.join("static", "index.html"))

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/pokemons/", response_model=schemas.Pokemon)
def create_pokemon(pokemon: schemas.PokemonCreate, db: Session = Depends(get_db)):
    existing = db.query(models.Pokemon).filter(
        (models.Pokemon.nombre == pokemon.nombre) | 
        (models.Pokemon.numero == pokemon.numero)
    ).first()
    if existing:
        raise HTTPException(status_code=400, detail="Pokemon ya existe")
    return crud.create_pokemon(db, pokemon)

@app.get("/pokemons/", response_model=list[schemas.Pokemon])
def read_pokemons(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_pokemons(db, skip=skip, limit=limit)
