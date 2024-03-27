import pymongo
import gridfs

class Modelo:
    def __init__(self):
        self.cliente = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.cliente["miBiblioteca"]
        self.coleccion = self.db["libros"]

        # Inicializar GridFS para almacenar la imagen en modo binario
        self.fs = gridfs.GridFS(self.db)

    def consultarDatos(self):
        libros = self.coleccion.find()

        return libros
    
    def traerLibroPorTitulo(self,titulo):
        libro = self.coleccion.find({"titulo": {"$regex": f".*{titulo}.*", "$options": "i"}})
        return list(libro)
    
    def traerLibroPorAutor(self,autor):
        libro = self.coleccion.find({"autor": {"$regex": f".*{autor}.*", "$options": "i"}})
        return list(libro)
    
    def traerLibroPorGenero(self,genero):
        libro = self.coleccion.find({"genero": {"$regex": f".*{genero}.*", "$options": "i"}})
        return list(libro)
    
    def obtenerPortada(self, idPortada):
        try:
            # Recuperar los datos de la imagen desde GridFS
            datosImagen = self.fs.get(idPortada).read()
            return datosImagen
        except Exception as e:
            print("Error al obtener la portada:", e)
            return None
    
    def guardarLibro(self, titulo, autor, genero, paginas, fecha, editorial, isbn, idPortada, sinopsis):

        libro = {
            "titulo":titulo,
            "autor":autor,
            "genero":genero,
            "paginas":paginas,
            "fecha de publicacion":fecha,
            "editorial":editorial,
            "isbn":isbn,
            "portada":idPortada,
            "sinopsis":sinopsis
            }
        self.coleccion.insert_one(libro)

    def eliminarLibro(self,idLibro):
        self.coleccion.delete_one({"_id": idLibro})

    def modificarLibro(self, idLibro, titulo, autor, genero, paginas, fecha, editorial, isbn, idPortada, sinopsis):
        libroActualizado = {
            "titulo": titulo,
            "autor": autor,
            "genero": genero,
            "paginas": paginas,
            "fecha de publicacion": fecha,
            "editorial": editorial,
            "isbn": isbn,
            "portada": idPortada,
            "sinopsis": sinopsis
        }
        self.coleccion.update_one({"_id": idLibro}, {"$set": libroActualizado})
        