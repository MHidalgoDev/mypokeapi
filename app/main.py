from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.database import SessionLocal, engine
from fastapi.staticfiles import StaticFiles  # <-- importamos

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Montamos el frontend estático (HTML/JS/CSS)
app.mount("/", StaticFiles(directory="app/static", html=True), name="static")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Aquí van tus endpoints REST
@app.post("/pokemons/", response_model=schemas.Pokemon)
def create_pokemon(pokemon: schemas.PokemonCreate, db: Session = Depends(get_db)):
    return crud.create_pokemon(db=db, pokemon=pokemon)

# ... (los demás endpoints)
