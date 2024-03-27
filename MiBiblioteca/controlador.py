class Controlador:
    def __init__(self, modelo):
        self.modelo = modelo
        self.fs = modelo.fs

    def consultarTodo(self):
        libros = self.modelo.consultarDatos()
        return libros

    def traerLibro(self, titulo):
        libro = self.modelo.traerLibroPorTitulo(titulo)
        return libro
    
    def traerLibroAutor(self, autor):
        libro = self.modelo.traerLibroPorAutor(autor)
        return libro
    
    def traerLibroGenero(self, genero):
        libro = self.modelo.traerLibroPorGenero(genero)
        return libro
        
    def obtenerPortada(self, idPortada):
        return self.modelo.obtenerPortada(idPortada)

    def guardarInfo(self, titulo, autor, genero, paginas, fecha, editorial, isbn, datosImagen, sinopsis):
        # Guardar la imagen en GridFS
        idPortada = self.fs.put(datosImagen, filename='portada.png')
        self.modelo.guardarLibro(titulo, autor,genero, paginas, fecha, editorial, isbn, idPortada, sinopsis)
        print("libro guardado correctamente")
    
    def eliminarLibro(self, idLibro):
        self.modelo.eliminarLibro(idLibro)

    def modificarLibro(self, libro, titulo, autor, genero, paginas, fecha, editorial, isbn, datosImagen, sinopsis):
        idPortada = self.fs.put(datosImagen, filename='portada.png')
        self.modelo.modificarLibro(libro["_id"], titulo, autor, genero, paginas, fecha, editorial, isbn, idPortada, sinopsis)
