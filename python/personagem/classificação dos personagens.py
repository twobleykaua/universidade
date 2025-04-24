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
