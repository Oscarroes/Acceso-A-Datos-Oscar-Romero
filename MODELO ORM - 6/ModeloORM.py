import tkinter as tk
from tkinter import ttk
import random
import math
import json

personas = []

class Persona:
    #CONSTRUCTOR DE LAS ENTIDADES PERSONA
    def __init__(self):
        self.posx = random.randint(0,1024)
        self.posy = random.randint(0,600)
        self.radio = 30
        self.direccion = random.randint(0,360)
        self.color = ""
        self.velocidad = 50
        self.entidad = ""
    #DIBUJA LAS ENTIDADES = LES DAMOS COLOR Y UNA COORDENADA DE POSICIÓN
    def dibuja(self):
        self.entidad = lienzo.create_oval(
            self.posx-self.radio/2,
            self.posy-self.radio/2,
            self.posx+self.radio/2,
            self.posy+self.radio/2,
            fill=self.color)
    #DEFINE EL MOVIMIENTO DE LAS ENTIDADES Y LOS LÍMITES DEL CANVAS PARA QUE NO ESCAPEN
    def mueve(self):
        self.colisiona()
        self.cambiaColor()
        lienzo.move(self.entidad,
                    math.cos(self.direccion),
                    math.sin(self.direccion))
        self.posx += math.cos(self.direccion)
        self.posy += math.sin(self.direccion)
    def colisiona(self):
        if self.posx <0 or self.posx > 1024 or self.posy < 0 or self.posy > 600:
            self.direccion += math.pi
    #CAMBIA EL COLOR DE LAS ENTIDADES DEPENDIENDO DEL CUADRANTE CARTESIANO QUE OCUPEN
    def cambiaColor(self):
        if self.posx < 512 and self.posy > 300:
            self.color = "blue"
            lienzo.itemconfig(self.entidad, fill=self.color)
        elif self.posx > 512 and self.posy > 300:
            self.color = "green"
            lienzo.itemconfig(self.entidad, fill=self.color)
        elif self.posx < 512 and self.posy < 300:
            self.color = "black"
            lienzo.itemconfig(self.entidad, fill=self.color)
        elif self.posx > 512 and self.posy < 300:
            self.color = "red"
            lienzo.itemconfig(self.entidad, fill=self.color)
    #CAMBIA LA VELOCIDAD DE LAS ENTIDADES SEGÚN SELECCINEMOS
    def cambiaVelocidad(event):
        if ajustaVelocidad.get() == 'Muy lento':
            for persona in personas:
                persona.velocidad = 400
        elif ajustaVelocidad.get() == 'Lento':
            for persona in personas:
                persona.velocidad = 125
        elif ajustaVelocidad.get() == 'Medio':
            for persona in personas:
                persona.velocidad = 50
        elif ajustaVelocidad.get() == 'Rapido':
            for persona in personas:
                persona.velocidad = 20
        elif ajustaVelocidad.get() == 'Muy rapido':
            for persona in personas:
                persona.velocidad = 5
    #GUARDA EL ESTADO DE LAS ENTIDADES
    def guardarPersonas():
        print("Guardo a los jugadores")
        cadena = json.dumps([vars(persona) for persona in personas])
        print(cadena)
        archivo = open("jugadores.json",'w')
        archivo.write(cadena)
        archivo.close()

        
#CREAMOS LA VENTANA
raiz = tk.Tk()
raiz.geometry("1024x600")
raiz.title("Modelo ORM")

#EN LA VENTANA CREAMOS UN LIENZO
lienzo = tk.Canvas(raiz,width=1024,height=600)
lienzo.pack()

#COMBOBOX PARA AJUSTAR LA VELOCIDAD
ajustaVelocidad = ttk.Combobox(raiz,values=['Muy lento','Lento','Medio','Rapido','Muy rapido'])
ajustaVelocidad.pack(padx=10,pady=10)
ajustaVelocidad.bind('<<ComboboxSelected>>', Persona.cambiaVelocidad)

#BOTÓN DE GUARDAR
boton = ttk.Button(raiz,text="Guardar", command=Persona.guardarPersonas)
boton.pack(padx=10,pady=10)

#CARGAR PERSONAS DESDE EL DISCO DURO:
try:
    carga = open("jugadores.json",'r')
    cargado = carga.read()
    cargadoLista = json.loads(cargado)
    for elemento in cargadoLista:
        persona = Persona()
        persona.__dict__.update(elemento)
        personas.append(persona)
except:
    print("No hay archivo guardado")

#EN LA COLECCION INTRODUZCO INSTANCIAS DE PERSONAS EN EL CASO QUE NO EXISTAN
if len (personas) == 0:
    numeroPersonas = 20
    for i in range(0,numeroPersonas):
        personas.append(Persona())

#PARA CADA PERSONA DE LA COLECCIÓN VAMOS A DIBUJARLA:
for persona in personas:
    persona.dibuja()

#CREAMOS UN BUCLE REPETITIVO Y PARA CADA PERSONA EN LA COLECCION LA MUEVO
def bucle():
    for persona in personas:
        persona.mueve()
    tiempo = persona.velocidad
    raiz.after(tiempo,bucle)

#EJECUCUION DEL BUCLE
bucle()

raiz.mainloop()