
from datetime import date
from typing import Optional
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.testing.schema import mapped_column

from .database import Base

class Note(Base):
    __tablename__ = 'notes'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(80))
    content: Mapped[str] = mapped_column(String(225))
    tag: Mapped[str] = mapped_column(String(225))
    created_at: Mapped[Optional[date]] = mapped_column() # optional but good practice