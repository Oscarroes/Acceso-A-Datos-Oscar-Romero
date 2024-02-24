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

//nos conectamos al servidor
mongoose.connect(conexion,{useNewUrlParser:true,useUnifiedTopology:true}).then(function(){
    console.log("conectado a mongo")
    //Una vez conectados hacemos una petición a la base de datos
    formulario.find({})
        //Ejecutamos y entonces los presentamos
        .exec()
        .then(function(formularios){
            console.log(formularios);
        });
});