"""
Functions that actually talk to the database. Keeping this separate from
main.py keeps route handlers thin and the DB logic testable/reusable.

Each function takes a `db: Session` (passed in from the route via dependency
injection) plus whatever data it needs.
"""
from typing import Any

from sqlalchemy.orm import Session
from . import models, schemas
from .models import Note

class NoteService:

    def __init__(self, session: Session):
        self._db = session


    def get_note(self, note_id: int) -> Note | None:
        return self._db.query(models.Note).filter(models.Note.id == note_id).first()

    def get_notes(self, skip: int = 0, limit: int = 100) -> list[type[Note]]:
        return self._db.query(models.Note).offset(skip).limit(limit).all()

    def create_note(self, note: schemas.NoteCreate) -> Note:
        new_note = models.Note(**note.model_dump())

        # TODO: call classify() on the note's text, set new_note.tag before saving
        # Hint: from ..ml.classify import classify
        #       combine title + content into one string (same format as training data)
        #       new_note.tag = classify(combined_text)

        self._db.add(new_note)
        self._db.commit()
        self._db.refresh(new_note)
        return new_note

    def update_note(self, note_id: int, note: schemas.NoteUpdate) -> Note | None:
        existing_note = self.get_note(note_id)
        if not existing_note:
            return None

        updated_data = note.model_dump(exclude_unset=True)
        for field, value in updated_data.items():
            setattr(existing_note, field, value)


        self._db.commit()
        self._db.refresh(existing_note)
        return existing_note

    def delete_note(self, note_id: int) -> bool:
        existing_note = self.get_note(note_id)

        if not existing_note:
            return False

        self._db.delete(existing_note)
        self._db.commit()

        return True
