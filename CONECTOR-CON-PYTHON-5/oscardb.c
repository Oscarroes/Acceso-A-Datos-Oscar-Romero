#include <stdio.h>
#include <string.h>
#include <unistd.h> //incluye funciones para manejar carpetas
#include <sys/stat.h> //incluye funciones de permisos a usuarios


int main(int argc, char *argv[]){
    FILE *archivo;
    FILE *archivoTemp;
    char *operacion = argv[1];
    char *basededatos = argv[2];
    char *coleccion = argv[3];
    
    if(strcmp(operacion,"select")==0){
        char *documento = argv[4];
        char ruta[100];
        strcpy(ruta,"db/");
        strcat(ruta,basededatos);
        strcat(ruta,"/");
        strcat(ruta,coleccion);
        strcat(ruta,"/");
        strcat(ruta,documento);
        strcat(ruta,".json");
        archivo = fopen(ruta,"r");
        printf("Los datos pedidos son:\n");
        char linea[1024];

        while(fgets(linea,sizeof(linea),archivo) != NULL){
            printf("Linea: %s", linea);
        }
            
    }else if(strcmp(operacion,"select_like")==0){
        char *documento = argv[4];
        char *texto = argv[5];
        char linea[1024];
        char ruta[100];
        int encontrado = 0;
        strcpy(ruta,"db/");
        strcat(ruta,basededatos);
        strcat(ruta,"/");
        strcat(ruta,coleccion);
        strcat(ruta,"/");
        strcat(ruta,documento);
        strcat(ruta,".json");
        
        archivo = fopen(ruta,"r");
        
        while(fgets(linea,sizeof(linea),archivo) != NULL && !encontrado){
            char *resultado = strstr(linea, texto);
            if (resultado != NULL) {
                printf("Coincidencia encontrada: %s\n", linea);
                encontrado = 1;
            }  
        }
        if(!encontrado){
                printf("%s no se encuentra en el archivo %s",texto,documento);
            }
        fclose(archivo);

    }else if(strcmp(operacion,"insert")==0){
        char *documento = argv[4];
        char ruta[100];
        strcpy(ruta,"db/");
        strcat(ruta,basededatos);
        strcat(ruta,"/");
        strcat(ruta,coleccion);
        strcat(ruta,"/");
        strcat(ruta,documento);
        strcat(ruta,".json");
        archivo = fopen(ruta,"w");
        char *texto = argv[5];

        fputs(strcat(texto,"\n"),archivo);
        fclose(archivo);

        if (chmod(ruta, S_IRWXU | S_IRWXG | S_IRWXO) == 0) {
            printf("Permisos establecidos.\n");
    }

    }else if(strcmp(operacion,"create_collection")==0){
            char rutaColeccion[200];
            strcpy(rutaColeccion,"db/");
            strcat(rutaColeccion,basededatos);
            strcat(rutaColeccion,"/");
            strcat(rutaColeccion,coleccion);

            if(mkdir(rutaColeccion) == 0){
                int permisos = chmod(rutaColeccion, S_IRWXU | S_IRWXG | S_IRWXO);
                if (permisos == 0) {
                    printf("Carpeta creada.\n");
                    printf("Permisos establecidos.\n");
                }
            }else{
                printf("Error al crear carpeta");
            }

    }else if(strcmp(operacion,"delete")==0){
        char *documento = argv[4];
        char *texto = argv[5];
        char linea[1024];
        char ruta[100];
        strcpy(ruta,"db/");
        strcat(ruta,basededatos);
        strcat(ruta,"/");
        strcat(ruta,coleccion);
        strcat(ruta,"/");
        strcat(ruta,documento);
        strcat(ruta,".json");

        remove(ruta);
        printf("Documento eliminado.\n");

    }else if(strcmp(operacion,"update")==0){
        char *documento = argv[4];
        char *texto = argv[5];
        char *modificado = argv[6];
        char linea[1024];
        char ruta[100];
        strcpy(ruta,"db/");
        strcat(ruta,basededatos);
        strcat(ruta,"/");
        strcat(ruta,coleccion);
        strcat(ruta,"/");
        strcat(ruta,documento);
        strcat(ruta,".json");
        char rutaTemp[100];
        strcpy(rutaTemp,"db/");
        strcat(rutaTemp,basededatos);
        strcat(rutaTemp,"/");
        strcat(rutaTemp,coleccion);
        strcat(rutaTemp,"/");
        strcat(rutaTemp,documento);
        strcat(rutaTemp,"temporal.json");

        archivo = fopen(ruta,"a");

        fputs(strcat(modificado,"\n"),archivo);
        fclose(archivo);

        archivo = fopen(ruta,"r");
        archivoTemp = fopen(rutaTemp,"w");

        while(fgets(linea,sizeof(linea),archivo) != NULL){
            if(strstr(linea, texto) == NULL){
                fputs(linea,archivoTemp);
                printf("El archivo ha sido modificado.\n");
            }
        }
        fclose(archivo);
        fclose(archivoTemp);

        remove(ruta);
        rename(rutaTemp, ruta);

    }else if (strcmp(operacion,"update_collection") == 0){
            char rutaColeccion[200];
            char rutaModificada[200];
            char *coleccionModificado = argv[4];

            strcpy(rutaColeccion,"db/");
            strcat(rutaColeccion,basededatos);
            strcat(rutaColeccion,"/");
            strcat(rutaColeccion,coleccion);

            strcpy(rutaModificada,"db/");
            strcat(rutaModificada,basededatos);
            strcat(rutaModificada,"/");
            strcat(rutaModificada,coleccionModificado);
            
            if(rename(rutaColeccion,rutaModificada) == 0){
                printf("Carpeta modificada");
            }else{
                printf("Error al renombrar carpeta");
            }
 
    }else{
        printf("La operación no es valida");
    }
    
    return 0;
}