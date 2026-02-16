import sqlite3

from database.queries import DB_PATH, SELECT_ALL, DELETE_LIBRO, SELECT_DISPONIBLES, SELECT_LIBRO, INSERT_LIBRO, \
    UPDATE_LIBRO


class GestionBD:

    def obtener_libros(self):
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(SELECT_ALL)
            libros = cursor.fetchall()
            return libros

    def eliminar_libro(self, id) -> str:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(DELETE_LIBRO, (id, ))
            return f"Libro eliminado {id}"

    def actualizar_libro(self, titulo, anio, fecha_adquisicion, disponible, n_usuario, fecha_prestamo, id) -> str:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(UPDATE_LIBRO, (titulo, anio, fecha_adquisicion, disponible, n_usuario, fecha_prestamo, id))
            return f"Libro actualizado {titulo}"

    def insertar_nuevo_libro(self, isbn, titulo, anio, fecha_adquisicion, disponible, n_usuario, fecha_prestamo) -> str:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(INSERT_LIBRO, (isbn, titulo, anio, fecha_adquisicion, disponible, n_usuario, fecha_prestamo))
            return f"Libro insertado {titulo}"

    def obtener_libros_disponibles(self, disponible):
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(SELECT_DISPONIBLES, (disponible, ))
            libros = cursor.fetchall()
            return libros

    def buscar_por_anio(self, anio):
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(SELECT_LIBRO, (anio, ))
            libros = cursor.fetchall()
            return libros