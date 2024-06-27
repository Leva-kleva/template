from sqlmodel import SQLModel, Field, ARRAY, JSON, Integer
from sqlalchemy import UniqueConstraint, Column, String
from typing import Optional, List, Dict


class NotePadBase(SQLModel):
    name: str = Field(max_length=256, nullable=False, index=True)
    info: str = Field(max_length=1024, nullable=False)


class NoteBase(SQLModel):
    __table_args__ = (UniqueConstraint("title"),)
    title: str = Field(max_length=256, nullable=False, index=True)
    text: Optional[str] = Field(max_length=1024, nullable=True, index=False)

    notepad_id: int = Field(foreign_key="notepad.id")
