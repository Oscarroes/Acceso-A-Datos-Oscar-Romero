#include <stdio.h>

int main (int argc,char *argv[]){
    
    char* agenda[10][4];
    
    agenda[0][0] = "Jose";
    agenda[0][1] = "Barbas Lino";
    agenda[0][2] = "1236548";
    agenda[0][3] = "jose.bl@gmail.com";
    
    agenda[1][0] = "Juan";
    agenda[1][1] = "Lopez Garcia";
    agenda[1][2] = "2548799";
    agenda[1][3] = "juan.ju@gmail.com";
    
    printf("El correo del segundo registro de la agenda es %s \n", agenda[1][3]);
    
    return 0;
}