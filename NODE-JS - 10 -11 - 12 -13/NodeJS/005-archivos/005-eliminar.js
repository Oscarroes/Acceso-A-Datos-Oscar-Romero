var archivos = require('fs');

archivos.unlink('nombreCambiado.txt', function(err){
    if(err) throw err;
    console.log("Mision cumplida");
})