var mysql = require('mysql');

var conexion = mysql.createConnection({
    host:"localhost",
    user:"nodejs",
    password:"nodejs",
    database:"nodejs2"
});

conexion.connect(function(err){
    if(err) throw err;
    console.log("conectado");
    conexion.query(`
        UPDATE entradas SET titulo = 'titulo modificado'
        WHERE id = 1
    `, function(err,result){
        if (err) throw err;
        console.log("Se ha modificado el registro");
    });
});