#include <stdio.h>

int main (int argc,char *argv[]){
    
    float altura =1.786;
    float peso = 90.82;
    //Con %.2f damos un corte en la impresión del número de 2 decimales
    printf("Mi altura es de %.2f metros y mi peso es de %f kilos \n",altura,peso);
    return 0;
}