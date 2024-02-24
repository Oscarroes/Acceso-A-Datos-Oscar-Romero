var servidor = require('http');
var archivos = require('fs');
var ruta = require('url');
var procesador = require('querystring');
var mongoose = require('mongoose');


//creamos la conexion al servidor de Mongo
const conexionMongoose = 'mongodb://127.0.0.1/Academia';

const contactosSchema = new mongoose.Schema({
    nombre:String,
    telefono:String,
    email:String,
    mensaje:String
});

const contactos = mongoose.model("contactos",contactosSchema);

const blogsSchema = new mongoose.Schema({
    titulo:String,
    articulo:String,
    fecha:String
})
const blogs = mongoose.model("blogs", blogsSchema);

const centroentradasSchema = new mongoose.Schema({
    titulo:String,
    articulo:String
})

const centroentradas = mongoose.model("centroentradas", centroentradasSchema);

const profesoresSchema = new mongoose.Schema({
    nombre:String,
    informacion:String,
    asignatura:String
})

const profesores = mongoose.model("profesores", profesoresSchema);

//nos conectamos al servidor de Mongo
mongoose.connect(conexionMongoose,{useNewUrlParser:true,useUnifiedTopology:true}).then(function(){
    console.log("conectado a mongo")
});

servidor.createServer(function(req,res){
    res.writeHead(200,{'Content-Type':'text/html'});
    var rutacompleta = ruta.parse(req.url,true);

    archivos.readFile('plantillas/cabecera.html', 'utf-8', function(err,cabecera){
        if (err) throw err;

    archivos.readFile('plantillas/pieDePagina.html', 'utf-8', function(err,pieDePagina){
        if (err) throw err;

        switch(req.url){
            case "/":
                archivos.readFile('inicio.html', 'utf-8', function(err,inicio){
                    if (err) throw err;
                    res.write(cabecera + inicio + pieDePagina);
                    res.end("");
                });
                break;
            case "/sobreElCentro":
                archivos.readFile('sobreElCentro.html', 'utf-8', function(err,sobreElCentro){
                    if (err) throw err;

                    centroentradas.find({}).then(function(resultados) {
                        // Construir el HTML con los datos de los blogs
                        var entradasHTML = "";
                        resultados.forEach(function(entrada) {
                            "<article>"
                                entradasHTML += "<h3>" + entrada.titulo + "</h3>";
                                entradasHTML += "<p>" + entrada.articulo + "</p>";
                            "</article>"
                        });
                        // Reemplaza el marcador de posición en blog.html con las entradas dinámicas
                        sobreElCentro = sobreElCentro.replace('<!--ENTRADAS-->', entradasHTML);

                        profesores.find({}).then(function(resultados2) {
                            // Construir el HTML con los datos de los blogs
                            var entradasHTML2 = "";
                            resultados2.forEach(function(entrada2) {
                                "<article>"
                                    entradasHTML2 += "<h3>" + entrada2.nombre + "</h3>";
                                    entradasHTML2 += "<h4>" + entrada2.asignatura + "</h4>";
                                    entradasHTML2 += "<p>" + entrada2.informacion + "</p>";
                                "</article>"
                            });
                            // Reemplaza el marcador de posición en blog.html con las entradas dinámicas
                            sobreElCentro = sobreElCentro.replace('<!--ENTRADAS2-->', entradasHTML2);

                        res.write(cabecera + sobreElCentro + pieDePagina);
                        res.end("");
                        });
                    });
                });
                break;
            case "/blog":
                archivos.readFile('blog.html', 'utf-8', function(err,blog){
                    if (err) throw err;
                    blogs.find({}).then(function(resultados) {
                        // Construir el HTML con los datos de los blogs
                        var entradasHTML = "";
                        resultados.forEach(function(entrada) {
                            entradasHTML += "<h3>" + entrada.titulo + "</h3>";
                            entradasHTML += "<p>" + entrada.articulo + "</p>";
                            entradasHTML += "<time>" + entrada.fecha + "</time>";
                        });
                        // Reemplaza el marcador de posición en blog.html con las entradas dinámicas
                        blog = blog.replace('<!--ENTRADAS-->', entradasHTML);
                        res.write(cabecera + blog + pieDePagina);
                        res.end("");
                        });
                });

                break;
            case "/contacto":
                archivos.readFile('contacto.html', 'utf-8', function(err,contacto){
                    if (err) throw err;
                    res.write(cabecera + contacto + pieDePagina);
                    res.end("");
                });
                break;
            case "/procesa":
                if(req.method === 'POST'){
                    let datos = '';
                    req.on('data', parte=>{
                        datos += parte.toString();
                    });
                    req.on('end',()=>{
                        //procesar los datos del formulario
                        var procesado = procesador.parse(datos);
                        console.log(procesado);

                        //Formatear los datos para insertarlos en MongoDB
                        var nuevoNombre = procesado.nombre;
                        var nuevoTelefono = procesado.telefono;
                        var nuevoEmail = procesado.email;
                        var nuevoMensaje = procesado.mensaje;

                        var nuevoContactos = new contactos({
                            nombre:nuevoNombre,
                            telefono:nuevoTelefono,
                            email:nuevoEmail,
                            mensaje:nuevoMensaje
                        });

                        // Insertar los datos en MongoDB con save():
                        nuevoContactos.save().then(function(){
                                console.log('Datos insertados correctamente.');
                                //redirigir a enviado.html después de procesar el formulario
                                archivos.readFile('enviado.html', 'utf-8', function(err,enviado){
                                    if (err) throw err;
                                    res.write(cabecera + enviado + pieDePagina);
                                    res.end("");
                                });
                        });
        
                    });
                }else {
                    // Si la solicitud no es POST, redirigir a página no encontrada
                    res.end("Página no encontrada");
                }
                break;
            default:
                res.end("Página no encontrada");
        }
    
    });
});

    if(req.url != "/favicon.ico"){
        var fecha = new Date();
        var mes = fecha.getMonth()+1;
        archivos.appendFile("registro.txt","fecha de acceso: " + fecha.getFullYear() + "," + mes + "," +
        fecha.getDate() + "," + fecha.getHours() + "," + fecha.getMinutes() + "," + fecha.getSeconds() + " | " +
        "ruta: " + rutacompleta.pathname + "," +
        req.url + "\n", function(err){
            if(err) throw err;

        })
    }
    
}).listen(3000)