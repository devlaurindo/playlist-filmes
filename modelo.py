#CLASSE PROGRAMA COM LIKE E NOME COMO PROPRIEDADES PARA QUE NAO TENHA ALTERAÇÃO
class Programa:

    def __init__(self, nome, ano):
            self._nome = nome.title()
            self.ano = ano
            self._likes = 0


    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    # PARA SABER IMPRIMIR OS DETALHES DE FILMES E SERIE SOZINHOS
    # __str__ REPRESENTANDO UMA EXPRESSAO TEXTUAL PARA O OBJ
    def __str__(self):
        return f'{self._nome} - {self.ano} - {self._likes} Likes'

# CLASSE SOBRE FILME COM HERANÇA DA CLASSE PROGRAMA
class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    # __str__ REPRESENTANDO UMA EXPRESSAO TEXTUAL PARA O OBJ
    def __str__(self):
            return f'{self._nome} - {self.ano} - {self.duracao} min - {self._likes} Likes'

# CLASSE SOBRE SERIE COM HERANÇA DA CLASSE PROGRAMA
class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

#CLASSE PLAYLIST QUE VAI LISTAR SERIES E FILMES
class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    def __len__(self):
        return len(self._programas)


    # __str__ REPRESENTANDO UMA EXPRESSAO TEXTUAL PARA O OBJ
    def __str__(self):
            return f'{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes} Likes'

# DETALHES SOBRE O FILME
vingadores = Filme ('vingadores - guerra infinita', 2018, 160)
atlanta = Serie ('atlanta', 2018, 2)
tmep = Filme ('todo mundo em panico', 1999, 100)
demolidor = Serie ('demolidor', 2016, 2)


vingadores.dar_like()
vingadores.dar_like()
tmep.dar_like()
tmep.dar_like()
demolidor.dar_like()
demolidor.dar_like()
atlanta.dar_like()
atlanta.dar_like()

#POLIMORFISMO PARA EXECUTAR FUNÇÃO FILME E SERIE SEPARADAMENTE DE FORMA CORRETA
filmes_e_series = [vingadores, atlanta, tmep, demolidor]
playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

print(f'Tamanho do playlist: {len(playlist_fim_de_semana)}')

for programa in playlist_fim_de_semana:
    print(programa)
