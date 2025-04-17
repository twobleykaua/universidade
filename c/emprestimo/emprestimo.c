#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>

#define MAX_EMPRESTIMOS 3
#define TAM_STR 100
#define QTD_LIVROS 3
#define MAX_PESSOAS 10

#define COR_RESET     "\033[0m"
#define COR_VERDE     "\033[1;32m"
#define COR_VERMELHO  "\033[1;31m"
#define COR_CYAN      "\033[1;36m"
#define COR_AMARELO   "\033[1;33m"

typedef enum {
    DISPONIVEL,
    EMPRESTADO
} StatusLivro;

typedef struct {
    char autor[TAM_STR];
    char titulo[TAM_STR];
    int total_emprestimos;
    StatusLivro status;
} Livro;

typedef struct {
    char nome_pessoa[TAM_STR];
    char titulo_livro[TAM_STR];
    char data[TAM_STR];
    char hora[TAM_STR];
} Emprestimo;

const char* statusParaString(StatusLivro status) {
    return status == DISPONIVEL ? "Disponível" : "Emprestado";
}

void limparTela() {
    system("clear || cls");
}

void pegarDataHora(char *dataStr, char *horaStr) {
    time_t agora = time(NULL);
    struct tm *info = localtime(&agora);
    strftime(dataStr, TAM_STR, "%d/%m/%Y", info);
    strftime(horaStr, TAM_STR, "%H:%M:%S", info);
}

void inicializarLivro(Livro *livro, const char *autor, const char *titulo) {
    strcpy(livro->autor, autor);
    strcpy(livro->titulo, titulo);
    livro->total_emprestimos = 0;
    livro->status = DISPONIVEL;
}

void listarLivros(Livro livros[], int qtd) {
    printf(COR_CYAN "\nLista de Livros:\n" COR_RESET);
    for (int i = 0; i < qtd; i++) {
        printf("%d. \"%s\" por %s [%s] (Total de empréstimos: %d)\n",
               i + 1, livros[i].titulo, livros[i].autor,
               statusParaString(livros[i].status),
               livros[i].total_emprestimos);
    }
}

void emprestarLivro(Livro livros[], Emprestimo emprestimos[], int *qtd_emprestimos) {
    limparTela();

    if (*qtd_emprestimos >= MAX_PESSOAS) {
        printf(COR_VERMELHO "Limite de cadastros atingido.\n" COR_RESET);
        return;
    }

    char nome[TAM_STR];
    printf(COR_AMARELO "Digite o nome da pessoa que está pegando o livro: " COR_RESET);
    getchar(); // limpar buffer
    fgets(nome, TAM_STR, stdin);
    nome[strcspn(nome, "\n")] = '\0';

    listarLivros(livros, QTD_LIVROS);
    int escolha;
    printf(COR_AMARELO "Escolha o número do livro: " COR_RESET);
    scanf("%d", &escolha);
    escolha--;

    if (escolha < 0 || escolha >= QTD_LIVROS) {
        printf(COR_VERMELHO "Livro inválido!\n" COR_RESET);
        return;
    }

    Livro *livro = &livros[escolha];

    if (livro->total_emprestimos >= MAX_EMPRESTIMOS) {
        printf(COR_VERMELHO "O livro \"%s\" esgotou na biblioteca!\n" COR_RESET, livro->titulo);
        return;
    }

    if (livro->status == EMPRESTADO) {
        printf(COR_VERMELHO "O livro \"%s\" já está emprestado.\n" COR_RESET, livro->titulo);
        return;
    }

    char data[TAM_STR], hora[TAM_STR];
    pegarDataHora(data, hora);

    livro->status = EMPRESTADO;
    livro->total_emprestimos++;

    strcpy(emprestimos[*qtd_emprestimos].nome_pessoa, nome);
    strcpy(emprestimos[*qtd_emprestimos].titulo_livro, livro->titulo);
    strcpy(emprestimos[*qtd_emprestimos].data, data);
    strcpy(emprestimos[*qtd_emprestimos].hora, hora);

    (*qtd_emprestimos)++;

    printf(COR_VERDE "\nLivro emprestado com sucesso!\n" COR_RESET);
    printf("Título: %s\n", livro->titulo);
    printf("Pessoa: %s\n", nome);
    printf("Data: %s - Hora: %s\n", data, hora);
    printf("Total de empréstimos: %d (Limite: 3)\n", livro->total_emprestimos);
}

void listarEmprestimos(Emprestimo emprestimos[], int qtd) {
    limparTela();
    printf(COR_CYAN "\n--- PESSOAS COM LIVROS EMPRESTADOS ---\n" COR_RESET);
    if (qtd == 0) {
        printf("Nenhum empréstimo registrado.\n");
        return;
    }
    for (int i = 0; i < qtd; i++) {
        printf("%d. %s pegou \"%s\" em %s às %s\n", i + 1,
               emprestimos[i].nome_pessoa,
               emprestimos[i].titulo_livro,
               emprestimos[i].data,
               emprestimos[i].hora);
    }
}

void devolverLivro(Livro livros[], Emprestimo emprestimos[], int *qtd_emprestimos) {
    limparTela();

    if (*qtd_emprestimos == 0) {
        printf(COR_VERMELHO "Não há livros emprestados.\n" COR_RESET);
        return;
    }

    listarEmprestimos(emprestimos, *qtd_emprestimos);

    int escolha;
    printf(COR_AMARELO "\nEscolha o número da pessoa que irá devolver o livro: " COR_RESET);
    scanf("%d", &escolha);
    escolha--;

    if (escolha < 0 || escolha >= *qtd_emprestimos) {
        printf(COR_VERMELHO "Escolha inválida!\n" COR_RESET);
        return;
    }

    char titulo[TAM_STR];
    strcpy(titulo, emprestimos[escolha].titulo_livro);

    // Atualizar status do livro
    for (int i = 0; i < QTD_LIVROS; i++) {
        if (strcmp(livros[i].titulo, titulo) == 0) {
            livros[i].status = DISPONIVEL;
            break;
        }
    }

    printf(COR_VERDE "Livro \"%s\" devolvido por %s.\n" COR_RESET,
           emprestimos[escolha].titulo_livro,
           emprestimos[escolha].nome_pessoa);

    // Remover empréstimo da lista
    for (int i = escolha; i < *qtd_emprestimos - 1; i++) {
        emprestimos[i] = emprestimos[i + 1];
    }
    (*qtd_emprestimos)--;
}

int main() {
    Livro livros[QTD_LIVROS];
    Emprestimo emprestimos[MAX_PESSOAS];
    int qtd_emprestimos = 0;
    int opcao;

    inicializarLivro(&livros[0], "Jorge Amado", "Capitães da Areia");
    inicializarLivro(&livros[1], "J.R.R. Tolkien", "O Senhor dos Anéis");
    inicializarLivro(&livros[2], "Machado de Assis", "Dom Casmurro");

    do {
        limparTela();
        printf(COR_CYAN "\n====== BEM VINDO ======\n" COR_RESET);
        printf("1. Emprestar um livro\n");
        printf("2. Devolver um livro\n");
        printf("3. Listar todos os livros\n");
        printf("4. Ver empréstimos ativos\n");
        printf("0. Sair\n");
        printf(COR_AMARELO "Escolha uma opção: " COR_RESET);
        scanf("%d", &opcao);

        switch (opcao) {
            case 1:
                emprestarLivro(livros, emprestimos, &qtd_emprestimos);
                break;
            case 2:
                devolverLivro(livros, emprestimos, &qtd_emprestimos);
                break;
            case 3:
                limparTela();
                listarLivros(livros, QTD_LIVROS);
                break;
            case 4:
                listarEmprestimos(emprestimos, qtd_emprestimos);
                break;
            case 0:
                printf(COR_CYAN "\nEncerrando o programa. Até logo!\n" COR_RESET);
                 printf(COR_VERDE "\n=======================================\n" COR_RESET);
                printf(COR_AMARELO "    Desenvolvido por Kauã e Vitor\n" COR_RESET);
                printf(COR_VERDE "=======================================\n" COR_RESET);
                break;
            default:
                printf(COR_VERMELHO "Opção inválida!\n" COR_RESET);
        }

        if (opcao != 0) {
            printf(COR_AMARELO "\nPressione ENTER para continuar..." COR_RESET);
            getchar();
            getchar();
        }

    } while (opcao != 0);

    return 0;
}
