
from datetime import datetime
from typing import Optional
from sqlalchemy import String, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column

from .database import Base

class Note(Base):
    __tablename__ = 'notes'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(80))
    content: Mapped[str] = mapped_column(String(225))
    tag: Mapped[Optional[str]] = mapped_column(String(225), nullable=True)
    created_at: Mapped[Optional[datetime]] = mapped_column(DateTime, server_default=func.now()) # optional but good practice