# app/crud.py
from sqlalchemy.orm import Session
from app import models, schemas

def get_pokemon(db: Session, pokemon_id: int):
    return db.query(models.Pokemon).filter(models.Pokemon.id == pokemon_id).first()

def get_pokemons(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Pokemon).offset(skip).limit(limit).all()

def create_pokemon(db: Session, pokemon: schemas.PokemonCreate):
    db_pokemon = models.Pokemon(**pokemon.dict())
    db.add(db_pokemon)
    db.commit()
    db.refresh(db_pokemon)
    return db_pokemon

def update_pokemon(db: Session, pokemon_id: int, pokemon: schemas.PokemonCreate):
    db_pokemon = get_pokemon(db, pokemon_id)
    if not db_pokemon:
        return None
    db_pokemon.nombre = pokemon.nombre
    db_pokemon.tipo = pokemon.tipo
    db_pokemon.numero_pokedex = pokemon.numero_pokedex
    db.commit()
    db.refresh(db_pokemon)
    return db_pokemon

def delete_pokemon(db: Session, pokemon_id: int):
    db_pokemon = get_pokemon(db, pokemon_id)
    if not db_pokemon:
        return None
    db.delete(db_pokemon)
    db.commit()
    return db_pokemon
