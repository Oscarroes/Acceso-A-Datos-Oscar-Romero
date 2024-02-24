var servidor = require('http');
var archivos = require('fs');

servidor.createServer(function(req,res){

    archivos.readFile('inicio.html', 'utf-8', function(err,data){
        res.writeHead(200,{'Content-Type':'text/html'});
        //no funciona al ejecutarlo en la terminal de VS pero sí en la consola de Windows
        //El error que da es que entiende que en write debiera entrar un String
        res.write(data);
        res.end();
    });

}).listen(3000)