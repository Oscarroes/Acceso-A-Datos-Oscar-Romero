#include <stdio.h>

int main (int argc,char *argv[]){
    char *numero = argv[1]; //con esto le podemos meter la entrada por consola como parámetro seguido del a.exe en la consola
    printf("El numero que has introducido es %s \n", numero); //el \n sirve para cambiar de línea
    
    return 0;
}