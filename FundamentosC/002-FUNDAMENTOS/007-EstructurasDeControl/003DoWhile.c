#include <stdio.h>

int main (int argc,char *argv[]){
    
    int edad =45;
    do{
        printf("Tu edad es de: %i anhos, eres menor de 60 \n",edad);
        edad++;
    }while(edad < 60);

    return 0;
}