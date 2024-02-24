var mongoose = require('mongoose');

//creamos la conexion al servidor
const conexion = 'mongodb://127.0.0.1/contacto';

//primero preparamos el esquema de datos para que Node sepa lo que vamos a traer de la base de datos
const formularioSchema = new mongoose.Schema({
    nombre:String,
    asunto:String,
    mensaje:String,
    fecha:String
});

const formulario = mongoose.model("Formulario",formularioSchema);

const nuevoFormulario = new formulario({
    nombre:"Oscar",
    asunto:"Este es un mensaje desde Node",
    mensaje:"Este es el cuerpo del mensaje",
    fecha:"2024-02-18"
});

//nos conectamos al servidor
mongoose.connect(conexion,{useNewUrlParser:true,useUnifiedTopology:true}).then(function(){
    console.log("conectado a mongo")
    //Una vez conectados hacemos una petición a la base de datos
    //en este caso vamos a insertar el registro nuevoFormulario, no funciona igual que con los comandos en este caso
    //en lugar de insertOne lo hacemos con save():
        nuevoFormulario.save().then(function(){
            console.log("Registro insertado");
        });
});