
# Exercício Impressão - Estrutura de Dados - CIC UNB 2024

import os

class Impressao:
    def __init__(self, nome, conteudo, paginas):
        self.nome = nome
        self.conteudo = conteudo
        self.paginas = paginas

class No:
    def __init__(self, impressao):
        self.impressao = impressao
        self.proximo = None

class Fila:
    def __init__(self):
        self.cabeca = None
        self.cauda = None

    def adicionar(self, impressao):
        novo_no = No(impressao)
        if not self.cabeca:
            self.cabeca = novo_no
            self.cauda = novo_no
        else:
            self.cauda.proximo = novo_no
            self.cauda = novo_no

    def processar(self):
        if self.cabeca:
            impressao = self.cabeca.impressao
            self.cabeca = self.cabeca.proximo
            if not self.cabeca:
                self.cauda = None
            print(f"Processando impressão: {impressao.nome} com {impressao.paginas} páginas.")
        else:
            print("Não há impressões na fila.")

    def listar(self):
        atual = self.cabeca
        if not atual:
            print("A fila está vazia.")
            return
        print("Estado atual da fila:")
        while atual:
            impressao = atual.impressao
            print(f"Nome: {impressao.nome}, Conteúdo: {impressao.conteudo}, Páginas: {impressao.paginas}")
            atual = atual.proximo


def clear_term():
    os.system('cls' if os.name == 'nt' else 'clear')



def main():
    fila = Fila()
    while True:
        print("\nMenu:")
        print("1 - Adicionar pedido de impressão")
        print("2 - Processar pedido de impressão")
        print("3 - Listar estado atual da fila")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")
        clear_term()

        if opcao == '1':
            nome = input("Digite o nome do documento: ")
            conteudo = input("Digite o conteúdo do documento: ")
            paginas = int(input("Digite o número de páginas: "))
            impressao = Impressao(nome, conteudo, paginas)
            fila.adicionar(impressao)
            print("Impressão adicionada à fila")
        elif opcao == '2':
            fila.processar()

        elif opcao == '3':
            fila.listar()
        elif opcao == '0':
            print("User cancel the operation")
            break
        else:
            print("Opção inválida")

if __name__ == "__main__":
    main()
