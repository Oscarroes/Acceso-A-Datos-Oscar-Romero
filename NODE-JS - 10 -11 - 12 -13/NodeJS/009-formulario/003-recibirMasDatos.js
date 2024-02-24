var servidor = require('http');
var ruta = require('url');

servidor.createServer(function(req,res){
    res.writeHead(200,{'Content-Type':'text/html'});

    switch(req.url){
        case "/":
                res.write(`
                    <form action="/procesa" method="POST">
                        <input type="text" name="nombre"><br>
                        <input type="text" name="asunto"><br>
                        <input type="email" name="email"><br>
                        <textarea name="mensaje"></textarea><br>
                        <input type="submit">
                    </form>
                `);
            break;
        //Vamos a recibir los datos escritos en el formulario al pulsar enviar
        //nos va a sacar los datos en formato de URL
        //vamos a pasarlo a Json
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