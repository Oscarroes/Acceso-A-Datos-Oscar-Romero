#include <stdio.h>
#include <string.h>

int main (int argc,char *argv[]){
    char nombre[] = "Juan";
    strcpy(nombre,"Jorge");
    int edad = 26;
    float altura =1.786;
    float peso = 90.82;
    
    printf("Mi nombre es %s mi edad es %i mi altura es de %.2f metros y mi peso es de %f kilos \n",nombre,edad,altura,peso);
    return 0;
}