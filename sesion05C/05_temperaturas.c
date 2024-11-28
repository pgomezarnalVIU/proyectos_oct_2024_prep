/*
* PROGRAMA DE TEMPERATURAS
Buscando en Internet, crear un pequeño problema que genere 1 números aleatorios entre 0 y 45, representando temperaturas. Sacaremos un mensaje dependiendo de la temperatura obtenida:
0 a 10, Hace mucho frio
11 a 20, Hace fresquito
21 a 30, No se está mal 
31 a 40, Comienza a hacer calor
41 a 45, Muero achicharrado

*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h> /* Nueva librería necesaria para la función srand */

void main(){
    int temperatura;

    srand(time(NULL)); //Generamos número aleatorio en base al tiempo
    //Obtener un nuemero aleatorio entre N y M
    temperatura = rand () % 46;

    printf("La temperatura que me da el sensor es: %d\n",temperatura);

    //Comprobacion
    if(temperatura>=0 && temperatura<=20){
        printf("HACE MUCHO FRIO");
    }else if(temperatura>=21 && temperatura<=30){
        printf("HACE FRESQUITO");
    }else{
        printf("RESTO");
    }

}