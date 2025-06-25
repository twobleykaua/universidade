from inimigos.inimigo import Inimigo

class MortoVivo(Inimigo):
    def __init__(self):
        super().__init__("Morto-Vivo", 50, 10)