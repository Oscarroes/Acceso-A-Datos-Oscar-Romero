//Los setters y getters nos sirven para proteger la información dentro de la clase
class Persona{
    constructor(){
        this.edad = 0;
        this.nombre = "";
    }
    setEdad(nuevaEdad){
        this.edad = nuevaEdad;
    }
    getEdad(){
        console.log(this.edad);
    }
    setNombre(nuevoNombre){
        this.nombre = nuevoNombre;
    }
    getNombre(){
        console.log(this.nombre);
    }
    saluda(){
        console.log("Hola, me llamo " + this.nombre + " y tengo " + this.edad + " años.");
    }
}

var persona1 = new Persona();
persona1.setEdad(45);
persona1.setNombre("Paco");
console.log(persona1);
persona1.saluda();