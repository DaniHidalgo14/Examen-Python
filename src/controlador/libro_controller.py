from src.modelo.gestion_bd import GestionBD


class Controller:
    def __init__(self):
        self.gestor = GestionBD()

    def mostrar_todos(self):
        libros = self.gestor.obtener_libros()
        return libros

    def mostrar_disponibles(self, disponible):
        libros = self.gestor.obtener_libros_disponibles(disponible)
        return libros

    def eliminar_libro(self, cod):
        mensaje = self.gestor.eliminar_libro(cod)
        return mensaje

    def actualizar_libro(self, titulo, anio, fecha_adquisicion, disponible, n_usuario, fecha_prestamo, id):
        mensaje = self.gestor.actualizar_libro(titulo, anio, fecha_adquisicion, disponible, n_usuario, fecha_prestamo, id)
        return mensaje

    def insertar_nuevo(self, isbn, titulo, anio, fecha_adquisicion, disponible, n_usuario, fecha_prestamo):
        mensaje = self.gestor.insertar_nuevo_libro(isbn, titulo, anio, fecha_adquisicion, disponible, n_usuario, fecha_prestamo)
        return mensaje