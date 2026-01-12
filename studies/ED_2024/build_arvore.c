
// Nome: Guilherme Rafael Cannavan Oliveira
// Matrícula: 241022488

#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node* esquerda;
    struct Node* direita;
} Node;

// Função para criar um novo nó
Node* criarno(int data) {
    Node* novono = (Node*)malloc(sizeof(Node));
    novono->data = data;
    novono->esquerda = NULL;
    novono->direita = NULL;
    return novono;
}



// Função para inserir um elemento na árvore
Node* inserir(Node* raiz, int data) {
    if (raiz == NULL) {
        return criarno(data);
    }
    if (data < raiz->data) {
        raiz->esquerda = inserir(raiz->esquerda, data);
    } else if (data > raiz->data) {
        raiz->direita = inserir(raiz->direita, data);
    }
    return raiz;
}



// Função para encontrar o nó com o valor mínimo
Node* valormin(Node* node) {
    Node* current = node;
    while (current && current->esquerda != NULL) {
        current = current->esquerda;
    }
    return current;
}



// Função para remover um elemento da árvore
Node* deletarno(Node* raiz, int data) {
    if (raiz == NULL) {
        return raiz;
    }
    if (data < raiz->data) {
        raiz->esquerda = deletarno(raiz->esquerda, data);
    } else if (data > raiz->data) {
        raiz->direita = deletarno(raiz->direita, data);
    } else {
        if (raiz->esquerda == NULL) {
            Node* temp = raiz->direita;
            free(raiz);
            return temp;
        } else if (raiz->direita == NULL) {
            Node* temp = raiz->esquerda;
            free(raiz);
            return temp;
        }
        Node* temp = valormin(raiz->direita);
        raiz->data = temp->data;
        raiz->direita = deletarno(raiz->direita, temp->data);
    }
    return raiz;
}

// Função para imprimir a árvore em ordem
void ordemcrescente(Node* raiz) {
    if (raiz != NULL) {
        ordemcrescente(raiz->esquerda);
        printf("%d ", raiz->data);
        ordemcrescente(raiz->direita);
    }
}

// Função para contar o número total de nós
int contarno(Node* raiz) {
    if (raiz == NULL) {
        return 0;
    }
    return 1 + contarno(raiz->esquerda) + contarno(raiz->direita);
}

// Função para contar o número total de folhas
int contarfolha(Node* raiz) {
    if (raiz == NULL) {
        return 0;
    }
    if (raiz->esquerda == NULL && raiz->direita == NULL) {
        return 1;
    }
    return contarfolha(raiz->esquerda) + contarfolha(raiz->direita);
}

// Função para calcular a altura da árvore
int altura(Node* raiz) {
    if (raiz == NULL) {
        return 0;
    }
    int alturaesquerda = altura(raiz->esquerda);
    int alturadireta = altura(raiz->direita);
    return (alturaesquerda > alturadireta) ? (alturaesquerda + 1) : (alturadireta + 1);
}

// Função para verificar se a árvore é própria ou imprópria
void propriaouimpropria(Node* raiz) {
    int totalNo = contarno(raiz);
    int totalfolhas = contarfolha(raiz);
    int nointerno = totalNo - totalfolhas;

    if (nointerno == totalfolhas) {
        printf("A árvore é própria.\n");
    } else {
        printf("A árvore é imprópria.\n");
    }
}



int main() {
    Node* raiz = NULL;
    raiz = inserir(raiz, 50);
    inserir(raiz, 30);
    inserir(raiz, 20);
    inserir(raiz, 40);
    inserir(raiz, 70);
    inserir(raiz, 60);
    inserir(raiz, 80);

    printf("Árvore em ordem: ");
    ordemcrescente(raiz);
    printf("\n");

    printf("Total de nós: %d\n", contarno(raiz));
    printf("Total de folhas: %d\n", contarfolha(raiz));
    printf("Altura da árvore: %d\n", altura(raiz));
    propriaouimpropria(raiz);

    printf("Removendo o nó 20\n");
    raiz = deletarno(raiz, 20);
    printf("Árvore em ordenada após remoção: ");
    ordemcrescente(raiz);
    printf("\n");

    return 0;
}