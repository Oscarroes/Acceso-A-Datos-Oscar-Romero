var mysql = require('mysql');

var conexion = mysql.createConnection({
    host:"localhost",
    user:"nodejs",
    password:"nodejs"
});

conexion.connect(function(err){
    if(err) throw err;
    console.log("conectado");
    conexion.query('CREATE DATABASE nodejs2', function(err,result){
        if (err) throw err;
        console.log("Se ha creado la base de datos");
    });
})