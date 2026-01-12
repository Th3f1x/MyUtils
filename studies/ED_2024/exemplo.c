#include <stdio.h>
#include <stdlib.h>

//cria o tipo de dado ArvoreNo
typedef struct arvNo ArvoreNo;              

//cria a estrutura de cada nó da árvore
struct arvNo                            
{
    char info;
    ArvoreNo* esquerda;
    ArvoreNo* direita;
};

//cria o tipo de dado Arvore
typedef struct arvore Arvore;           

//cria a estrutura da árvore apontando a raiz do nó
struct arvore
{
    ArvoreNo* raiz;
};

//função que cria o nó e insere o elemento
ArvoreNo* criarNo (char elemento, ArvoreNo* esq, ArvoreNo* dir){
    ArvoreNo* p = (ArvoreNo*) malloc(sizeof (ArvoreNo));            //p = ponteiro
    p->info = elemento;
    p->esquerda = esq;
    p->direita = dir;

    return p;
}

//função que cria e aponta para o nó raiz
Arvore* criarArvore (ArvoreNo* r){
    Arvore* a = (Arvore*) malloc(sizeof(Arvore));               //a = ponteiro
    a->raiz = r;

    return a;
}

//função que cria os nós e insere os elementos na árvore
/*Arvore* a = criarArvore(criarNo('a', 
                            criarNo('b', NULL, 
                                criarNo('d', NULL, NULL)
                            ),
                            criarNo('c',
                                    criarNo('e', NULL, NULL),
                                    criarNo('f', NULL, NULL)
                                    )
                            )
                        );*/

//função que exibe os elementos da árvore
static void imprime (ArvoreNo* r){
    if (r != NULL){
        printf("% c ", r->info);
        imprime(r->esquerda);
        imprime(r->direita);
    }
}

//função que imprime a árvore a partir da raiz
void imprimeArvore (Arvore* a){
    imprime(a->raiz);
}

//função que libera a memória
static void liberarMemoria (ArvoreNo* r){
    if (r != NULL){
        liberarMemoria(r->esquerda);
        liberarMemoria(r->direita);
        free(r);
    }
}

//função que libera a memoria da raiz
void liberarRaiz (Arvore* a){
    liberarMemoria(a->raiz);
    free(a);
}

//função que verifica se o elemento está na árvore
static int pertence (ArvoreNo* r, char c){
    if (r == NULL){
        return 0;
    }else{
        return c == r->info || pertence(r->esquerda, c) || pertence(r->direita, c);
    }
}

//função que verifica se o elemento é a raiz
int pertenceRaiz (Arvore* a, char c){
    return pertence(a->raiz, c);
}

//função que busca e apresenta o elemento
static ArvoreNo* buscaElemento (ArvoreNo* r, char c){
    if (r == NULL){
        return NULL;
    }else if (c == r->info){
        return r;
    }else{
        ArvoreNo* p = buscaElemento(r->esquerda, c);
        if (p != NULL){
            return p;
        }else{
            return buscaElemento(r->direita, c);
        }
    }    
}

//função que busca e apresenta o elemento no nó raiz
ArvoreNo* buscaRaiz (Arvore* a, char c){
    return buscaElemento(a->raiz, c);
}


