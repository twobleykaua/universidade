class Inimigo:
    def __init__(self, nome, hp, ataque):
        self.nome = nome
        self.hp = hp
        self.ataque = ataque

    def atacar(self, jogador):
        jogador.receber_dano(self.ataque)

    def receber_dano(self, dano):
        self.hp -= dano
        print(f"{self.nome} sofreu {dano} de dano. HP: {self.hp}")