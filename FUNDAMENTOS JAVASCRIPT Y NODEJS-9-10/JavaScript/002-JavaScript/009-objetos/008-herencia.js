class Animal{
    constructor(){

    }
    respira(){
        return "El aninalico está respirando";
    }

}

class Persona extends Animal{
    //si una clase hereda de otra hay que poner super en el constructor
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

class Perro extends Animal{

    constructor(){
        super();
        this.edad = 0;
        this.nombre = "";
        this.duenno = "";
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
    setDuenno(nuevoDuenno){
        this.duenno = nuevoDuenno;
    }
    getDuenno(){
        return this.duenno;
    }
    fichaCanina(){
        return "La ficha de " + this.nombre + " indica que tiene " + this.edad + " años y su dueño es " + this.duenno;
    }
    ladra(){
        return "Guau! Guau!";
    }
}

var persona1 = new Persona();
var perro1 = new Perro();

persona1.setEdad(45);
persona1.setNombre("Paco");
perro1.setEdad(5);
perro1.setNombre("Pulgas");
perro1.setDuenno("Paco");

console.log(persona1);
console.log(perro1);
console.log("------------------------");
console.log(persona1.saluda());
console.log(persona1.respira());
console.log("------------------------");
console.log(perro1.fichaCanina());
console.log(perro1.respira());
console.log(perro1.getNombre() + " dice: " + perro1.ladra());
