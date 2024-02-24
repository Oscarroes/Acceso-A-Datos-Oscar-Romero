var servidor = require('http');

//creamos el servidor con su require y su respuesta y lo arrancamos en el puerto 3000
servidor.createServer(function(req,res){
    //para ver que funciona vamos a sacar un texto por el navegador:
    res.writeHead(200,{'Content-Type':'text/html'});
    res.end("Hola mundo desde Node.js");
    //cada vez que se actualice la web nos da mensaje por consola.
    console.log("Alguien ha cargado la web");
    

}).listen(3000)
//Solo con esto ya tendríamos creado un servidor web
