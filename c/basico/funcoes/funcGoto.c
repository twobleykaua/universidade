#include <stdio.h>
#include <stdlib.h>
#include"lib/clear.h"

int main()
{
    int numero;
    
    clear2();
    printf("Digite um número: ");
    scanf("%d", &numero);

    if (numero < 0)
    {
        goto NEGATIVO;
    }
    else if (numero > 0)
    {
        goto POSITIVO;
    }
    else
    {
        goto ZERO;
    }

NEGATIVO:
 
    printf("O número [%d] é negativo.\n", numero);
    goto FIM;

POSITIVO:
   
    printf("O número [%d] é positivo.\n", numero);
    goto FIM;

ZERO:
   
    printf("Você inseriu o número ZERO.\n");
    goto FIM;

FIM:
printf("Fim do programa.\n");

    return 0;
}