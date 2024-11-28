#include <stdio.h>


// Prototype required by standard
int get_menu_choice(void);


void main(void)
{
    int choice;
    // Call get_menu_choice() function
    choice = get_menu_choice();
    printf("You have chosen Menu #%d\n", choice);
    printf("\n");
}

int get_menu_choice(void){
    int selection = 0;

    do{
        printf("1 - Add a record");
        printf("\n2 - Change a record");
        printf("\n3 - Delete a record");
        printf("\n4 - Quit");
        printf("\nEnter a selection: ");
        /* scanf("%d", &selection ); */

        scanf("%d", &selection);
    } while ((selection < 1) || (selection > 4));

    return selection;

}

 