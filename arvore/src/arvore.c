#include <stdio.h>
#include <string.h>
#include "../lib/arvore.h"
#include "../lib/evento.h"

void plantar(Arvore* a) {
    a->fase = SEMENTE;
    a->dados.semente.umidade = 0.0f;
    printf("🌱 Uma semente foi plantada.\n");
}

void evoluir(Arvore* a) {
    switch (a->fase) {
        case SEMENTE:
            if (a->dados.semente.umidade >= 10.0f) {
                a->fase = BROTO;
                a->dados.broto.altura = 0.5f;
                printf("🌿 A semente virou um broto!\n");
            } else {
                printf("⚠️ Umidade insuficiente para germinar.\n");
            }
            break;

        case BROTO:
            printf("✅ O broto já está em sua fase final.\n");
            break;

        case MORTA:
            printf("☠️ A árvore está morta. Evolução impossível.\n");
            break;
    }
}


void tratar_evento(Arvore* a, Evento evento) {
    switch (evento) {
        case EVENTO_REGA:
            if (a->fase == SEMENTE) {
                a->dados.semente.umidade += 5.0f;
                printf("💧 Semente regada. Umidade: %.1f\n", a->dados.semente.umidade);
            } else {
                printf("💧 A árvore não é mais uma semente.\n");
            }
            break;

        case EVENTO_EVOLUIR:
            evoluir(a);
            break;

        case EVENTO_QUEIMAR:
            a->fase = MORTA;
            strcpy(a->dados.morta.motivo, "Incêndio");
            printf("🔥 A árvore morreu por incêndio.\n");
            break;

        case EVENTO_INVALIDO:
            printf("⚠️ Evento inválido.\n");
            break;

        case EVENTO_SAIR:
            // Sinal para encerrar (tratado no main)
            break;
    }
}

