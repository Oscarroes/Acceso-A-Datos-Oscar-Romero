var servidor = require('http');
var archivos = require('fs');

servidor.createServer(function(req,res){
    res.writeHead(200,{'Content-Type':'text/html'});

    switch(req.url){
        case "/":
            archivos.readFile('inicio.html', 'utf-8', function(err,data){
                res.write(data);
                res.end();
            });
            break;
        case "/sobremi":
            archivos.readFile('sobremi.html', 'utf-8', function(err,data){
                res.write(data);
                res.end();
            });
            break;
        case "/contacto":
            archivos.readFile('contacto.html', 'utf-8', function(err,data){
                res.write(data);
                res.end();
            });
            break;
        default:
            res.end("Página no encontrada");
    }

    //vamos a llevar un registro de las url visitadas:
    //nos quitamos el favicon, que se carga cada vez que cambias de página
    if(req.url != "/favicon.ico"){
        archivos.appendFile("registro.txt", req.url + "\n", function(err){
            if(err) throw err;
            console.log("Mision cumplida");
        })
    }
    
}).listen(3000)