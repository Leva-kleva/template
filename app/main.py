from fastapi import FastAPI, Depends, Request, Response, HTTPException, Depends
from fastapi.openapi.utils import get_openapi
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import requestvars
from requestvars import g
import types
import uvicorn

from routers import api, front

from db import *


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

app.include_router(api.router)
app.include_router(front.router)


# ##### startup actions #####
@app.on_event("startup")
def on_startup():
    create_db_and_tables()


# @app.context_processor
# def inject_url():
#     return {"inject_data": "string"}


##### middleware #####
@app.middleware("http")
async def check_access(request: Request, call_next):
    # set global contest object "g"
    initial_g = types.SimpleNamespace()
    requestvars.request_global.set(initial_g)

    # use g
    g().field = "string"

    response = await call_next(request)

    return response


def custom_openapi():
    tags_metadata = [
        {
            "name": "example_tag",
            "description": "Description of tag",
        },
    ]

    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title="Test API",
        version="1.0",
        description="The test service",
        routes=app.routes,
        tags=tags_metadata,
    )
    app.openapi_schema = openapi_schema

    return app.openapi_schema


app.openapi = custom_openapi

if __name__ == '__main__':
    app_name = "main"
    uvicorn.run(app=f"{app_name}:app", host=conf.host, port=conf.port)
