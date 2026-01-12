import json
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def ler_textos():
    print("Digite o texto na língua estrangeira (pressione Enter em uma linha vazia para finalizar):")
    texto_estrangeiro = []
    while True:
        linha = input()
        if linha == "":
            break
        texto_estrangeiro.append(linha.strip())
    
    print("Digite o texto traduzido para o português (pressione Enter em uma linha vazia para finalizar):")
    texto_traduzido = []
    while True:
        linha = input()
        if linha == "":
            break
        texto_traduzido.append(linha.strip())

    clear_console()
    
    return texto_estrangeiro, texto_traduzido

def associar_frases(texto_estrangeiro, texto_traduzido):
    associacoes = []
    
    for i, (linha_estrangeira, linha_traduzida) in enumerate(zip(texto_estrangeiro, texto_traduzido)):
        associacoes.append({
            "id": i,
            "translation": {
                "pt": linha_traduzida,
                "tca": linha_estrangeira
            }
        })
    
    return associacoes

def mostrar_traducao(associacoes):
    print("Escolha um número para ver a tradução correspondente:")
    while True:
        try:
            escolha = int(input("Digite o número da frase (ou digite -1 para sair): "))
            if escolha == -1:
                break

            clear_console()
            frase = associacoes[escolha]
            print(f"Frase em tca: {frase['translation']['tca']}")
            print(f"Tradução em pt: {frase['translation']['pt']}")

        except (ValueError, IndexError):
            print("Número inválido. Tente novamente.")

def exportar_json(associacoes):
    with open('traducao.json', 'w', encoding='utf-8') as arquivo_json:
        json.dump(associacoes, arquivo_json, ensure_ascii=False, indent=4)
    print("Traduções exportadas para 'traducao.json'.")


def main():
    texto_estrangeiro, texto_traduzido = ler_textos()
    associacoes = associar_frases(texto_estrangeiro, texto_traduzido)
    
    while True:
        clear_console()
        print("\n1. Mostrar tradução de uma frase")
        print("2. Exportar traduções para JSON")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            mostrar_traducao(associacoes)
        elif escolha == "2":
            exportar_json(associacoes)
        elif escolha == "3":
            break
        else:
            print("Opção inválida. Tente novamente.")


main()