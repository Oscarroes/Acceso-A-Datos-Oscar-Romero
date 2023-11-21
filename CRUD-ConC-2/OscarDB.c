#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[]){
    FILE *archivo;
    FILE *archivoTemp;
    char *operacion = argv[1];
    char *basededatos = argv[2];
    char *nombreArchivo = argv[3];
    
    char ruta[100];
    strcpy(ruta,basededatos);
    strcat(ruta,"-");
    strcat(ruta,nombreArchivo);
    strcat(ruta,".txt");
    
    
    if(strcmp(operacion,"select")==0){
        archivo = fopen(ruta,"r");
        printf("Te doy datos:\n");
        char linea[1024];

        while(fgets(linea,sizeof(linea),archivo) != NULL){
            printf("Linea: %s", linea);
        }
            
    }else if(strcmp(operacion,"insert")==0){
        archivo = fopen(ruta,"a");
        char *texto = argv[4];
        fputs(strcat(texto,"\n"),archivo);
        fclose(archivo);

    }else if(strcmp(operacion,"delete")==0){
        archivo = fopen(ruta,"r");
        archivoTemp = fopen("temporal.txt","w");
        char *texto = argv[4];
        char linea[1024];

        while(fgets(linea,sizeof(linea),archivo) != NULL){
            if(strstr(linea, texto) == NULL){
                fputs(linea,archivoTemp);
            }
        }
        fclose(archivo);
        fclose(archivoTemp);

        remove(ruta);
        rename("temporal.txt", ruta);

    }else if(strcmp(operacion,"update")==0){
        archivo = fopen(ruta,"a");
        char *texto = argv[4];
        char linea[1024];
        char *modificado = argv[5];

        fputs(strcat(modificado,"\n"),archivo);
        fclose(archivo);

        archivo = fopen(ruta,"r");
        archivoTemp = fopen("temporal.txt","w");

        while(fgets(linea,sizeof(linea),archivo) != NULL){
            if(strstr(linea, texto) == NULL){
                fputs(linea,archivoTemp);
            }
        }
        fclose(archivo);
        fclose(archivoTemp);

        remove(ruta);
        rename("temporal.txt", ruta);

    }
    return 0;
}