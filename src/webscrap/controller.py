#!/usr/bin/env python3
"""Orquestador principal de webscrapping"""

from dataclasses import dataclass

from selenium import webdriver

from .blueprint import StoredOutputs
from .ipc import IndicePreciosConsumo
from .ims import IndiceMedioSalarios


@dataclass
class Run:
    """Obtengo los datos de Nasdaq del ultimo mes"""

    url: str
    month: str
    year: int

    def run_all(self) -> StoredOutputs:
        """Ejecuta la descarga paso a paso"""

        driver = self.set_driver()

        # Datos de inflacion
        ipc = IndicePreciosConsumo(self.url, self.month, self.year, driver)
        data_ipc = ipc.run_all()

        # Datos de Unidad Indexada
        ims = IndiceMedioSalarios(self.url, self.month, self.year, driver)
        data_ims = ims.run_all()

        # Cierro driver
        driver.quit()

        return StoredOutputs(
            ipc=data_ipc,
            ims=data_ims,
        )


    def set_driver(self) -> webdriver.Chrome:
        """Setea el navegador web"""

        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        drv = webdriver.Chrome(options=options)
        return drv
