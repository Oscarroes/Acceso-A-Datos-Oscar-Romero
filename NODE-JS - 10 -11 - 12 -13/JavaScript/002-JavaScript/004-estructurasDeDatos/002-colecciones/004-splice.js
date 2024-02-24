//con splice elegimos el elemento o elementos que queremos quitar

var agenda = [];
agenda[0] = "Oscar";
agenda[1] = "Juan";
agenda[2] = "Jorge";
agenda.push("Julia");
console.table(agenda);

//quitamos al primer elemento (el indice 0)
console.log("Quitamos el indice 0 con un console.splice")
agenda.splice(0,1);
console.table(agenda);