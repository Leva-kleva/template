from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import time
from typing import List

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from fastapi import FastAPI, Depends, Request, Response, HTTPException, Depends
from fastapi.openapi.utils import get_openapi
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from typing import List, Union, Optional
from fastapi.responses import JSONResponse, FileResponse, StreamingResponse
import requestvars
from requestvars import g
import types
import models
from sqlmodel import Field, Session, SQLModel, create_engine, select, update, func, case
from sqlalchemy.orm import aliased
import time, datetime
import uvicorn
from hashlib import sha256
import psycopg2
from psycopg2.extras import RealDictCursor
# import jwt

# import conf

from db import *


router = APIRouter(
    prefix="",
    tags=["front"],
    responses={404: {"description": "Not found"}},
)


templates = Jinja2Templates(directory="templates")


##### FRONT ######
@router.get("/example/{id_}", tags=["front"],)
def example_get(*, session: Session = Depends(get_session), request: Request, id_: int):
    query = session.query(models.database.NotePad).where(models.database.NotePad.id==id_)

    return query.all()


@router.get("/index", tags=["front"], response_class=HTMLResponse)
def index(*, session: Session = Depends(get_session), request: Request):
#     return templates.TemplateResponse(request=request, name="index.html", context={"param": "param"})
    return templates.TemplateResponse("index.html", context={"request": request, "param": "param"})


