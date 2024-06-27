from sqlmodel import Field, Relationship
from sqlalchemy import UniqueConstraint
from typing import Optional, List

from ..base import note


class NotePad(note.NotePadBase, table=True):
    id: int = Field(default=None, primary_key=True)


class Note(note.NoteBase, table=True):
    id: int = Field(default=None, primary_key=True)
