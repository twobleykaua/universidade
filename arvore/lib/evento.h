#ifndef EVENTO_H
#define EVENTO_H

typedef enum {
    EVENTO_REGA,
    EVENTO_EVOLUIR,
    EVENTO_QUEIMAR,
    EVENTO_SAIR,
    EVENTO_INVALIDO
} Evento;

// 👇 Solução: declaração antecipada da struct Arvore
struct Arvore;

Evento ler_evento();
void tratar_evento(struct Arvore* a, Evento evento);

#endif
