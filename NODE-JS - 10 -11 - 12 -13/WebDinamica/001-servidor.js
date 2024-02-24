var servidor = require('http');
var archivos = require('fs');
var procesador = require('querystring');
var ruta = require('url');
var mysql = require('mysql');

var conexion = mysql.createConnection({
    host:"localhost",
    user:"nodejs",
    password:"nodejs",
    database:"academia"
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
            case "/sobreElCentro":
                archivos.readFile('sobreElCentro.html', 'utf-8', function(err,sobreElCentro){
                    if (err) throw err;

                    conexion.query(`
                            SELECT * FROM entradascentro
                        `, function(err,result,fields){
                        if (err) throw err;

                        var entradasHTML = '';
                        console.log(result);
                        for (let i = 0; i < result.length; i++){
                            entradasHTML += `
                                <article>
                                    <h3>`+result[i].tituloinfo+`</h3>
                                    <p>`+result[i].textoinfo+`</p>
                                </article>
                            `;
                        }
                        // Reemplaza el marcador de posición en sobreElCentro.html con las entradas dinámicas
                        sobreElCentro = sobreElCentro.replace('<!--ENTRADAS-->', entradasHTML);

                    });

                    conexion.query(`
                        SELECT * FROM profesores
                    `, function(err,result,fields){
                    if (err) throw err;

                    var entradasHTML2 = '';
                    console.log(result);
                    for (let i = 0; i < result.length; i++){
                        entradasHTML2 += `
                            <article>
                                <h3>`+result[i].nombre+`</h3>
                                <h4>`+result[i].asignatura+`</h4>
                                <p>`+result[i].descripcion+`</p>
                            </article>
                        `;
                    }
                    // Reemplaza el marcador de posición en sobreElCentro.html con las entradas dinámicas
                    sobreElCentro = sobreElCentro.replace('<!--ENTRADAS2-->', entradasHTML2);

                    res.write(cabecera + sobreElCentro + pieDePagina);
                    res.end("");
                });
                });
                break;
            case "/blog":
                archivos.readFile('blog.html', 'utf-8', function(err,blog){
                    if (err) throw err;

                    conexion.query(`
                        SELECT * FROM entradasblog
                    `, function(err,result,fields){
                        if (err) throw err;

                        var entradasHTML = '';
                        console.log(result);
                        for (let i = 0; i < result.length; i++){
                            entradasHTML += `
                                <article>
                                    <h3>`+result[i].titulo+`</h3>
                                    <p>`+result[i].articulo+`</p>
                                    <time>`+result[i].fecha+`</time>
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
                if(req.method === 'POST'){
                    let datos = '';
                    req.on('data', parte=>{
                        datos += parte.toString();
                    });
                    req.on('end',()=>{
                        //procesar los datos del formulario
                        var procesado = procesador.parse(datos);
                        console.log(procesado);

                        // Insertar los datos en la tabla MySQL
                        conexion.query(`
                            INSERT INTO contactos (nombre, telefono, email, mensaje) 
                            VALUES (?, ?, ?, ?)
                            `, [procesado.nombre, procesado.telefono, procesado.email, procesado.mensaje], function(err, result){
                            if (err) {
                                console.error('Error al insertar datos:', err);
                                // Si hay error:
                            } else {
                                console.log('Datos insertados correctamente.');
                                //redirigir a enviado.html después de procesar el formulario
                                archivos.readFile('enviado.html', 'utf-8', function(err,enviado){
                                    if (err) throw err;
                                    res.write(cabecera + enviado + pieDePagina);
                                    res.end("");
                                });
                            }
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
            //console.log("Acceso registrado");
            //rutacompleta.host + "," + 
            //rutacompleta.search + "," + 
        })
    }
    
}).listen(3000)