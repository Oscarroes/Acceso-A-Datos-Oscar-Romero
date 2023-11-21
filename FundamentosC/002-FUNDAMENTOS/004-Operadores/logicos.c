#include <stdio.h>

int main (int argc,char *argv[]){
    //AND
    printf("dime si es cierto: %i \n", (4>3 && 3>2 && 2>1));//si es cierto nos va a dar un 1, si es falso da un cero
    printf("dime si es cierto: %i \n", (4>3 && 3>2 && 2>5));//esta va a dar 0 porque una de ellas no es cierta
    //OR
    printf("dime si es cierto: %i \n", (4>3 || 3>2 || 2>5));//es cierta si al menos una es cierta
    printf("dime si es cierto: %i \n", (4>6 || 3>7 || 2>5));//es falsa si todas son falsas y daría 0

    return 0;
}