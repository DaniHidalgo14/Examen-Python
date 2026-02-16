import sqlite3

import customtkinter as ctk

from database.base_de_datos import CrearBD
from database.queries import DB_PATH
from src.vista.ventana_principal import VentanaMain


bd = CrearBD()

ventana = VentanaMain()
ventana.mainloop()