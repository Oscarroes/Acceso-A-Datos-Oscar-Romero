var servidor = require('http');
var archivos = require('fs');
var ruta = require('url');

servidor.createServer(function(req,res){
    res.writeHead(200,{'Content-Type':'text/html'});
    var rutacompleta = ruta.parse(req.url,true);

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

    //vamos a llevar un registro de las url visitadas y  información como la fecha y hora de la visita:
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