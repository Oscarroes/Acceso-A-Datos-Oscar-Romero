import tkinter as tk
from customtkinter import *
from tkinter import messagebox, filedialog
from PIL import Image
import os

class VistaInsertar:

    def __init__(self, ventana, controlador, vista):
        self.ventana = ventana
        self.controlador = controlador
        self.vista = vista 

        self.imagenPath = tk.StringVar()
        self.ventanaInsertar = None

    
    def abrirVentanaInsertar(self):
            
            ventanaInsertar = tk.Toplevel(self.ventana)
            ventanaInsertar.geometry("896x896")
            ventanaInsertar.config(bg="#2E4C39")
            ventanaInsertar.title('Añade un nuevo libro')
            ventanaInsertar.iconbitmap('img/iconoLibros.ico')
            ventanaInsertar.lift()

            def posicionarVentana():
                ventanaInsertar.lift()
            
            def cancelarVentanaInsertar():
                ventanaInsertar.destroy()

            self.frameSeparador = CTkFrame(master=ventanaInsertar, fg_color="#2E4C39", height=10)
            self.frameSeparador.grid(row=0, column=0, padx=10, pady=5)

            #ENTRADA TÍTULO--------------------------------------------------

            self.etiquetaTitulo = CTkLabel(master=ventanaInsertar,
                                        text="Título: ",
                                        justify="left",
                                        anchor="w",
                                        width=200,
                                        font=("Roboto", 18, "bold"),
                                        text_color="#F6FFF9")
            self.etiquetaTitulo.grid(row=1, column=0, padx=10, pady=5)
            self.entradaTitulo = CTkEntry(master=ventanaInsertar,
                                        font=("Roboto", 12, "bold"),
                                        width=200)
            self.entradaTitulo.grid(row=1, column=1, padx=10, pady=5)

            #ENTRADA AUTOR-------------------------------------------------------

            self.etiquetaAutor = CTkLabel(master=ventanaInsertar,
                                        text="Autor: ",
                                        justify="left",
                                        anchor="w",
                                        width=200,
                                        font=("Roboto", 18, "bold"),
                                        text_color="#F6FFF9")
            self.etiquetaAutor.grid(row=2, column=0, padx=10, pady=5)
            self.entradaAutor = CTkEntry(master=ventanaInsertar,
                                        font=("Roboto", 12, "bold"),
                                        width=200)
            self.entradaAutor.grid(row=2, column=1, padx=10, pady=0)

            #ENTRADA GÉNERO-------------------------------------------------------

            self.etiquetaGenero = CTkLabel(master=ventanaInsertar,
                                        text="Género: ",
                                        justify="left",
                                        anchor="w",
                                        width=200,
                                        font=("Roboto", 18, "bold"),
                                        text_color="#F6FFF9")
            self.etiquetaGenero.grid(row=3, column=0, padx=10, pady=5)
            self.entradaGenero = CTkEntry(master=ventanaInsertar,
                                        font=("Roboto", 12, "bold"),
                                        width=200)
            self.entradaGenero.grid(row=3, column=1, padx=10, pady=5)

            #ENTRADA PÁGINAS-------------------------------------------------------

            self.etiquetaPaginas = CTkLabel(master=ventanaInsertar,
                                        text="Número de páginas: ",
                                        justify="left",
                                        anchor="w",
                                        width=200,
                                        font=("Roboto", 18, "bold"),
                                        text_color="#F6FFF9")
            self.etiquetaPaginas.grid(row=4, column=0, padx=10, pady=5)
            self.entradaPaginas = CTkEntry(master=ventanaInsertar,
                                        font=("Roboto", 12, "bold"),
                                        width=200)
            self.entradaPaginas.grid(row=4, column=1, padx=10, pady=5)

            #ENTRADA FECHA DE PUBLICACIÓN-------------------------------------------------------

            self.etiquetaFecha = CTkLabel(master=ventanaInsertar,
                                        text="Fecha de publicación: ",
                                        justify="left",
                                        anchor="w",
                                        width=200,
                                        font=("Roboto", 18, "bold"),
                                        text_color="#F6FFF9")
            self.etiquetaFecha.grid(row=5, column=0, padx=10, pady=5)
            self.entradaFecha = CTkEntry(master=ventanaInsertar,
                                        font=("Roboto", 12, "bold"),
                                        width=200,
                                        placeholder_text="DD/MM/AAAA",
                                        placeholder_text_color="#B8B8B8")
            self.entradaFecha.grid(row=5, column=1, padx=10, pady=5)

            #ENTRADA EDITORIAL-------------------------------------------------------

            self.etiquetaEditorial = CTkLabel(master=ventanaInsertar,
                                        text="Editorial: ",
                                        justify="left",
                                        anchor="w",
                                        width=200,
                                        font=("Roboto", 18, "bold"),
                                        text_color="#F6FFF9")
            self.etiquetaEditorial.grid(row=6, column=0, padx=10, pady=5)
            self.entradaEditorial = CTkEntry(master=ventanaInsertar,
                                        font=("Roboto", 12, "bold"),
                                        width=200)
            self.entradaEditorial.grid(row=6, column=1, padx=10, pady=5)

            #ENTRADA ISBN-------------------------------------------------------

            self.etiquetaISBN = CTkLabel(master=ventanaInsertar,
                                        text="ISBN: ",
                                        justify="left",
                                        anchor="w",
                                        width=200,
                                        font=("Roboto", 18, "bold"),
                                        text_color="#F6FFF9")
            self.etiquetaISBN.grid(row=7, column=0, padx=10, pady=5)
            self.entradaISBN = CTkEntry(master=ventanaInsertar,
                                        font=("Roboto", 12, "bold"),
                                        width=200)
            self.entradaISBN.grid(row=7, column=1, padx=10, pady=5)

            #ENTRADA PORTADA-------------------------------------------------------

            self.etiquetaPortada = CTkLabel(master=ventanaInsertar,
                                            text="Portada: ",
                                            justify="left",
                                            anchor="w",
                                            width=200,
                                            font=("Roboto", 18, "bold"),
                                            text_color="#F6FFF9")
            self.etiquetaPortada.grid(row=8, column=0, padx=10, pady=5)
            self.entradaPortada = CTkEntry(master=ventanaInsertar,
                                            textvariable=self.imagenPath,
                                            state="readonly",
                                            font=("Roboto", 12, "bold"),
                                            width=200)
            self.entradaPortada.grid(row=8, column=2, padx=10, pady=5)

            #BOTÓN DE EXPLORACIÓN----------------------------------------------------
            
            self.botonExplorador = CTkButton(master=ventanaInsertar,text="Abrir explorador",
                                            command=lambda: [self.abrirExplorador(),posicionarVentana()],
                                            width=200,
                                            text_color="#F6FFF9",
                                            font=("Roboto", 18, "bold"),
                                            fg_color="#42594B",
                                            hover_color="#2E324C",
                                            border_color="#4C2E41",
                                            border_width=3)
            self.botonExplorador.grid(row=8, column=1, padx=10, pady=5)

            #ENTRADA SINOPSIS-------------------------------------------------------

            self.etiquetaSinopsis = CTkLabel(master=ventanaInsertar,
                                        text="Sinopsis: ",
                                        justify="left",
                                        anchor="nw",
                                        width=200,
                                        height=250,
                                        font=("Roboto", 18, "bold"),
                                        text_color="#F6FFF9")
            self.etiquetaSinopsis.grid(row=9, column=0, padx=10, pady=5)
            self.entradaSinopsis = CTkTextbox(master=ventanaInsertar,
                                        font=("Roboto", 12, "bold"),
                                        scrollbar_button_color="#42594B",
                                        width=430,
                                        height=250)
            self.entradaSinopsis.grid(row=9, column=1, columnspan=2, padx=10, pady=5)

            #BOTÓN AGREGAR------------------------------------------------------------

            self.botonAgregar = CTkButton(master=ventanaInsertar,
                                            text="Añadir libro",
                                            command=lambda: [self.guardarInfo(),self.limpiarCampos(),posicionarVentana()],
                                            text_color="#F6FFF9",
                                            height=40,
                                            width=210,
                                            font=("Roboto", 18, "bold"),
                                            corner_radius=32,
                                            fg_color="#42594B",
                                            hover_color="#2E324C",
                                            border_color="#4C2E41",
                                            border_width=3)
            self.botonAgregar.grid(row=10, column=1, padx=10, pady=5)

            #BOTÓN CANCELAR-----------------------------------------------------------

            self.botonCancelar = CTkButton(master=ventanaInsertar,text="Cancelar",
                                            command=cancelarVentanaInsertar,
                                            text_color="#F6FFF9",
                                            height=40,
                                            width=210,
                                            font=("Roboto", 18, "bold"),
                                            corner_radius=32,
                                            fg_color="#42594B",
                                            hover_color="#2E324C",
                                            border_color="#4C2E41",
                                            border_width=3)
            self.botonCancelar.grid(row=10, column=2, padx=10, pady=5)

    # Función para abrir un explorador de archivos y seleccionar una imagen
    def abrirExplorador(self):
        
        rutaImagen = filedialog.askopenfilename(initialdir=os.getcwd(), title="Seleccionar imagen", filetypes=[("Archivos de imagen", "*.jpg;*.jpeg;*.png")])
        if rutaImagen:
            self.imagenPath.set(rutaImagen)

    # Función para limpiar los campos de entrada
    def limpiarCampos(self):
        self.entradaTitulo.delete(0, END)
        self.entradaAutor.delete(0, END)
        self.imagenPath.set("")
        self.entradaGenero.delete(0, END)
        self.entradaPaginas.delete(0, END)
        self.entradaFecha.delete(0, END)
        self.entradaEditorial.delete(0, END)
        self.entradaISBN.delete(0, END)
        self.entradaSinopsis.delete("1.0", END)

    #Función para guardar libro:
    def guardarInfo(self):
        titulo = self.entradaTitulo.get()
        autor = self.entradaAutor.get()
        genero = self.entradaGenero.get()
        paginas = self.entradaPaginas.get()
        fecha = self.entradaFecha.get()
        editorial = self.entradaEditorial.get()
        isbn = self.entradaISBN.get()
        sinopsis = self.entradaSinopsis.get("1.0", END)

        #Si no se introducen valores, cargar valores por defecto
        if self.entradaTitulo.get() == "":
            titulo = "Título no encontrado"
        if self.entradaAutor.get() == "":
            autor = "Autor no encontrado"
        if self.entradaGenero.get() == "":
            genero = "Género no encontrado"
        if self.entradaPaginas.get() == "":
            paginas = "Número de páginas no encontrado"
        if self.entradaFecha.get() == "":
            fecha = "No encontrada"
        if self.entradaEditorial.get() == "":
            editorial = "Editorial no encontrada"
        if self.entradaISBN.get() == "":
            isbn = "Número de ISBN no encontrado"
        if self.entradaSinopsis.get("1.0", END) == "":
            sinopsis = "Sinopsis no encontrada"

        # Si no se carga imagen carga una por defecto
        if self.imagenPath.get() == "":
            rutaImagenPorDefecto = 'img/portadaPorDefecto.png'
            self.imagenPath.set(rutaImagenPorDefecto)

        # Leer la imagen seleccionada
        with open(self.imagenPath.get(), 'rb') as f:
            datosImagen = f.read()

        self.controlador.guardarInfo(titulo, autor, genero, paginas, fecha, editorial, isbn, datosImagen, sinopsis)
        self.limpiarCampos()
        messagebox.showinfo("Añadir Libro", "El libro " + titulo +" ha sido añadido a la biblioteca")
        self.vista.actualizarMarcoLibros()
        
