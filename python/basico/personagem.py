import time
import os

class PersonagemGame:
    def __init__(self, nome, classe, vida, ataque):
        self.nome = nome
        self.classe = classe
        self.vida = vida
        self.ataque = ataque
        self.inventario = []

    def exibir_status(self):
        print(f"🧍 Nome: {self.nome}")
        print(f"🌀 Classe: {self.classe}")
        print(f"❤️ Vida: {self.vida} HP")
        print(f"⚔️ Ataque: {self.ataque}")
        print(f"🎒 Inventário: {', '.join(self.inventario)}")
        print("-" * 40)

    def atacar(self, outro_personagem):
        print(f"🔥 {self.nome} ataca {outro_personagem.nome} causando 💥 {self.ataque} de dano!")
        outro_personagem.vida -= self.ataque
        if outro_personagem.vida <= 0:
            outro_personagem.vida = 0
            print(f"💀 {outro_personagem.nome} foi derrotado!")
        else:
            print(f"❤️ {outro_personagem.nome} agora tem {outro_personagem.vida} de vida.")
        print("~" * 40)
        time.sleep(1)

# Função para limpar tela (compatível com Windows e Unix)
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Criando os personagens
liu_kang = PersonagemGame("Liu Kang", "🧘 Monge Shaolin", 100, 18)
scorpion = PersonagemGame("Scorpion", "🦂 Ninja Infernal", 100, 15)

# Inventários (decorativos)
liu_kang.inventario.append("🔥 Chute Flamejante")
scorpion.inventario.append("🪝 Lança Infernal")

# Começo da luta
round_atual = 1
limpar_tela()
print("🎮 BATALHA MORTAL KOMBAT: Liu Kang VS Scorpion!")
print("=" * 40)
time.sleep(2)

# Luta até Scorpion ser derrotado
while scorpion.vida > 0 and liu_kang.vida > 0:
    limpar_tela()
    print(f"\n🥊 ROUND {round_atual}")
    print("=" * 40)

    # Liu Kang ataca primeiro
    liu_kang.atacar(scorpion)
    if scorpion.vida <= 0:
        break

    # Scorpion ataca de volta
    scorpion.atacar(liu_kang)
    if liu_kang.vida <= 0:
        print("❌ Liu Kang foi derrotado! Scorpion venceu!")
        break

    # Exibe status dos dois
    print("📊 Status após o round:")
    liu_kang.exibir_status()
    scorpion.exibir_status()

    round_atual += 1
    time.sleep(3)

# Resultado final
print("\n🏁 FIM DE COMBATE")
if liu_kang.vida > 0:
    print("🏆 Liu Kang é o grande vencedor! 🔥🔥 FATALITY!")
else:
    print("☠️ Scorpion venceu... Vingança das Sombras! 💀")
