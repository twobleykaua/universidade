#include <stdio.h>


// int main(int argc,char *argv[])
// {
//   for(int i=0; i <argc; i++){
//      printf("Arg[%i] %s\n", i, argv[i]);

//   }
//     return 0;
// }


// float inTofloat(int n){
//     float new = (float)n;
//     return new;

// }

// void halfConvert(int n){
//     float num = inTofloat(n);
//     float half = num * 0.5;
//      printf("metade: %.2f\n" , half);
// }




// void menu(){
//     int i = 100;
//     printf("numero: %i\n" , i);
//     halfConvert(100);
//     printf("==================================\n\n\n\n\n");
// }

// int main()
// {
//      menu();
//     return 0;
// }

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#define MAX_STR 50

typedef struct 
{
    char name[MAX_STR];
    float power;
    int lives;
    bool alive;
} player;

void imprimePlayer(player *p){
    printf("===GAME OVER=====\n");
    printf("%s\n", p->name);
    printf("%.4f\n", p->power);
    printf("%d\n", p->lives);
    printf("%i\n", p->alive);
    printf("===================\n");
}

int main(){
player p1 = {
    .name = "brunão",
    .power = 1500.0,
    .lives = 5,
    .alive = true
};
imprimePlayer(&p1);
return 0;
}