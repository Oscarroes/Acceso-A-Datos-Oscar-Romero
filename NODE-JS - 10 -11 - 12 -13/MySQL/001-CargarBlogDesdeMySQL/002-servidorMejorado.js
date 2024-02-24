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
            case "/sobremi":
                archivos.readFile('sobremi.html', 'utf-8', function(err,sobremi){
                    if (err) throw err;
                    res.write(cabecera + sobremi + pieDePagina);
                    res.end("");
                });
                break;
            case "/blog":
                //no lee el archivo de blog, va directamente a la base de datos.
                //¿COMO HAGO PARA QUE LEA EL HTML Y LA BASE DE DATOS?
                archivos.readFile('blog.html', 'utf-8', function(err,blog){
                    if (err) throw err;

                    conexion.query(`
                        SELECT * FROM entradas
                    `, function(err,result,fields){
                        if (err) throw err;

                        var entradasHTML = '';
                        console.log(result);
                        for (let i = 0; i < result.length; i++){
                            entradasHTML += `
                                <article>
                                    <h4>`+result[i].titulo+`</h4>
                                    <time>`+result[i].fecha+`</time>
                                    <p>`+result[i].texto+`</p>
                                </article>
                            `;
                        }
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
                let datos = '';
                    req.on('data', parte=>{
                        datos += parte.toString();
                    })
                    req.on('end',()=>{
                        var cadena = datos;
                        var procesado = procesador.parse(cadena);
                        console.log(procesado);
                })
                break;
            default:
                res.end("Página no encontrada");
        }
    
    });
});

    if(req.url != "/favicon.ico"){
        var fecha = new Date();
        archivos.appendFile("registro.txt",fecha.getFullYear() + "," + fecha.getMonth()+1 + "," +
        fecha.getDate() + "," + fecha.getHours() + "," + fecha.getMinutes() + "," + fecha.getSeconds() + "," +
        rutacompleta.host + "," + rutacompleta.pathname + "," +
        rutacompleta.search + "," + req.url + "\n", function(err){
            if(err) throw err;
            console.log("Mision cumplida");
        })
    }
    
}).listen(3000)