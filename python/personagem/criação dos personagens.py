from personagem import PersonagemGame  # Importa a classe do personagem

# Criação dos personagens
liu_kang = PersonagemGame("Liu Kang", "🧘 Monge Shaolin", 100, 18)
scorpion = PersonagemGame("Scorpion", "🦂 Ninja Infernal", 100, 15)

# Adicionando habilidades ao inventário
liu_kang.inventario.append("🔥 Chute Flamejante")
scorpion.inventario.append("🪝 Lança Infernal")
