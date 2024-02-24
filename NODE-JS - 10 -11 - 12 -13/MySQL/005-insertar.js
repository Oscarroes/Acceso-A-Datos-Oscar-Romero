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
        INSERT INTO entradas VALUES(
            NULL,
            'Titulo de la entrada',
            'texto de la entrada',
            '2024-02-15'
        )
    `, function(err,result){
        if (err) throw err;
        console.log("Se ha insertado el registro");
    });
});