
class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def dar_likes(self):
        self._likes += 1

    def imprime(self):
        print(f' - Nome: {self._nome}' +
              f'\n - Ano: {self.ano}' +
              f'\n - Likes: {self._likes}' +
              f'\n -------------')

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def imprime(self):
        print(f' - Nome: {self._nome}' +
              f'\n - Ano: {self.ano}' +
              f'\n - Duração (minutos): {self.duracao}' +
              f'\n - Likes: {self._likes}' +
              f'\n -------------')

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def imprime(self):
        print(f' - Nome: {self._nome}' +
              f'\n - Ano: {self.ano}' +
              f'\n - Temporadas: {self.temporadas}' +
              f'\n - Likes: {self._likes}' +
              f'\n -------------')

#Execução
vingadores = Filme('vingadores', 2018, 160)
vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()

atlanta = Serie('Atlanta', 2020, 2)
atlanta.dar_likes()


playlist = [vingadores, atlanta]

for i in playlist:
    i.imprime()
