var archivos = require('fs');

archivos.rename("nuevo.txt", 'nombreCambiado.txt', function(err){
    if(err) throw err;
    console.log("Mision cumplida");
})