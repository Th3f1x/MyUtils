import os
import re
from PIL import Image
from PyPDF2 import PdfMerger

def converter_imagens_para_pdf(pasta_raiz):
    for raiz, subpastas, arquivos in os.walk(pasta_raiz):
        imagens = [f for f in arquivos if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

        if imagens:
            imagens_ordenadas = sorted(imagens)
            caminhos_completos = [os.path.join(raiz, img) for img in imagens_ordenadas]

            lista_imagens = []
            for caminho in caminhos_completos:
                try:
                    img = Image.open(caminho).convert('RGB')
                    lista_imagens.append(img)
                except Exception as e:
                    print(f"[!] Erro ao abrir imagem {caminho}: {e}")

            if lista_imagens:
                nome_pdf = os.path.basename(raiz) + '.pdf'
                caminho_pdf = os.path.join(raiz, nome_pdf)
                try:
                    lista_imagens[0].save(caminho_pdf, save_all=True, append_images=lista_imagens[1:])
                    print(f"[✓] PDF salvo: {caminho_pdf}")
                except Exception as e:
                    print(f"[!] Erro ao salvar PDF em {raiz}: {e}")

def extrair_numero_do_capitulo(nome_pasta):
    match = re.search(r'Chapter\s+(\d+)', nome_pasta, re.IGNORECASE)
    return int(match.group(1)) if match else float('inf')  # Se não encontrar, vai para o fim

def juntar_pdfs_de_subpastas(pasta_raiz, nome_pdf_final="resultado_final.pdf"):
    pdfs_encontrados = []

    for subpasta in os.listdir(pasta_raiz):
        caminho_subpasta = os.path.join(pasta_raiz, subpasta)
        if os.path.isdir(caminho_subpasta):
            for arquivo in os.listdir(caminho_subpasta):
                if arquivo.lower().endswith('.pdf'):
                    caminho_pdf = os.path.join(caminho_subpasta, arquivo)
                    numero = extrair_numero_do_capitulo(subpasta)
                    pdfs_encontrados.append((numero, caminho_pdf))

    # Ordena os PDFs com base no número do capítulo
    pdfs_ordenados = sorted(pdfs_encontrados, key=lambda x: x[0])

    if not pdfs_ordenados:
        print("[!] Nenhum PDF encontrado para juntar.")
        return

    try:
        merger = PdfMerger()
        for _, pdf in pdfs_ordenados:
            merger.append(pdf)
        caminho_saida = os.path.join(pasta_raiz, nome_pdf_final)
        merger.write(caminho_saida)
        merger.close()
        print(f"[✓] PDF final salvo em: {caminho_saida}")
    except Exception as e:
        print(f"[!] Erro ao juntar PDFs: {e}")

def menu():
    print("\n=== Menu ===")
    print("1 - Converter imagens em PDF")
    print("2 - Juntar todos os PDFs das subpastas em ordem de capítulo")
    print("0 - Sair")

    while True:
        opcao = input("Escolha uma opção: ").strip()
        if opcao in {"0", "1", "2"}:
            return opcao
        else:
            print("Opção inválida. Tente novamente.")

# --- Execução Principal ---
if __name__ == "__main__":
    pasta = input("Digite o caminho da pasta principal: ").strip()
    if not os.path.isdir(pasta):
        print("Caminho inválido.")
    else:
        escolha = menu()
        if escolha == "1":
            converter_imagens_para_pdf(pasta)
        elif escolha == "2":
            juntar_pdfs_de_subpastas(pasta)
        else:
            print("Saindo...")
