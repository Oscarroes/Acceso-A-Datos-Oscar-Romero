import tkinter as tk
from tkinter import ttk
import random
import math
import sqlite3

#INICIALIZAMOS LA LISTA DE ENTIDADES
personas = []

class Persona:
    #CONSTRUCTOR DE LAS ENTIDADES PERSONA
    def __init__(self):
        self.posx = random.randint(0,1024)
        self.posy = random.randint(0,600)
        self.radio = 30
        self.direccion = random.randint(0,360)
        self.velocidad = 10
        self.color = ""
        self.entidad = ""
        #A medida que el personaje vaya avanzando va a ir perdiendo energía y descanso, pero ganando experiencia
        self.energia = 100
        self.descanso = 100
        self.experiencia = 0
        self.entidadEnergia = ""
        self.entidadDescanso = ""
        self.entidadExperiencia = ""
        self.nivel = 1
        self.entidadNivel = ""
    #DIBUJA LAS ENTIDADES = LES DAMOS COLOR Y UNA COORDENADA DE POSICIÓN
    def dibuja(self):
        self.entidad = lienzo.create_oval(
            self.posx-self.radio/2,
            self.posy-self.radio/2,
            self.posx+self.radio/2,
            self.posy+self.radio/2,
            fill=self.color)
        #Vamos a dibujarles las barras de energía, descanso y experiencia
        self.entidadEnergia = lienzo.create_rectangle(
            self.posx-self.radio/2,
            self.posy-self.radio/2-14,
            self.posx+self.radio/2,
            self.posy-self.radio/2-8,
            fill="green"
            )
        self.entidadDescanso = lienzo.create_rectangle(
            self.posx-self.radio/2,
            self.posy-self.radio/2-22,
            self.posx+self.radio/2,
            self.posy-self.radio/2-16,
            fill="red"
            )

        self.entidadExperiencia = lienzo.create_rectangle(
            self.posx+self.radio/2 + 8,
            self.posy-self.radio/2,
            self.posx+self.radio/2 + 14,
            self.posy+self.radio/2,
            fill="yellow"
            )
        # Texto de nivel
        self.entidadNivel = lienzo.create_text(
            self.posx + self.radio / 2 + 11,
            self.posy,
            text=str(round(self.nivel)),
            fill="black"
        )
    #DEFINE EL MOVIMIENTO DE LAS ENTIDADES Y LOS LÍMITES DEL CANVAS PARA QUE NO ESCAPEN
    def mueve(self):
        #Al moverse van a ir perdiendo energía y descanso, pero ganando experiencia:
        #Recuperan la energía y el descanso en la zona verde
        if self.energia > 0:
            self.energia -= 0.075
            if self.posx < 512 and self.posy > 300:
                self.energia = 100

        if self.descanso > 0:
            self.descanso -= 0.05
            if self.posx < 512 and self.posy > 300:
                self.descanso = 100

        #Ganan más experiencia en la zona roja y no la ganan en la verde
        self.experiencia += 0.001
        if self.posx > 512 and self.posy < 300:
            self.experiencia += 0.002
        if self.posx < 512 and self.posy > 300:
            self.experiencia += 0

        #SI LA EXPERIENCIA ES MAYOR QUE 2 -> SUBEN DE NIVEL
        if self.experiencia > 2:
            self.nivel +=1
            self.experiencia = 0
            # Actualizar el texto del nivel después de aumentar
            lienzo.itemconfig(self.entidadNivel, text=str(round(self.nivel)))
        
        self.colisiona()
        self.cambiaColor()
        lienzo.move(self.entidad,
                    math.cos(self.direccion),
                    math.sin(self.direccion))
        #Las barras se van a mover con coordenadas referenciadas a la posición:
        anchuraDescanso = (self.descanso/100)*self.radio  
        anchuraEnergia = (self.energia/100)*self.radio
        anchuraExperiencia = (self.experiencia-1)*self.radio

        lienzo.coords(self.entidadEnergia,
                    self.posx - self.radio/2,
                    self.posy - self.radio/2 - 14,
                    self.posx - self.radio/2 + anchuraEnergia,
                    self.posy - self.radio/2 - 8)
              
        lienzo.coords(self.entidadDescanso,
                    self.posx - self.radio/2,
                    self.posy - self.radio/2 - 22,
                    self.posx - self.radio/2 + anchuraDescanso,
                    self.posy - self.radio/2 - 16)
        
        lienzo.coords(self.entidadExperiencia,
                    self.posx + self.radio/2 + 8,
                    self.posy - self.radio/2 - anchuraExperiencia,
                    self.posx + self.radio/2 + 14,
                    self.posy + self.radio/2)
        # Actualizar las posiciones del texto de nivel
        lienzo.coords(self.entidadNivel,
                    self.posx + self.radio / 2 + 11,
                    self.posy)
        
        #Actualizar las posiciones de los jugadores:
        self.posx += math.cos(self.direccion)
        self.posy += math.sin(self.direccion)


    def colisiona(self):
        if self.posx <0 or self.posx > 1024 or self.posy < 0 or self.posy > 600:
            self.direccion += math.pi

    #CAMBIA EL COLOR DE LAS ENTIDADES DEPENDIENDO DEL CUADRANTE CARTESIANO QUE OCUPEN
    def cambiaColor(self):
        if self.posx < 512 and self.posy > 300:
            self.color = "green"
            lienzo.itemconfig(self.entidad, fill=self.color)
        elif self.posx > 512 and self.posy > 300:
            self.color = "blue"
            lienzo.itemconfig(self.entidad, fill=self.color)
        elif self.posx < 512 and self.posy < 300:
            self.color = "black"
            lienzo.itemconfig(self.entidad, fill=self.color)
        elif self.posx > 512 and self.posy < 300:
            self.color = "red"
            lienzo.itemconfig(self.entidad, fill=self.color)
    #CAMBIA LA VELOCIDAD DE LAS ENTIDADES SEGÚN SELECCIONEMOS
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
    #GUARDA EL ESTADO DE LAS ENTIDADES EN LA BASE DE DATOS SQL:
    def guardarPersonas():
        print("Guardo a los jugadores")
        #GUARDO LOS PERSONAJES EN SQL
        conexion = sqlite3.connect("jugadores.sqlite3")
        cursor = conexion.cursor()
        #TRUNCAR LA TABLA CADA VEZ QUE GUARDEMOS LOS JUGADORES
        cursor.execute('''
                       DELETE FROM jugadores
                       ''')
        conexion.commit()
        for persona in personas:
            cursor.execute('''
                            INSERT INTO jugadores VALUES(
                                NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?
                            )
                           ''', (
                               persona.posx,
                               persona.posy,
                               persona.radio,
                               persona.direccion,
                               persona.velocidad,
                               persona.color,
                               persona.entidad,
                               persona.energia,
                               persona.entidadEnergia,
                               persona.descanso,
                               persona.entidadDescanso,
                               persona.experiencia,
                               persona.entidadExperiencia,
                               persona.nivel,
                               persona.entidadNivel
                           ))
        conexion.commit()
        conexion.close()
     
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

#CARGAR EL ESTADO DE LOS JUGADORES DESDE LA BASE DE DATOS:
#PODEMOS TRAER A TODOS O SÓLO LAS CONDICIONES QUE NOS INTERESEN COMO WHERE color = "blue"
try:
    conexion = sqlite3.connect("jugadores.sqlite3")
    cursor = conexion.cursor()
    cursor.execute('''
                   SELECT * 
                   FROM jugadores
                   ''')
    while True:
        fila = cursor.fetchone()
        if fila is None:
            break
        
        persona = Persona()
        persona.posx = fila[1]
        persona.posy = fila[2]
        persona.radio = fila[3]
        persona.direccion = fila[4]
        persona.velocidad = fila[5]
        persona.color = fila[6]
        persona.entidad = fila[7]
        persona.energia = fila[8]
        persona.entidadEnergia = fila[9]
        persona.descanso = fila[10]
        persona.entidadDescanso = fila[11]
        persona.experiencia = fila[12]
        persona.entidadExperiencia = fila[13]
        persona.nivel = fila[14]
        persona.entidadNivel = fila[15]
        personas.append(persona)
    conexion.close()
except:
    print("error al cargar la base de datos")

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