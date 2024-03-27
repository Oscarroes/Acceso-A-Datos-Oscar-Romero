import tkinter as tk
from customtkinter import *
from tkinter import messagebox
from PIL import Image
import os

class VistaFicha:

    def __init__(self, ventana, controlador, vista):
        self.ventana = ventana
        self.controlador = controlador
        self.vista = vista
        self.ventanaVerFicha = None
        self.ventanaModificar = None

        self.imagenPath = tk.StringVar()

    def abrirVentanaVerFicha(self, libro):
        
        self.ventanaVerFicha = tk.Toplevel(self.ventana)
        self.ventanaVerFicha.geometry("896x896")
        self.ventanaVerFicha.config(bg="#2E4C39")
        self.ventanaVerFicha.title('Ficha del libro')
        self.ventanaVerFicha.iconbitmap('img/iconoLibros.ico')
        self.ventanaVerFicha.lift()

        def cancelarVentanaVerFicha():
            self.ventanaVerFicha.destroy()
        
        def posicionarVentana():
            self.ventanaVerFicha.lift()

        imagenPortada = self.controlador.obtenerPortada(libro["portada"])

        imagen = tk.PhotoImage(data=imagenPortada)

        lienzoPortada = tk.Canvas(master=self.ventanaVerFicha, width=200, height=310)
        lienzoPortada.create_image(0, 0, anchor=tk.NW, image=imagen)
        lienzoPortada.grid(row=0, column=0, rowspan=6, padx=10, pady=10)

        lienzoPortada.imagen = imagen

        etiquetaTitulo = CTkLabel(master=self.ventanaVerFicha,
                                    text="Título: " + libro["titulo"],
                                    justify="left",
                                    anchor="w",
                                    width=400,
                                    font=("Roboto", 18, "bold"),
                                    text_color="#F6FFF9")
        etiquetaTitulo.grid(row=0, column=1, padx=10, pady=5)
        

        etiquetaAutor = CTkLabel(master=self.ventanaVerFicha,
                                    text="Autor: " + libro["autor"],
                                    justify="left",
                                    anchor="w",
                                    width=400,
                                    font=("Roboto", 18, "bold"),
                                    text_color="#F6FFF9")
        etiquetaAutor.grid(row=1, column=1, padx=10, pady=5)

        etiquetaGenero = CTkLabel(master=self.ventanaVerFicha,
                                    text="Género: " + libro["genero"],
                                    justify="left",
                                    anchor="w",
                                    width=400,
                                    font=("Roboto", 18, "bold"),
                                    text_color="#F6FFF9")
        etiquetaGenero.grid(row=2, column=1, padx=10, pady=5)

        etiquetaPaginas = CTkLabel(master=self.ventanaVerFicha,
                                    text="Páginas: " + libro["paginas"],
                                    justify="left",
                                    anchor="w",
                                    width=400,
                                    font=("Roboto", 18, "bold"),
                                    text_color="#F6FFF9")
        etiquetaPaginas.grid(row=3, column=1, padx=10, pady=5)

        etiquetaFecha = CTkLabel(master=self.ventanaVerFicha,
                                    text="Fecha de publicación: " + libro["fecha de publicacion"],
                                    justify="left",
                                    anchor="w",
                                    width=400,
                                    font=("Roboto", 18, "bold"),
                                    text_color="#F6FFF9")
        etiquetaFecha.grid(row=4, column=1, columnspan=2, padx=10, pady=5)

        etiquetaEditorial = CTkLabel(master=self.ventanaVerFicha,
                                    text="Editorial: " + libro["editorial"],
                                    justify="left",
                                    anchor="w",
                                    width=400,
                                    font=("Roboto", 18, "bold"),
                                    text_color="#F6FFF9")
        etiquetaEditorial.grid(row=5, column=1, padx=10, pady=5)

        etiquetaISBN = CTkLabel(master=self.ventanaVerFicha,
                                    text="ISBN: " + libro["isbn"],
                                    justify="left",
                                    anchor="w",
                                    width=400,
                                    font=("Roboto", 18, "bold"),
                                    text_color="#F6FFF9")
        etiquetaISBN.grid(row=6, column=1, padx=10, pady=5)

        marcoSinopsis = CTkScrollableFrame(master=self.ventanaVerFicha,width=600, height=300, fg_color="#F6FFF9", border_color="#4C2E41", border_width=3,
                                orientation="horizontal", scrollbar_button_color="#42594B")
        marcoSinopsis.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

        etiquetaSinopsis = CTkLabel(master=marcoSinopsis,
                                    text="Sinopsis: \n \n" + libro["sinopsis"],
                                    justify="left",
                                    anchor="nw",
                                    font=("Roboto", 12, "bold"),
                                    text_color="#000000")
        etiquetaSinopsis.grid(row=0, column=0, padx=10, pady=5)

        #BOTÓN MODIFICAR------------------------------------------------------------

        self.botonModificar = CTkButton(master=self.ventanaVerFicha,
                                        text="Modificar libro",
                                        command=lambda: self.abrirVentanaModificar(libro),
                                        text_color="#F6FFF9",
                                        height=40,
                                        width=210,
                                        font=("Roboto", 18, "bold"),
                                        corner_radius=32,
                                        fg_color="#42594B",
                                        hover_color="#2E324C",
                                        border_color="#4C2E41",
                                        border_width=3)
        self.botonModificar.grid(row=8, column=0, padx=10, pady=10)

        #BOTÓN CANCELAR-----------------------------------------------------------

        self.botonCancelar = CTkButton(master=self.ventanaVerFicha,text="Cancelar",
                                        command=cancelarVentanaVerFicha,
                                        text_color="#F6FFF9",
                                        height=40,
                                        width=210,
                                        font=("Roboto", 18, "bold"),
                                        corner_radius=32,
                                        fg_color="#42594B",
                                        hover_color="#2E324C",
                                        border_color="#4C2E41",
                                        border_width=3)
        self.botonCancelar.grid(row=8, column=1, padx=10, pady=10)

    #VISTA MODIFICAR -----------------------------------------------------------
  
    def abrirVentanaModificar(self,libro):
        
        self.ventanaModificar = tk.Toplevel(self.ventanaVerFicha)
        self.ventanaModificar.geometry("896x896")
        self.ventanaModificar.config(bg="#2E4C39")
        self.ventanaModificar.title('Modifica el libro')
        self.ventanaModificar.iconbitmap('img/iconoLibros.ico')
        self.ventanaModificar.lift()
        

        def posicionarVentana():
            self.ventanaModificar.lift()
        
        def cancelarVentanaModificar():
            self.ventanaModificar.destroy()

        self.frameSeparador = CTkFrame(master=self.ventanaModificar, fg_color="#2E4C39", height=10)
        self.frameSeparador.grid(row=0, column=0, padx=10, pady=5)

        #ENTRADA TÍTULO--------------------------------------------------
        self.etiquetaTitulo = CTkLabel(master=self.ventanaModificar,
                                    text="Nuevo título: ",
                                    justify="left",
                                    anchor="w",
                                    width=200,
                                    font=("Roboto", 18, "bold"),
                                    text_color="#F6FFF9")
        self.etiquetaTitulo.grid(row=1, column=0, padx=10, pady=5)
        self.entradaTitulo = CTkEntry(master=self.ventanaModificar,
                                    font=("Roboto", 12, "bold"),
                                    width=200)
        self.entradaTitulo.grid(row=1, column=1, padx=10, pady=5)

        #ENTRADA AUTOR-------------------------------------------------------
        self.etiquetaAutor = CTkLabel(master=self.ventanaModificar,
                                    text="Nuevo Autor: ",
                                    justify="left",
                                    anchor="w",
                                    width=200,
                                    font=("Roboto", 18, "bold"),
                                    text_color="#F6FFF9")
        self.etiquetaAutor.grid(row=2, column=0, padx=10, pady=5)
        self.entradaAutor = CTkEntry(master=self.ventanaModificar,
                                    font=("Roboto", 12, "bold"),
                                    width=200)
        self.entradaAutor.grid(row=2, column=1, padx=10, pady=0)

        #ENTRADA GÉNERO-------------------------------------------------------

        self.etiquetaGenero = CTkLabel(master=self.ventanaModificar,
                                    text="Nuevo género: ",
                                    justify="left",
                                    anchor="w",
                                    width=200,
                                    font=("Roboto", 18, "bold"),
                                    text_color="#F6FFF9")
        self.etiquetaGenero.grid(row=3, column=0, padx=10, pady=5)
        self.entradaGenero = CTkEntry(master=self.ventanaModificar,
                                    font=("Roboto", 12, "bold"),
                                    width=200)
        self.entradaGenero.grid(row=3, column=1, padx=10, pady=5)

        #ENTRADA PÁGINAS-------------------------------------------------------

        self.etiquetaPaginas = CTkLabel(master=self.ventanaModificar,
                                    text="Nuevo nº de páginas: ",
                                    justify="left",
                                    anchor="w",
                                    width=200,
                                    font=("Roboto", 18, "bold"),
                                    text_color="#F6FFF9")
        self.etiquetaPaginas.grid(row=4, column=0, padx=10, pady=5)
        self.entradaPaginas = CTkEntry(master=self.ventanaModificar,
                                    font=("Roboto", 12, "bold"),
                                    width=200)
        self.entradaPaginas.grid(row=4, column=1, padx=10, pady=5)

        #ENTRADA FECHA DE PUBLICACIÓN-------------------------------------------------------

        self.etiquetaFecha = CTkLabel(master=self.ventanaModificar,
                                    text="Nueva fecha: ",
                                    justify="left",
                                    anchor="w",
                                    width=200,
                                    font=("Roboto", 18, "bold"),
                                    text_color="#F6FFF9")
        self.etiquetaFecha.grid(row=5, column=0, padx=10, pady=5)
        self.entradaFecha = CTkEntry(master=self.ventanaModificar,
                                    font=("Roboto", 12, "bold"),
                                    width=200,
                                    placeholder_text="DD/MM/AAAA",
                                    placeholder_text_color="#B8B8B8")
        self.entradaFecha.grid(row=5, column=1, padx=10, pady=5)

        #ENTRADA EDITORIAL-------------------------------------------------------

        self.etiquetaEditorial = CTkLabel(master=self.ventanaModificar,
                                    text="Nueva editorial: ",
                                    justify="left",
                                    anchor="w",
                                    width=200,
                                    font=("Roboto", 18, "bold"),
                                    text_color="#F6FFF9")
        self.etiquetaEditorial.grid(row=6, column=0, padx=10, pady=5)
        self.entradaEditorial = CTkEntry(master=self.ventanaModificar,
                                    font=("Roboto", 12, "bold"),
                                    width=200)
        self.entradaEditorial.grid(row=6, column=1, padx=10, pady=5)

        #ENTRADA ISBN-------------------------------------------------------

        self.etiquetaISBN = CTkLabel(master=self.ventanaModificar,
                                    text="Nuevo ISBN: ",
                                    justify="left",
                                    anchor="w",
                                    width=200,
                                    font=("Roboto", 18, "bold"),
                                    text_color="#F6FFF9")
        self.etiquetaISBN.grid(row=7, column=0, padx=10, pady=5)
        self.entradaISBN = CTkEntry(master=self.ventanaModificar,
                                    font=("Roboto", 12, "bold"),
                                    width=200)
        self.entradaISBN.grid(row=7, column=1, padx=10, pady=5)

        #ENTRADA PORTADA-------------------------------------------------------

        self.etiquetaPortada = CTkLabel(master=self.ventanaModificar,
                                        text="Nueva Portada: ",
                                        justify="left",
                                        anchor="w",
                                        width=200,
                                        font=("Roboto", 18, "bold"),
                                        text_color="#F6FFF9")
        self.etiquetaPortada.grid(row=8, column=0, padx=10, pady=5)
        self.entradaPortada = CTkEntry(master=self.ventanaModificar,
                                        textvariable=self.imagenPath,
                                        state="readonly",
                                        font=("Roboto", 12, "bold"),
                                        width=200)
        self.entradaPortada.grid(row=8, column=2, padx=10, pady=5)

        #BOTÓN DE EXPLORACIÓN--------------------------------------------------

        self.botonExplorador = CTkButton(master=self.ventanaModificar,text="Abrir explorador",
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

        self.etiquetaSinopsis = CTkLabel(master=self.ventanaModificar,
                                    text="Nueva sinopsis: ",
                                    justify="left",
                                    anchor="nw",
                                    width=200,
                                    height=250,
                                    font=("Roboto", 18, "bold"),
                                    text_color="#F6FFF9")
        self.etiquetaSinopsis.grid(row=9, column=0, padx=10, pady=5)
        self.entradaSinopsis = CTkTextbox(master=self.ventanaModificar,
                                    font=("Roboto", 12, "bold"),
                                    scrollbar_button_color="#42594B",
                                    width=430,
                                    height=250)
        self.entradaSinopsis.grid(row=9, column=1, columnspan=2, padx=10, pady=5)

        #BOTÓN MODIFICAR LIBRO------------------------------------------------------------

        self.botonModificaLibro = CTkButton(master=self.ventanaModificar,
                                        text="Modificar libro",
                                        command=lambda: self.modificarLibro(libro),
                                        text_color="#F6FFF9",
                                        height=40,
                                        width=210,
                                        font=("Roboto", 18, "bold"),
                                        corner_radius=32,
                                        fg_color="#42594B",
                                        hover_color="#2E324C",
                                        border_color="#4C2E41",
                                        border_width=3)
        self.botonModificaLibro.grid(row=10, column=1, padx=10, pady=5)

        #BOTÓN CANCELAR-----------------------------------------------------------

        self.botonCancelar = CTkButton(master=self.ventanaModificar,text="Cancelar",
                                        command=cancelarVentanaModificar,
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

    def modificarLibro(self, libro):

        # Verificar si se ha seleccionado una nueva portada
        if not self.imagenPath.get():
            messagebox.showerror("Error", "El campo nueva portada es obligatorio.")
            self.ventanaModificar.lift()
            return

        titulo = self.entradaTitulo.get()
        autor = self.entradaAutor.get()
        genero = self.entradaGenero.get()
        paginas = self.entradaPaginas.get()
        fecha = self.entradaFecha.get()
        editorial = self.entradaEditorial.get()
        isbn = self.entradaISBN.get()
        sinopsis = self.entradaSinopsis.get("1.0", END)

        if self.imagenPath.get():
            with open(self.imagenPath.get(), 'rb') as f:
                datosImagen = f.read()

        else:
            # Si no se ha seleccionado una nueva imagen, se mantiene la imagen original
            datosImagen = libro["portada"]

        # Si los campos están vacíos se cargan los originales
        if not titulo:
            titulo = libro["titulo"]
        if not autor:
            autor = libro["autor"]
        if not genero:
            genero = libro["genero"]
        if not paginas:
            paginas = libro["paginas"]
        if not fecha:
            fecha = libro["fecha de publicacion"]
        if not editorial:
            editorial = libro["editorial"]
        if not isbn:
            isbn = libro["isbn"]
        if not sinopsis.strip():
            sinopsis = libro["sinopsis"]

        # Modificar el libro
        self.controlador.modificarLibro(libro, titulo, autor, genero, paginas, fecha, editorial, isbn, datosImagen, sinopsis)
        messagebox.showinfo("Modificar Libro", "El libro " + titulo +" ha sido modificado")
        self.ventanaModificar.destroy()
        self.ventanaVerFicha.destroy()
        self.vista.actualizarMarcoLibros()

    


