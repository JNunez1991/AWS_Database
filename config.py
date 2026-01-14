#!/usr/bin/env python3
"""Orquestador principal del proyecto"""

import os
from dataclasses import dataclass
from enum import StrEnum
from pathlib import Path

class Rutas(StrEnum):
    """URLs del proyecto"""

    ROOT_PATH = os.path.abspath(Path(__file__).resolve().parent)
    INE_URL = "https://www.gub.uy/instituto-nacional-estadistica/comunicacion/publicaciones"



@dataclass(frozen=True)
class Meses:
    """Meses del año"""

    enero: int = 1
    febrero: int = 2
    marzo: int = 3
    abril: int = 4
    mayo: int = 5
    junio: int = 6
    julio: int = 7
    agosto: int = 8
    septiembre: int = 9
    octubre: int = 10
    noviembre: int = 11
    diciembre: int = 12
