
class Player:
    host = "localhost:8080" # Global
    # inicializador do objeto
    # passando valores posicionais
    def_init_(self, nome, arma):
        self.nome = nome # autoriza modificação/objeto
        self.arma = arma 


kratos: Player = Player("kratos", "Lâminas do caos")

Hades: Player = Player("Hades", "Stygius")
print(kratos.nome, kratos.arma)
print(Hades.nome, Hades.host)