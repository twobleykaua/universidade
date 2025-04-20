import random

class PersonagemGame:
    def __init__(self, nome, classe, nivel, vida, poder):
        self.nome = nome
        self.classe = classe
        self.nivel = nivel
        self.vida = vida
        self.poder = poder
        self.inventario = []

    def atacar(self, outro):
        dano = random.randint(10, 30) + self.poder
        outro.vida -= dano
        print(f"⚔️ {self.nome} atacou {outro.nome}, causando {dano} de dano!")

    def habilidade_especial(self, outro):
        dano = self.nivel * 20 + self.poder
        outro.vida -= dano
        print(f"💥 {self.nome} usou HABILIDADE ESPECIAL em {outro.nome} causando {dano} de dano devastador!")

    def status(self):
        print(f"\n📜 STATUS de {self.nome}:")
        print(f"Classe: {self.classe}")
        print(f"Nível: {self.nivel}")
        print(f"Vida: {max(self.vida, 0)}")  # Evita mostrar vida negativa
        print(f"Poder Base: {self.poder}")
        print(f"Inventário: {', '.join(self.inventario) if self.inventario else 'Vazio'}")
        print("-" * 40)

    def esta_vivo(self):
        return self.vida > 0


# Criando personagens
dark_lord = PersonagemGame("Azrakul", "Lorde das Sombras", 12, 180, 25)
dark_lord.inventario.extend(["Espada Sombria", "Capa da Invisibilidade", "Orbe da Morte"])

guardia = PersonagemGame("Elyndra", "Arcanista Sagrada", 11, 160, 30)
guardia.inventario.extend(["Cajado da Luz Eterna", "Elmo de Prata", "Anel da Cura Divina"])

# Status inicial
dark_lord.status()
guardia.status()

# Loop de combate até um morrer
round_num = 1
while dark_lord.esta_vivo() and guardia.esta_vivo():
    print(f"\n🔥 ROUND {round_num}")
    if random.choice([True, False]):
        dark_lord.atacar(guardia)
    else:
        dark_lord.habilidade_especial(guardia)

    if guardia.esta_vivo():
        if random.choice([True, False]):
            guardia.atacar(dark_lord)
        else:
            guardia.habilidade_especial(dark_lord)
    else:
        print(f"\n💀 {guardia.nome} foi derrotada!")
        break

    # Mostrar status dos dois
    dark_lord.status()
    guardia.status()
    round_num += 1

# Verificando quem venceu
if dark_lord.esta_vivo():
    print(f"\n🏆 {dark_lord.nome} é o grande vencedor!")
elif guardia.esta_vivo():
    print(f"\n🏆 {guardia.nome} é a campeã!")
else:
    print("\n⚔️ Ambos caíram na batalha! Foi um empate mortal!")
