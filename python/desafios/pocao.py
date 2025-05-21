class Personagem:
    def _init_(self, nome):
        self.nome = nome
        self.saude = 10
        self.vivo = True
        
    def usar_pocao(self, pocao):
        if not self.vivo:
            print(f"{self.nome} está morto e não pode usar poções.")
            return

        # Aplica o efeito da poção (pode ser positiva ou negativa)
        self.saude += pocao.potencia
        print(f"Personagem {self.nome} usou poção {pocao.tipo}")
        print(f"Dano {pocao.potencia} saúde atual: {self.saude}")

        # Verifica se o personagem morreu
        if self.saude <= 0:
            self.vivo = False
            self.saude = 0
            print(f"{self.nome} foi de arrasta pra cima")

class PocaoVerde:
    def _init_(self, tipo, potencia):
        self.tipo = tipo
        self.potencia = potencia

class PocaoRoxa:
    def _init_(self, tipo, potencia):
        self.tipo = tipo
        self.potencia = -abs(potencia)  # Sempre dano negativo (veneno)

# Instanciar Jogador
p1 = Personagem("Chaves")

# Criar poções
pocao1 = PocaoVerde("Cura", 15)
pocao2 = PocaoRoxa("Veneno", 25)

# Usar poções
p1.usar_pocao(pocao1)  # Cura
p1.usar_pocao(pocao2)  # Veneno

# Tentando usar outra poção após a morte
p1.usar_pocao(pocao1)

# Mostra o objeto da poção (exemplo do del p1)
del p1
print(pocao1)