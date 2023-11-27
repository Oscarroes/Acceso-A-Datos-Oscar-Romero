import subprocess

class Oscardb:

    def __init__(self,basededatos):
        self.basededatos =basededatos
    
    def insert(self,coleccion,documento,contenido):
        
        self.operacion = "insert"
        self.coleccion = coleccion
        self.documento = documento
        self.contenido = contenido

        comando = '"C:\\Users\\oscar\\OneDrive\\Escritorio\\IMF\\Segundo\\ACCESO A DATOS\\GIT\\Acceso-A-Datos-Oscar-Romero\\CONECTOR-CON-PYTHON-5\\oscardb.exe" '+self.operacion+' '+self.basededatos+' '+self.coleccion+' '+self.documento+' "'+self.contenido+'"'
        resultado = subprocess.run(comando,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
        if resultado.returncode == 0:
            print("Registro insertado")
            return("ok")
        else:
            return("ko")
    
    def select(self,coleccion,documento):
        self.operacion = "select"
        self.coleccion = coleccion
        self.documento = documento

        comando = '"C:\\Users\\oscar\\OneDrive\\Escritorio\\IMF\\Segundo\\ACCESO A DATOS\\GIT\\Acceso-A-Datos-Oscar-Romero\\CONECTOR-CON-PYTHON-5\\oscardb.exe" '+self.operacion+' '+self.basededatos+' '+self.coleccion+' '+self.documento+'"'
        resultado = subprocess.run(comando,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
        if resultado.returncode == 0:
            print(resultado.stdout)
            return("ok")
        else:
            return("ko")

    def delete(self,coleccion,documento):

        self.operacion = "delete"
        self.coleccion = coleccion
        self.documento = documento

        comando = '"C:\\Users\\oscar\\OneDrive\\Escritorio\\IMF\\Segundo\\ACCESO A DATOS\\GIT\\Acceso-A-Datos-Oscar-Romero\\CONECTOR-CON-PYTHON-5\\oscardb.exe" '+self.operacion+' '+self.basededatos+' '+self.coleccion+' '+self.documento+'"'
        resultado = subprocess.run(comando,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
        if resultado.returncode == 0:
            print("Registro eliminado")
            return("ok")
        else:
            return("ko")
        
    def update(self,coleccion,documento,contenidoOld,contenidoNew):

        self.operacion = "update"
        self.coleccion = coleccion
        self.documento = documento
        self.contenidoOld = contenidoOld
        self.contenidoNew = contenidoNew

        comando = '"C:\\Users\\oscar\\OneDrive\\Escritorio\\IMF\\Segundo\\ACCESO A DATOS\\GIT\\Acceso-A-Datos-Oscar-Romero\\CONECTOR-CON-PYTHON-5\\oscardb.exe" '+self.operacion+' '+self.basededatos+' '+self.coleccion+' '+self.documento+' "'+self.contenidoOld+'" "'+self.contenidoNew+'"'
        resultado = subprocess.run(comando,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
        if resultado.returncode == 0:
            print("Registro modificado")
            return("ok")
        else:
            return("ko")