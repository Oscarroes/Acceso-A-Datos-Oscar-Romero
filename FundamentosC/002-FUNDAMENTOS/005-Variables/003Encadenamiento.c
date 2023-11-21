#include <stdio.h>
#include <string.h> //importar la libreria de Strings

int main (int argc,char *argv[]){
    char nombre[] = "Juan ";
    char apellidos[] = "Velasco Tena";
    
    strcat(nombre,apellidos);
    printf("Mi nombre completo es: %s", nombre);
    
    return 0;
}