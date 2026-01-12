def processa_comentarios():
    resultados = {}
    
    while True:
        nome_usuario = input()
        if nome_usuario.lower() == 'fim':
            break
        
        comentario = input()
        
        ocorrencias = comentario.count('Joana')
        
        if ocorrencias > 0:
            resultado = 'Joana' * ocorrencias
        else:
            resultado = f"{nome_usuario} não fez comentário sobre a Joana"
        
        resultados[nome_usuario] = resultado
    
    for usuario, resultado in resultados.items():
        print(f"{usuario} -- {resultado}")


processa_comentarios()
