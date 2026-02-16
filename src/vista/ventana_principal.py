import sqlite3
from tkinter import ttk, messagebox
import customtkinter as ctk

from database.queries import DB_PATH
from src.controlador.libro_controller import Controller
from src.modelo.gestion_bd import GestionBD
from src.vista.ventana_exportar import VentanaExp
from src.vista.ventana_mensaje import mostrar_ventana_emergente


class VentanaMain(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.configurar_ventana()
        self.construir_ventana()
        self.controlador = Controller()
        self.mostrar_datos_libros()

    def configurar_ventana(self):
        self.title("Biblioteca")
        self.geometry("700x550")
        self.resizable(True, True)

    def construir_ventana(self):
        titulo = ctk.CTkLabel(self, text="Gestion Biblioteca", font=("Arial", 20))
        titulo.pack(pady=10)

        frame_entrys = ctk.CTkFrame(self, width=500, height=150)
        frame_entrys.grid_propagate(False)
        frame_entrys.pack(pady=10, padx=20)

        self.tituloEntrada = ctk.CTkEntry(frame_entrys, placeholder_text="Titulo")
        self.tituloEntrada.grid(row=0, column=0, padx=5, pady=10)

        self.anoEntrada = ctk.CTkEntry(frame_entrys, placeholder_text="Año")
        self.anoEntrada.grid(row=0, column=1, padx=5, pady=10)

        self.fechaEntrada = ctk.CTkEntry(frame_entrys, placeholder_text="Adquisicion : YYYY-MM-DD")
        self.fechaEntrada.grid(row=0, column=2, padx=5, pady=10)

        self.prestableEntrada = ctk.CTkEntry(frame_entrys, placeholder_text="Disponible?")
        self.prestableEntrada.grid(row=1, column=0, padx=5, pady=10)

        self.nUsuarioEntrada = ctk.CTkEntry(frame_entrys, placeholder_text="Nº de usuario")
        self.nUsuarioEntrada.grid(row=1, column=1, padx=5, pady=10)

        self.fPrestamoEntrada = ctk.CTkEntry(frame_entrys, placeholder_text="Prestamo: YYYY-MM-DD")
        self.fPrestamoEntrada.grid(row=1, column=2, padx=5, pady=10)

        self.isbnEntrada = ctk.CTkEntry(frame_entrys, placeholder_text="ISBN")
        self.isbnEntrada.grid(row=2, column=1, padx=5, pady=10)

        frame_botones = ctk.CTkFrame(self, width=500, height=100)
        frame_botones.grid_propagate(False)
        frame_botones.pack(pady=10, padx=20)

        anadirBtn = ctk.CTkButton(frame_botones, text="Añadir Libro", fg_color="green", command=self.insertar)
        anadirBtn.grid(row=0, column=0, padx=5, pady=10)

        modifBtn = ctk.CTkButton(frame_botones, text="Modificar Libro", command=self.actualizar_libro)
        modifBtn.grid(row=0, column=1, padx=5, pady=10)

        eliminarBtn = ctk.CTkButton(frame_botones, text="Eliminar Libro", fg_color="red", command=self.eliminar_libro)
        eliminarBtn.grid(row=0, column=2, padx=5, pady=10)

        exportarBtn = ctk.CTkButton(frame_botones, text="Exportar a CSV", fg_color="blue", command=self.exportar_a_csv)
        exportarBtn.grid(row=1, column=1, padx=5, pady=10)

        buscarBtn = ctk.CTkButton(frame_botones, text="Disposiciones", fg_color="blue", command=self.mostrar_libros_disponibles)
        buscarBtn.grid(row=1, column=0, padx=5, pady=10)

        frame_tabla = ctk.CTkFrame(self, width=700, height=250)
        frame_tabla.pack_propagate(False)
        frame_tabla.pack(pady=10, padx=20)

        scrollbar = ttk.Scrollbar(frame_tabla)
        scrollbar.pack(side="right", fill="y")

        self.tabla = ttk.Treeview(frame_tabla, columns=("ISBN", "Titulo", "Ano", "Fecha Adquisicion", "Disponible", "Nº Usuario", "Fecha Prestamo"),
                                  show="headings", yscrollcommand=scrollbar.set)

        self.tabla.heading("ISBN", text="ISBN")
        self.tabla.heading("Titulo", text="Titulo")
        self.tabla.heading("Ano", text="Año")
        self.tabla.heading("Fecha Adquisicion", text="Fecha Adquisicion")
        self.tabla.heading("Disponible", text="Disponible")
        self.tabla.heading("Nº Usuario", text="N Usuario")
        self.tabla.heading("Fecha Prestamo", text="Fecha Prestamo")

        self.tabla.column("ISBN", width=50)
        self.tabla.column("Titulo", width=150)
        self.tabla.column("Ano", width=50)
        self.tabla.column("Fecha Adquisicion", width=100)
        self.tabla.column("Disponible", width=75)
        self.tabla.column("Nº Usuario", width=75)
        self.tabla.column("Fecha Prestamo", width=75)

        self.tabla.pack(fill="both", expand=True)

    def limpiar_tabla(self):
        for item in self.tabla.get_children():
            self.tabla.delete(item)

    def mostrar_datos_libros(self):
        libros = self.controlador.mostrar_todos()

        for libro in libros:
            self.tabla.insert("", "end", iid=libro[0],
                              values=(libro[1], libro[2], libro[3], libro[4], libro[5], libro[6], libro[7]))

    def mostrar_libros_disponibles(self):
        try:
            disponible = self.getint(self.prestableEntrada.get())

            if disponible not in (0, 1):
                mostrar_ventana_emergente("Error", "Error", "Campo disponible erroneo")
            else:
                self.limpiar_tabla()
                libros = self.controlador.mostrar_disponibles(disponible)

                for libro in libros:
                    self.tabla.insert("", "end", iid=libro[0],
                                      values=(libro[1], libro[2], libro[3], libro[4], libro[5], libro[6], libro[7]))
        except ValueError:
            self.limpiar_tabla()
            self.mostrar_datos_libros()

    def insertar(self):
        try:
            isbn = int(self.isbnEntrada.get())
            titulo = self.tituloEntrada.get()
            anio = int(self.anoEntrada.get())
            fecha_adq = self.fechaEntrada.get()
            prestable = self.prestableEntrada.get()
            n_usuario = int(self.nUsuarioEntrada.get())
            prestamo = self.fPrestamoEntrada.get()

            if n_usuario == "" or prestamo == "":
                mensaje = self.controlador.insertar_nuevo(isbn, titulo, anio, fecha_adq, prestable, None, None)
                self.limpiar_tabla()
                self.mostrar_datos_libros()
                mostrar_ventana_emergente("Informacion", "Informacion", mensaje)
            else:
                mensaje = self.controlador.insertar_nuevo(isbn, titulo, anio, fecha_adq, prestable, n_usuario, prestamo)
                self.limpiar_tabla()
                self.mostrar_datos_libros()
                mostrar_ventana_emergente("Informacion", "Informacion", mensaje)
        except ValueError:
            mostrar_ventana_emergente("Error", "Error", "Campos vacios o incorrectos")

    def eliminar_libro(self):
        seleccion = self.tabla.selection()

        if not seleccion:
            mostrar_ventana_emergente("Error", "Error", "Seleccione un item")
        else:
            cod = seleccion[0]
            self.controlador.eliminar_libro(cod)
            mostrar_ventana_emergente("Informacion", "Informacion", f"Libro eliminado {cod}")
            self.limpiar_tabla()
            self.mostrar_datos_libros()

    def actualizar_libro(self):
        try:
            seleccion = self.tabla.selection()
            titulo = self.tituloEntrada.get()
            anio = int(self.anoEntrada.get())
            fecha_adq = self.fechaEntrada.get()
            prestable = self.prestableEntrada.get()
            n_usuario = int(self.nUsuarioEntrada.get())
            prestamo = self.fPrestamoEntrada.get()

            if not seleccion:
                mostrar_ventana_emergente("Error", "Error", "Seleccione un item")
            else:
                cod = seleccion[0]
                if not n_usuario or not prestamo:
                    mensaje = self.controlador.actualizar_libro(titulo, anio, fecha_adq, prestable, None, None, cod)
                    self.limpiar_tabla()
                    self.mostrar_datos_libros()
                    mostrar_ventana_emergente("Informacion", "Informacion", mensaje)
                else:
                    mensaje = self.controlador.actualizar_libro(titulo, anio, fecha_adq, prestable, n_usuario, prestamo, cod)
                    self.limpiar_tabla()
                    self.mostrar_datos_libros()
                    mostrar_ventana_emergente("Informacion", "Informacion", mensaje)
        except ValueError:
            mostrar_ventana_emergente("Error", "Error", "Campos vacios o incorrectos")


    def exportar_a_csv(self):
        vista = VentanaExp(self.controlador)
        vista.mainloop()