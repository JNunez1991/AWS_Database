#!/usr/bin/env python3
"""Clase comun al resto de archivos del modulo"""

from dataclasses import dataclass

@dataclass
class Credentials:
    """Clase donde se almacena la data scrappeada"""

    host:str
    port:str
    database:str
    user:str
    password:str
