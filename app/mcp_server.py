"""
MCP server exposing Note Classifier operations as tools for an LLM client
(e.g. Claude Desktop) to call directly.

THE CORE IDEA: this file doesn't reimplement any logic. It's a thin adapter
that wraps your existing NoteService methods as "tools" an LLM can discover
and call. Same backend, new front door.

WHY A SEPARATE DB SESSION HERE (not the same get_db() from main.py):
FastAPI's get_db() is a generator built for FastAPI's own Depends() injection
system request-by-request. MCP has its own lifecycle (it's not running inside
FastAPI's request loop), so we manage a session more directly here. Later, if
we mount MCP inside the FastAPI app itself (Phase 3 stretch goal), this gets
unified — for now, keeping them separate keeps each piece easy to reason about.


Run it directly to sanity check it starts without errors:
    python -m app.mcp_server
(it will look like it "hangs" — that's correct, it's waiting on stdio for a
client to connect. Ctrl+C to stop.)
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from mcp.server.fastmcp import FastMCP
from app.database import SessionLocal
from app.schemas import NoteCreate
from app.crud import NoteService
from ml.classify import classify

mcp = FastMCP('note-classifier')


@mcp.tool()
def create_note(title: str, content: str) -> dict:
    """Create a new note. The note is automatically tagged by category (work, personal, idea, urgent)."""
    db = SessionLocal()

    try:
        service = NoteService(session=db)
        note = service.create_note(NoteCreate(title=title, content=content))
        return {"id": note.id, "title": note.title, "content": note.content, "tag": note.tag}

    finally:
        db.close()


@mcp.tool()
def list_notes(skip: int = 0, limit: int = 100) -> list[dict]:
    """List existing notes, with optional pagination."""
    db = SessionLocal()

    try:
        service = NoteService(session=db)
        notes = service.get_notes(skip=skip, limit=limit)
        return [
            {"id": n.id, "title": n.title, "content": n.content, "tag": n.tag}
            for n in notes
        ]
    finally:
        db.close()


@mcp.tool()
def get_note(note_id: int) -> dict | None:
    """Get a single note by its ID. Returns None if not found."""
    db = SessionLocal()

    try:
        service = NoteService(session=db)
        note = service.get_note(note_id)
        if note:
            return {"id": note.id, "title": note.title, "content": note.content, "tag": note.tag}
        return None

    finally:
        db.close()

@mcp.tool()
def classify_text(text: str) -> str:
    """Predict the category (work, personal, idea, urgent) for a piece of text,
    without creating a note."""

    return classify(text)



if __name__ == "__main__":
    mcp.run()

