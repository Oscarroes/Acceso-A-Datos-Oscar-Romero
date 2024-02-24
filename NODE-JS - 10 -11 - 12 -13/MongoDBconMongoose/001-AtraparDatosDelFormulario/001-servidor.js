var servidor = require('http');
var archivos = require('fs');
var procesador = require('querystring');
var ruta = require('url');
var mysql = require('mysql');

var conexion = mysql.createConnection({
    host:"localhost",
    user:"nodejs",
    password:"nodejs",
    database:"nodejs"
});

conexion.connect(function(err){
    if(err) throw err;
    console.log("conectado");
});

servidor.createServer(function(req,res){
    res.writeHead(200,{'Content-Type':'text/html'});
    var rutacompleta = ruta.parse(req.url,true);

    archivos.readFile('plantillas/cabecera.html', 'utf-8', function(err,data){
        res.write(data);

        switch(req.url){
            case "/":
                archivos.readFile('inicio.html', 'utf-8', function(err,data){
                    res.write(data);
                });
                break;
            case "/sobremi":
                archivos.readFile('sobremi.html', 'utf-8', function(err,data){
                    res.write(data);
                });
                break;
            case "/blog":
                //no lee el archivo de blog, va directamente a la base de datos.
                //¿COMO HAGO PARA QUE LEA EL HTML Y LA BASE DE DATOS?
                // archivos.readFile('blog.html', 'utf-8', function(err,data){
                //     res.write(data);
                // });
                conexion.query(`
                    SELECT * FROM entradas
                `, function(err,result,fields){
                    if (err) throw err;
                    console.log(result);
                    for (let i = 0; i < result.length; i++){
                        console.log(result[i]);
                        res.write(`
                            <article>
                                <h4>`+result[i].titulo+`</h4>
                                <time>`+result[i].fecha+`</time>
                                <p>`+result[i].texto+`</p>
                            </article>
                        `);
                    }
                });

                break;
            case "/contacto":
                archivos.readFile('contacto.html', 'utf-8', function(err,data){
                    res.write(data);
                });
                break;
            case "/procesa":
                let datos = '';
                    req.on('data', parte=>{
                        datos += parte.toString();
                    })
                    req.on('end',()=>{
                        var cadena = datos;
                        var procesado = procesador.parse(cadena);
                        console.log(procesado);

                        //vamos a sacar en formato Json para que podamos trabajar con ello en Mongo:
                        var nombre = procesado.nombre;
                        var asunto = procesado.asunto;
                        var email = procesado.email;
                        var mensaje = procesado.mensaje;
                        
                })
                break;
            default:
                res.end("Página no encontrada");
        }
    
            archivos.readFile('plantillas/pieDePagina.html', 'utf-8', function(err,data){
                res.write(data);
                res.end("");
            });

    });

    if(req.url != "/favicon.ico"){
        var fecha = new Date();
        var mes = fecha.getMonth()+1;
        archivos.appendFile("registro.txt",fecha.getFullYear() + "," + mes + "," +
        fecha.getDate() + "," + fecha.getHours() + "," + fecha.getMinutes() + "," + fecha.getSeconds() + "," +
        rutacompleta.host + "," + rutacompleta.pathname + "," +
        rutacompleta.search + "," + req.url + "\n", function(err){
            if(err) throw err;
            console.log("Mision cumplida");
        })
    }
    
}).listen(3000)