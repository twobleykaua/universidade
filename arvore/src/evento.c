#include <stdio.h>
#include "../lib/evento.h"

Evento ler_evento() {
    char input;
    printf("\n[ e ] Evoluir  |  [ r ] Regar  |  [ q ] Queimar  |  [ x ] Sair\n> ");
    scanf(" %c", &input);

    switch (input) {
        case 'r': return EVENTO_REGA;
        case 'e': return EVENTO_EVOLUIR;
        case 'q': return EVENTO_QUEIMAR;
        case 'x': return EVENTO_SAIR;
        default:  return EVENTO_INVALIDO;
    }
}
