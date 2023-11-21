#include <stdio.h>

int main (int argc,char *argv[]){
    
    int dia =1;
    while(dia < 31){
        
        printf("Hoy es el día: %i del mes \n", dia);
        dia ++; //En los While hay que controlar la condición de parada o salida del bucle
    }
    
    
    
    return 0;
}