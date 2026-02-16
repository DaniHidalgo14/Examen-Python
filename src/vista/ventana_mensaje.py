from tkinter import messagebox

def mostrar_ventana_emergente(tipo : str, titulo : str, info : str):
    if tipo == "Error":
        messagebox.showerror(titulo, info)
    elif tipo == "Informacion":
        messagebox.showinfo(titulo, info)
    else:
        messagebox.showwarning(titulo, info)