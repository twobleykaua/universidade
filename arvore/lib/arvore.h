#ifndef ARVORE_H
#define ARVORE_H

#include "evento.h"

typedef enum {
    SEMENTE,
    BROTO,
    MORTA
} FaseArvore;

typedef struct Arvore {
    FaseArvore fase;
    union {
        struct { float umidade; int dias_no_solo; } semente;
        struct { float altura; } broto;
        struct { char motivo[100]; } morta;
    } dados;
} Arvore;

// ✅ Use "struct Arvore*" para bater com a declaração em evento.h
void plantar(struct Arvore* a);
void evoluir(struct Arvore* a);
void tratar_evento(struct Arvore* a, Evento evento);

#endif
