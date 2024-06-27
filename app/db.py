from sqlmodel import Session, create_engine, SQLModel
import psycopg2
from psycopg2.extras import RealDictCursor
import sqlite3

import configparser

import conf


# engine = create_engine(conf.postgresql_url, echo=False, pool_pre_ping=True)
engine = create_engine(conf.sqlite_url, echo=False, pool_pre_ping=True)


def get_session():
    with Session(engine) as session:
        yield session


def get_cursor():
    # connect = psycopg2.connect(dbname=conf.db_name, user=conf.db_user,
    #                            password=conf.db_password, host=conf.db_host,
    #                            port=conf.db_port)
    # cur = connect.cursor(cursor_factory=RealDictCursor)
    connect = sqlite3.connect(conf.sqlite_url)
    cur = connect.cursor()

    return connect, cur


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
