import csv

import customtkinter as ctk

from src.vista.ventana_mensaje import mostrar_ventana_emergente


class VentanaExp(ctk.CTk):
    def __init__(self, gestion_bd):
        super().__init__()
        self.configurar_ventana()
        self.construir_ventana()
        self.gestion_bd = gestion_bd

    def configurar_ventana(self):
        self.title("Exportar a CSV")
        self.geometry("200x200")
        self.resizable(False, False)

    def construir_ventana(self):
        titulo = ctk.CTkLabel(self, text="Exportar a CSV", font=("Arial", 20))
        titulo.pack(pady=10)

        titulo = ctk.CTkLabel(self, text="Nombre del archivo:")
        titulo.pack(pady=10)

        self.nombreEntrada = ctk.CTkEntry(self)
        self.nombreEntrada.pack(pady=10)

        guardarBtn = ctk.CTkButton(self, text="Guardar", command=self.guardar_en_csv)
        guardarBtn.pack(pady=10)


    def guardar_en_csv(self):
        rutaArchivo = self.nombreEntrada.get()
        libros = self.gestion_bd.mostrar_todos()
        with open(rutaArchivo, mode="w", newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["ISBN", "Titulo", "Año", "Fecha Adquisicion", "Disponible", "Nº Usuario", "Fecha Prestamo"])
            for libro in libros:
                writer.writerow([libro[1], libro[2], libro[3], libro[4], libro[5], libro[6], libro[7]])

        mostrar_ventana_emergente("Informacion", "Info", f"Datos exportados a {rutaArchivo}")
        self.destroy()