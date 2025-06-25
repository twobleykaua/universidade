class NPC:
    def __init__(self, nome, dialogo):
        self.nome = nome
        self.dialogo = dialogo

    def falar(self):
        print(f"{self.nome}: {self.dialogo}")