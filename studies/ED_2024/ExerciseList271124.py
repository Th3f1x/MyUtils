
#  Exercício PlayList - Estrutura de Dados - CIC UNB 2024

class Musica:
    def __init__(self, nome, artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao 

    def __str__(self):
        return f"{self.nome} - {self.artista} ({self.duracao // 60}:{self.duracao % 60:02})"


class No:
    def __init__(self, musica):
        self.musica = musica
        self.anterior = None
        self.proximo = None


class Playlist:
    def __init__(self):
        self.cabeca = None
        self.cauda = None

    def adicionar_ao_fim(self, musica):
        novo_no = No(musica)
        if not self.cabeca:
            self.cabeca = self.cauda = novo_no
        else:
            self.cauda.proximo = novo_no
            novo_no.anterior = self.cauda
            self.cauda = novo_no

    def adicionar_em_posicao(self, musica, posicao):
        novo_no = No(musica)
        if posicao == 0:
            novo_no.proximo = self.cabeca
            if self.cabeca:
                self.cabeca.anterior = novo_no
            self.cabeca = novo_no
            if not self.cauda:
                self.cauda = novo_no
        else:
            atual = self.cabeca
            for _ in range(posicao - 1):
                if not atual.proximo:
                    break
                atual = atual.proximo
            novo_no.proximo = atual.proximo
            novo_no.anterior = atual
            if atual.proximo:
                atual.proximo.anterior = novo_no
            atual.proximo = novo_no
            if not novo_no.proximo:
                self.cauda = novo_no

    def deletar_pelo_nome(self, nome):
        atual = self.cabeca
        while atual:
            if atual.musica.nome == nome:
                if atual.anterior:
                    atual.anterior.proximo = atual.proximo
                if atual.proximo:
                    atual.proximo.anterior = atual.anterior
                if atual == self.cabeca:
                    self.cabeca = atual.proximo
                if atual == self.cauda:
                    self.cauda = atual.anterior
                return True
            atual = atual.proximo
        return False

    def apresentar_playlist(self):
        atual = self.cabeca
        while atual:
            print(atual.musica)
            atual = atual.proximo

    def encontrar_musica(self, nome):
        atual = self.cabeca
        while atual:
            if atual.musica.nome == nome:
                return str(atual.musica)
            atual = atual.proximo
        return "Música não encontrada"

    def duracao_total(self):
        total = 0
        atual = self.cabeca
        while atual:
            total += atual.musica.duracao
            atual = atual.proximo
        return f"{total // 60}:{total % 60:02}"


# Some tests for correction of bugs.
# Perhaps, i create a interface for this, by the moment its just "hardcoded".

# playlist = Playlist()
# playlist.adicionar_ao_fim(Musica("Mulher de Fases", "Raimundos", 199))
# playlist.adicionar_ao_fim(Musica("Buddy Holly", "Weezer", 144))
# playlist.adicionar_em_posicao(Musica("Kids", "Current Joys", 257), 1)
# playlist.apresentar_playlist()
# print("\nEncontrar música 'Buddy Holly':", playlist.encontrar_musica("Buddy Holly"))
# print("Duração total da playlist:", playlist.duracao_total())
# playlist.deletar_pelo_nome("Kids")
# print("\nApós deletar 'Kids':")
# playlist.apresentar_playlist()
