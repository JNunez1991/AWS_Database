#!/usr/bin/env python3
"""Funciones auxiliares"""

from dataclasses import dataclass

import arrow

@dataclass
class Utils:
    """Funciones auxiliares"""

    meses:dict[str, int]

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

        meses_invertido = { v: k for k, v in self.meses.items() }
        return meses_invertido[month].lower()
