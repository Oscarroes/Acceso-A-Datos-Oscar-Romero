//egenda esta vez va a ser una coleccion de colecciones
var agenda = [];
//el indice 0 es una colección también
//esta vez vamos a mezclar indices numericos con alfanumericos
//cada uno en una dimension
agenda[0] = [];
agenda[0]['nombre'] = "Oscar";
agenda[0]['telefono'] = "123456";
agenda[0]['mail'] = "info@oscar.com";

agenda[1] = [];
agenda[1]['nombre'] = "Juan";
agenda[1]['telefono'] = "654123";
agenda[1]['mail'] = "info@juan.com";

agenda[2] = [];
agenda[2]['nombre'] = "Jorge";
agenda[2]['telefono'] = "124563";
agenda[2]['mail'] = "info@jorge.com";

console.table(agenda)
