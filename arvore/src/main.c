#include <stdio.h>
#include "../lib/arvore.h"
#include "../lib/evento.h"

int main() {
    Arvore arvore;
    plantar(&arvore);

    while (1) {
        Evento evento = ler_evento();

        if (evento == EVENTO_SAIR) {
            printf("👋 Programa encerrado.\n");
            break;
        }

        tratar_evento(&arvore, evento);
    }

    return 0;
}
