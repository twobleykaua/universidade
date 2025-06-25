from itens.item import Item

class Pocao(Item):
    def __init__(self, nome, cura):
        super().__init__(nome, "Poção de cura")
        self.cura = cura