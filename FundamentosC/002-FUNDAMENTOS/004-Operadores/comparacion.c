#include <stdio.h>

int main (int argc,char *argv[]){
     //si es cierto nos van a dar un 1, si es falso dan un 0
    printf("mayor que: %i \n", (4>3));
    printf("menor que: %i \n", (4<3));
    
    printf("mayor o igual que: %i \n", (4<=3));
    printf("menor o igual que: %i \n", (4<=3));
    
    printf("igualdad: %i \n", (4==3));
    printf("desigualdad: %i \n", (4!=3));

    
    return 0;
}