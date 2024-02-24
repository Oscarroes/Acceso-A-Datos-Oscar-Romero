var servidor = require('http');
var ruta = require('url');

servidor.createServer(function(req,res){

    res.writeHead(200,{'Content-Type':'text/html'});

    var parametros = ruta.parse(req.url,true).query;
    //Para pasarle los parametros los podemos escribir en la barra de navegacion
    //localhost:3000/?nombre=Oscar&apellidos=Perez Lopez
    res.write("Tu nombre es: " + parametros.nombre);
    res.write("<br>");
    res.write("Tus apellidos son: " + parametros.apellidos);
    res.end("<h1>OK</h1>");

    console.log("Alguien ha cargado la web");

}).listen(3000)