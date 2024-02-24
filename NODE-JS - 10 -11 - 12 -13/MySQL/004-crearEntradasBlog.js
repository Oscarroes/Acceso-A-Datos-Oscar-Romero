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
        CREATE TABLE entradas
        (id INT AUTO_INCREMENT PRIMARY KEY,
        titulo VARCHAR(255),
        texto TEXT,
        fecha VARCHAR(255)
            )
    `, function(err,result){
        if (err) throw err;
        console.log("Se ha creado la tabla");
    });
})