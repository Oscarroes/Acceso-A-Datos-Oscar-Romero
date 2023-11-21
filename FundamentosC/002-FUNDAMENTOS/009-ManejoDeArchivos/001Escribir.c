#include <stdio.h>

int main (int argc,char *argv[]){
    
    //apertura de un archivo
    FILE *archivo;
    
    //el archivo tiene nombre y se abre en modo escritura
    archivo = fopen("agenda.txt","w");
    //escribo en el archivo
    fprintf(archivo,"Este es un nuevo mensaje \n");
    //cierro el archivo
    fclose(archivo);
    return 0;
}

