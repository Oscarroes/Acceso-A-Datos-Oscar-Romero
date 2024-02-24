function saluda(nombre,telefono,email){
    cadena = "";
    cadena += "Me llamo " + nombre + ".\n";
    cadena += "Mi teléfono es " + telefono + ".\n";
    cadena += "Mi correo es " + email + ".\n";

    return cadena;
}

console.log(saluda("Oscar",123456,"oscar.info@gmail.com"));
console.log(saluda("Juan",124563,"juan.info@gmail.com"));
console.log(saluda("Jorge",365214,"jorge.info@gmail.com"));
