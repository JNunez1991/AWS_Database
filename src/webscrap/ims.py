#!/usr/bin/env python3
"""Orquestador principal de webscrapping"""

from dataclasses import dataclass, field
from io import StringIO

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .utils import Utils

@dataclass
class IndiceMedioSalarios:
    """Obtengo los datos de Nasdaq del ultimo mes"""

    url: str
    month: str
    year: int
    driver: webdriver.Chrome
    xpath:str = '//*[@id="block-starterkits-content"]/article/div/ul/li/a'
    utils: Utils = field(default_factory=Utils)

    def __post_init__(self):
        """Se ejecuta luego de instanciar la clase"""

        print("  -. Obteniendo datos de Indice Medio de Salarios...")
        self.url = f"{self.url}/indice-medio-salarios-ims-{self.month}-{self.year}"
        self.utils.check_url_exists(self.url)

    def run_all(self) -> pd.DataFrame:
        """Ejecuta la descarga paso a paso"""

        self.navigate()
        data = self.get_data()
        # data = self.clean_data(data)
        return data

    def navigate(self, wait_time:int=1) -> None:
        """Carga le dataframe desde la web"""

        self.driver.get(self.url)
        elemento = WebDriverWait(self.driver, wait_time).until(
                EC.element_to_be_clickable((By.XPATH, self.xpath))
            )
        elemento.click()

    def get_data(
        self,
        wait_time:int=3,
    ) -> pd.DataFrame:
        """Obtiene la data desde la web"""

        WebDriverWait(self.driver, wait_time).until(
            EC.presence_of_element_located((By.TAG_NAME, "table"))
        )

        html_content = StringIO(self.driver.page_source)
        tablas = pd.read_html(html_content)

        if not tablas:
            raise ValueError("   -- [ERROR]: No se encontraron tablas en la pagina")

        return tablas[0]

    def clean_data(
        self,
        data:pd.DataFrame,
    ) -> pd.DataFrame:
        """Limpieza de datos"""

        data = data.copy()
        data = data.dropna()
        return data.reset_index(drop=True)
