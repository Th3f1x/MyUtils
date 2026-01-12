def main():
    comentarios_joana = 0
    usuarios_comentarios = {}

    while True:
        nome_usuario = input("Nome do usuário (ou 'fim' para encerrar): ")
        if nome_usuario.lower() == 'fim':
            break
        
        comentario = input("Comentário: ")
        
        if 'joana' in comentario.lower():
            if nome_usuario not in usuarios_comentarios:
                usuarios_comentarios[nome_usuario] = 0
            usuarios_comentarios[nome_usuario] += 1
            comentarios_joana += 1
            print(f"{nome_usuario} fez comentário sobre a Joana")
        else:
            print(f"{nome_usuario} não fez comentário sobre a Joana")
    
    print(f"Comentários sobre Joana: {comentarios_joana}")

if __name__ == "__main__":
    main()


