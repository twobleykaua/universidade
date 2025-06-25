from inimigos.inimigo import Inimigo

class Chefe(Inimigo):
    def __init__(self):
        super().__init__("Chefe Demoníaco", 200, 25)