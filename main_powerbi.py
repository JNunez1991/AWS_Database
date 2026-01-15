#!/usr/bin/env python3
"""Orquestador principal del proyecto"""

from dataclasses import dataclass, field

import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine

from config import Rutas
from src.connection import SetConnection, Credentials


@dataclass
class GetData:
    """Obtiene la data desde AWS y la muestra en PowerBi"""

    engine:Engine = field(init=False)

    def __post_init__(self):
        """Se ejecuta luego de instanciar la clase"""

        connection = SetConnection(Rutas.ROOT_PATH)
        credentials = connection.get_credentials()
        self.engine = self.set_engine(credentials)

    def set_engine(self, creds:Credentials) -> Engine:
        """Establece el Engine para extraer la data"""

        string = "mysql+pymysql://"
        string += f"{creds.user}:{creds.password}@"
        string += f"{creds.host}:{creds.port}/{creds.database}"
        return create_engine(string, pool_pre_ping=True)

    def get(self, qry:str) -> pd.DataFrame:
        """Ejecuta cada etapa del proceso"""

        return pd.read_sql(text(qry), self.engine)


if __name__ == "__main__":
    getter = GetData()
    dataset = getter.get("CALL sp_get_iccv()")
