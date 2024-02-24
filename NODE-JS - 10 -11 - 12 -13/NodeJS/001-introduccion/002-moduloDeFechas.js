var servidor = require('http');

servidor.createServer(function(req,res){
    fecha = new Date();

    res.writeHead(200,{'Content-Type':'text/html'});
    //con res.write escribimos y con res.end ponemos el ultimo mensaje
    res.write("Hola mundo desde Node.js");
    //Hay que ponerlo como si fuese texto, porque espera que sea número.
    res.end("" + fecha.getFullYear() + "");

    console.log("Alguien ha cargado la web");
    
}).listen(3000)
