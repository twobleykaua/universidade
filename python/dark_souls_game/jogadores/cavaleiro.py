from jogadores.jogador import Jogador

class Cavaleiro(Jogador):
    def __init__(self, nome):
        super().__init__(nome)
        self.hp += 50
        self.ataque += 5