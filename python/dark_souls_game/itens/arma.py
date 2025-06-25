from itens.item import Item

class Arma(Item):
    def __init__(self, nome, dano):
        super().__init__(nome, "Arma de ataque")
        self.dano = dano