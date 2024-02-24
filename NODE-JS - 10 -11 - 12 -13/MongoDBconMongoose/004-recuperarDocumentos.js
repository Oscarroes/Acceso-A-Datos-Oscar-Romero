var mongoose = require('mongoose');

const conexion = 'mongodb://127.0.0.1/contacto';

//primero preparamos el esquema de datos para que Node sepa lo que vamos a traer de la base de datos
const formularioSchema = new mongoose.Schema({
    nombre:String,
    asunto:String,
    mensaje:String,
    fecha:String
});

const formulario = mongoose.model("Formulario",formularioSchema)

mongoose.connect(conexion,{useNewUrlParser:true,useUnifiedTopology:true}).then(function(){
    console.log("conectado a mongo")
});

