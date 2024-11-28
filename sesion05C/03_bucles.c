#include <stdio.h>

#define NUM_SUM 100

/*Variables*/
int main(){
    int suma=0;
    int cont=0;

    for (int i = 0; i < NUM_SUM; i++)
    {
        suma=suma+i;
    }

    printf("La suma total de %d numeros es %d\n",NUM_SUM,suma);
    suma=0;
    while (cont<NUM_SUM)
    {
        suma=suma+cont;
        cont++;
    }
    printf("La suma total de %d numeros es %d",NUM_SUM,suma);
    
    
}
