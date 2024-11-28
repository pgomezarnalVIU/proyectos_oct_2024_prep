/*
    EJEMPLO DE SCAN

 */
#include <stdio.h>


int main(void)
{
  char cadena[80];
  int entero1, entero2;
  float decimal;
  printf("Introduce dos enteros separados por un espacio: \n");
  //entero1 en una variable
  //&entero1 es la direccion a la memoria de entero1
  scanf("%d %d", &entero1, &entero2);
  printf("Introduce un número decimal:\n");
  scanf("%f", &decimal);
  printf("Introduce una cadena:\n");
  //cadena es una direccion de memoria
  //cadena[0] es el valor de la primera posicion
  scanf("%s",cadena);
  printf("Esto es todo lo que has escrito:\n");
  printf("%d %d %f %s\n",entero1,entero2,decimal,cadena);
  return 0;
}
