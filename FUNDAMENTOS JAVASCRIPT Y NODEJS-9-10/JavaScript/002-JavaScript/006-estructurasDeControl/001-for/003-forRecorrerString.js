var valido = false;
var email1 = "oscar.info@gmail.com";
var email2 = "oscar.info#gmail.com";

for(let i = 0; i<=email1.length; i++){
    if(email1[i]=="@"){
        valido = true;
    }
}

if(valido == true){
    console.log("El mail: "+email1+" es correcto");
}else{
    console.log("El mail: "+email1+" es incorrecto");
}

var valido = false;

for(let i = 0; i<=email2.length; i++){
    if(email2[i]=="@"){
        valido = true;
    }
}

if(valido == true){
    console.log("El mail: "+email2+" es correcto");
}else{
    console.log("El mail: "+email2+" es incorrecto");
}