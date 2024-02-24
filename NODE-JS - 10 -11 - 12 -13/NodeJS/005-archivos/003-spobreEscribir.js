var archivos = require('fs');

//para sobreescribir el contenido usamos writeFile
archivos.writeFile("nuevo.txt", 'Este es mi contenido 2 \n', function(err){
    if(err) throw err;
    console.log("Mision cumplida");
})