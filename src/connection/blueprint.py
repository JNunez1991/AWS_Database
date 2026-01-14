#!/usr/bin/env python3
"""Clase comun al resto de archivos del modulo"""

from dataclasses import dataclass

from mysql.connector.connection import MySQLConnection
from mysql.connector.cursor import MySQLCursor
from sqlalchemy.engine import Engine

@dataclass
class Credentials:
    """Clase donde se almacena la data scrappeada"""

    host:str
    port:str
    database:str
    user:str
    password:str

@dataclass
class SqlStructures:
    """Estructuras de la conexion"""

    connector: MySQLConnection
    cursor: MySQLCursor
    engine: Engine
