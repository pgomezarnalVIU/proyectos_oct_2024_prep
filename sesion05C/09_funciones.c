#include <stdio.h>
#define MAX_NUMERO 10

//Prototipos
void cambia(int a,int b);

int main(){
    int primerNumero=2;
    int segundoNumero=3;

    cambia(primerNumero,segundoNumero);

}

void cambia(int a,int b){
    int temp;
    temp=a;
    a=b;
    b=temp;
}