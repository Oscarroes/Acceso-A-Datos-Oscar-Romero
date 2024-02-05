class Animal{
    constructor(){

    }
    respira(){
        return "El aninalico está respirando";
    }

}
class Persona extends Animal{
    //si una clase hereda de otra hay que poner superconstructor
    constructor(){
        super();
        this.edad = 0;
        this.nombre = "";
    }
    setEdad(nuevaEdad){
        this.edad = nuevaEdad;
    }
    getEdad(){
        return this.edad;
    }
    setNombre(nuevoNombre){
        this.nombre = nuevoNombre;
    }
    getNombre(){
        return this.nombre;
    }
    saluda(){
        return "Hola, me llamo " + this.nombre + " y tengo " + this.edad + " años.";
    }
}

var persona1 = new Persona();
persona1.setEdad(45);
persona1.setNombre("Paco");
console.log(persona1);
console.log(persona1.saluda());
console.log(persona1.respira());
