"""
The FastAPI app itself: route definitions wiring HTTP <-> crud.py.

Run locally with:
    uvicorn app.main:app --reload

Then check:
    http://127.0.0.1:8000/docs   <- interactive Swagger UI, test everything here
"""

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from . import models, schemas
from .crud import NoteService
from .database import engine, SessionLocal


def init_base():
    models.Base.metadata.create_all(bind=engine)

init_base()
app = FastAPI(title="Note Classifier API")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_note_service(db: Session = Depends(get_db)):
    return NoteService(session=db)

@app.post('/notes', response_model=schemas.NoteResponse, status_code=201)
def create_note(note: schemas.NoteCreate,service: NoteService = Depends(get_note_service)):

    new_note = service.create_note(note)
    return new_note

@app.get('/notes', response_model=list[schemas.NoteResponse], status_code=200)
def get_notes(skip: int = 0, limit: int = 100, service: NoteService = Depends(get_note_service)):

    return service.get_notes(skip=skip, limit=limit)

@app.get('/notes/{note_id}', status_code=200, response_model=schemas.NoteResponse)
def read_note(note_id: int, service: NoteService = Depends(get_note_service)):

    db_note = service.get_note(note_id=note_id)

    if db_note is None:
        raise HTTPException(
            status_code=404,
            detail='Note not found'
        )

    return db_note

@app.put('/notes/{note_id}', status_code=200, response_model=schemas.NoteResponse)
def update_note(note: schemas.NoteUpdate, note_id: int, service: NoteService = Depends(get_note_service)):

    updated_note = service.update_note(note_id=note_id, note=note)

    if updated_note is None:
        raise HTTPException(
            status_code=404,
            detail='Note not found'
        )

    return updated_note

@app.delete('/notes/{note_id}', status_code=204)
def delete_note(note_id: int, service: NoteService = Depends(get_note_service)):

    is_deleted = service.delete_note(note_id=note_id)

    if is_deleted:
        return None

    raise HTTPException(
        status_code=404,
        detail='Note not found'
    )
