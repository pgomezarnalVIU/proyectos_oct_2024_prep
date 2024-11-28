/*
    CONVERSION FAH CEL
 */


#include <stdio.h>
#include <stdlib.h>
#include <time.h> /* Nueva librería necesaria para la función srand */

int main(){
    float celsius,fahr;
    int min,max,paso;

    int num_temperaturas=0;
    int temperatura;

    srand(time(NULL)); //Generamos número aleatorio en base al tiempo


    //Inicializacion
    min=0;
    max=300;
    paso=20;

    fahr=min;
    celsius=min;

    while(fahr<=max){
        celsius=5*(fahr-32)/9;
        printf("Conversion temp ºF:%.2f ºC:%.2f\n",fahr,celsius);
        fahr=fahr+paso;
    }

    while(num_temperaturas<=24){
        //Obtener un nuemero aleatorio entre N y M
        temperatura = rand () % 15;
        printf("Temperatura %d",temperatura);
        if(temperatura>=10){
            printf("LA CAMARA SE DESCOGELA");
            break;
        }
        num_temperaturas++;
    }

}