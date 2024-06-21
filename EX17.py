class Musica:
    musicas: []

    def __init__(self, nome, artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao

    def __str__(self):
        return f'{self.nome} | {self.artista} | {self.duracao}'
    
    def listar_musicas():
        for musica in Musica.musicas:
            print(f'{musica.nome}|{musica.artista}|{musica.duracao}')

musica_elvis = Musica('Elvis Presley', 'Rock', '10')
musica_frank = Musica('Frank Sinatra', 'Blues', '15')

Musica.listar_musicas()