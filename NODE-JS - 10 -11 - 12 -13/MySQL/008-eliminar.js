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
        DELETE FROM entradas WHERE id = 2
    `, function(err,result){
        if (err) throw err;
        console.log("Se ha eliminado el registro");
    });
});