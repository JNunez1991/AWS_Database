#!/usr/bin/env python3
"""Orquestador principal del proyecto"""

from dataclasses import dataclass, asdict

import arrow

from config import Rutas, Meses
from src.webscrap import Run


@dataclass
class Main:
    """Clase principal que se encarga de orquestar el webscrapping y la persistencia de datos"""

    def run_all(self):
        """Ejecuta el proceso paso a paso"""

        # Obtiene año/mes desde el usuario
        anio, mes = self.user_input()
        mes = self.month_to_string(mes)

        # Llamo al controller que orquesta la descarga de informacion
        controller = Run(Rutas.BASE_INE, mes, anio)
        data = controller.run_all()

        return data


    def user_input(self) -> tuple[int, int]:
        """Mes y Año ingresado por el usuario"""

        while True:
            year = self.user_year()
            month = self.user_month()

            now = arrow.now().date()
            current_year, current_month = now.year, now.month

            if (year, month) <= (current_year, current_month):
                return year, month
            else:
                tope = f"{current_month}/{current_year}"
                msg = f"  -- [ERROR]: La combinación mes/año debe ser menor a {tope} "
                print(msg)

    def user_year(self) -> int:
        """El usuario ingresa el año"""

        while True:
            try:
                anio = int(input("Introduzca un año (2023 o posterior): "))
                if anio >= 2023:
                    return anio
                else:
                    print("  -- [ERROR]: El año debe ser mayor o igual a 2023.")
            except ValueError:
                print("  -- [ERROR]: Por favor, introduce un número entero válido.")

    def user_month(self) -> int:
        """El usuario ingresa el año"""

        while True:
            try:
                mes = int(input("Introduce un número de mes (1-12): "))
                if 1 <= mes <= 12:
                    return mes
                else:
                    print("  -- [ERROR]: El mes debe estar entre 1 y 12.")
            except ValueError:
                print("  -- [ERROR]: Por favor, introduce un número entero válido.")

    def month_to_string(self, month:int) -> str:
        """Transforma el numero de mes en su correspondiente nombre"""

        meses = asdict(Meses())
        meses_invertido = {v: k for k, v in meses.items()}
        return meses_invertido[month].lower()








if __name__ == "__main__":

    main = Main()
    z = main.run_all()
