#include <stdio.h>

/*Variables*/
int main(){
    //DEfinicion de var
    int a=10,b=34; 

    if (a>b) { 
        b--; 
        a=a+5; 
    } else { 
        a++; 
        b=b-5; 
    } 
    if (b-a!=7) b=5;

}