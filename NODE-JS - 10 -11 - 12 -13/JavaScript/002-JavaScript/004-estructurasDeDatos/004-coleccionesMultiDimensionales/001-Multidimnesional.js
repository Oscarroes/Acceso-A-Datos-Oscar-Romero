//egenda esta vez va a ser una coleccion de colecciones
var agenda = [];
//el indice 0 es una colección también
agenda[0] = [];
agenda[0][0] = "Oscar";
agenda[0][1] = "123456";
agenda[0][2] = "info@oscar.com";

agenda[1] = [];
agenda[1][0] = "Juan";
agenda[1][1] = "654123";
agenda[1][2] = "info@juan.com";

agenda[2] = [];
agenda[2][0] = "Jorge";
agenda[2][1] = "124563";
agenda[2][2] = "info@jorge.com";

console.table(agenda)
