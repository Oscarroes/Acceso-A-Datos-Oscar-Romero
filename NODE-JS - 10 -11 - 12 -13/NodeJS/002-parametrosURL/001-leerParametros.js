var servidor = require('http');
var ruta = require('url');

servidor.createServer(function(req,res){

    res.writeHead(200,{'Content-Type':'text/html'});

    var parametros = ruta.parse(req.url,true).query;
    res.write("Tu nombre es: " + parametros.nombre + "\n");
    res.end("<h1>OK</h1>");

    console.log("Alguien ha cargado la web");

}).listen(3000)
