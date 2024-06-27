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

from helpers import data as dt  #, jwt_handler as jwth, schedule as sch, api as apih
# from helpers.roles import check_role
# import conf

from db import *


router = APIRouter(
    prefix="/api/v1",
    tags=["api"],
    responses={404: {"description": "Not found"}},
)


##### API ######
@router.post("/example", tags=["api"],)
async def example_post(*, session: Session = Depends(get_session), obj: models.schemas.CreateNotePad):

    access = True
    if not access:
        return JSONResponse(status_code=401, content={"detail": "not access"})

    obj_model = models.database.NotePad.from_orm(obj)
    obj, is_commit = dt.get_or_create(session, models.database.NotePad, obj_model)

    return obj
