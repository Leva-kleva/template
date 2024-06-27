from typing import Optional, List, Union, Dict
from sqlmodel import SQLModel
from pydantic import validator, BaseModel
import datetime
from requestvars import g

from ..base import note


class CreateNote(note.NoteBase):
    pass


class CreateNotePad(note.NotePadBase):
    pass


class CreateNotePadWithNote(note.NotePadBase):
    notes: List[CreateNote]

    @validator("notes")
    def date_to_iso(cls, obj):
        return obj
