import os.path
import sqlite3

from database.queries import *


class CrearBD:
    def __init__(self):
        self.construir_bd()

    def construir_bd(self):
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(CREATE_TABLE)
            conn.commit()
            print("Creando / Comprobando base de datos")

        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(SELECT_ALL)
            libros = cursor.fetchall()

        if not libros:
            self.cargas_iniciales()

    def cargas_iniciales(self):
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.executescript(CARGA_INICIAL)
            conn.commit()
            print("Datos cargados exitosamente")