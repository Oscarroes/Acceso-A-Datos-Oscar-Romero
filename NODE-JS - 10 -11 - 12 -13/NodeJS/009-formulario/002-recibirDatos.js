var servidor = require('http');
var ruta = require('url');

servidor.createServer(function(req,res){
    res.writeHead(200,{'Content-Type':'text/html'});

    switch(req.url){
        case "/":
                res.write(`
                    <form action="/procesa" method="POST">
                        <input type="text" name="nombre">
                        <input type="submit">
                    </form>
                `);
            break;
        //Vamos a recibir los datos escritos en el formulario al pulsar enviar
        case "/procesa":
            let datos = '';
            req.on('data', parte=>{
                datos += parte.toString();
            })
            req.on('end',()=>{
                console.log(datos);
            })
            break;

    }
    res.end("");

}).listen(3000)