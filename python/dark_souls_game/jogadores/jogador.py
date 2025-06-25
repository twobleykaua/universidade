class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.hp = 100
        self.ataque = 10
        self.inventario = []
    
    def atacar(self, inimigo):
        inimigo.receber_dano(self.ataque)

    def receber_dano(self, dano):
        self.hp -= dano
        print(f"{self.nome} recebeu {dano} de dano. HP: {self.hp}")