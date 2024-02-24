//pop quita el ultimo elemento del array

var agenda = [];
agenda[0] = "Oscar";
agenda[1] = "Juan";
agenda[2] = "Jorge";
agenda.push("Julia");
console.table(agenda);

//quitamos a Juila
console.log("Quitamos a Julia con un console.pop")
agenda.pop();
console.table(agenda);
