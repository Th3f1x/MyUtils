def lista_usuarios_comentarios():
    usuarios_joana = []
    
    while True:
        nome_usuario = input().strip()
        if nome_usuario.lower() == 'fim':
            break
        
        comentario = input().strip()
        

        ocorrencias = comentario.lower().count('joana')
        
        if ocorrencias > 0:
            usuarios_joana.append(nome_usuario)
    
    print(*usuarios_joana)


lista_usuarios_comentarios()
