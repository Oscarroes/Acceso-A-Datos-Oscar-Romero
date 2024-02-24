var archivos = require('fs');
//ojo, ejecutarlo en la terminal de VS crea el archivo en la raiz, sin embargo,
//La consola de Windows lo crea en la carpeta donde está el archivo.js
archivos.appendFile("nuevo.txt", 'Este es mi contenido', function(err){
    if(err) throw err;
    console.log("Mision cumplida");
})