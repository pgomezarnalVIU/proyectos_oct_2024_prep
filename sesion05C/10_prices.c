/*
Encontrar el precio más alto dentro de un array de cien números 
y aplicarle un 10% de descuento

 */

#include <stdio.h>
#include <stdlib.h>
#include <time.h> /* Nueva librería necesaria para la función srand */

#define MAX_PRICES 100

void imprime_precios(int precios[]);
int busca_pos_max(int precios[]);

int main(){
    //Array de precios
    int precios[MAX_PRICES];
    int max_pos_price;

    srand(time(NULL)); //Generamos número aleatorio en base al tiempo
    
    //Inicialización aleatoria
    for (int i = 0; i < MAX_PRICES; i++)
    {
        precios[i] = rand () % (1500-10+1) + 10;  
    }
    imprime_precios(precios);
    //Busca el máximo
    max_pos_price=busca_pos_max(precios);
    //Imprime
    printf("------\n");
    printf("El maximo precio es %d, aplicado el descuenso es %f\n",precios[max_pos_price],precios[max_pos_price]*0.9);

}

void imprime_precios(int precios[]){
    for (int i = 0; i < MAX_PRICES; i++)
    {
        printf("%d",precios[i]);
        if((i+1)%5!=0) printf(",");
        else printf("\n");
    }
    
}

int busca_pos_max(int precios[]){
    int max=0,pos_max=0;
    for (int i = 0; i < MAX_PRICES; i++)
    {
        if(precios[i]>max){
            max=precios[i];
            pos_max=i;
        }
    }
    return pos_max;
    
}