import sys
from oscardb_conector import Oscardb

basedatos = input("Escribe la base de datos con la que quieres trabajar:")
conexion = Oscardb(basedatos)
def menu():
    #Menu inicial:
    print("Escoge una operación:")
    print("1.- Introduce un nuevo registro")
    print("2.- Lista los registros")
    print("3.- Elimina un registro")
    print("4.- Modifica un registro")
    print("5.- Salir")

    operacion = int(input())
    if operacion == 1:
        coleccion = input("Introduce el nombre de la colección: ")
        documento = input("Introduce el nombre del documento: ")
        contenido = input("Introduce el contenido: ")
        conexion.insert(coleccion,documento,contenido)
        print("-------------------------------")
        
    elif operacion == 2:
        coleccion = input("Introduce el nombre de la colección: ")
        documento = input("Introduce el nombre del documento a consultar: ")
        conexion.select(coleccion,documento)
        print("-------------------------------")
    elif operacion == 3:
        coleccion = input("Introduce el nombre de la colección: ")
        documento = input("Introduce el nombre del documento a eliminar: ")
        conexion.delete(coleccion,documento)
        print("-------------------------------")
    elif operacion == 4:
        coleccion = input("Introduce el nombre de la colección: ")
        documento = input("Introduce el nombre del documento: ")
        contenidoOld = input("Introduce el contenido que quieres modificar: ")
        contenidoNew = input("Introduce el contenido actualizado: ")
        conexion.update(coleccion,documento,contenidoOld,contenidoNew)
        print("-------------------------------")
    elif operacion == 5:
        sys.exit()

    menu()

menu()