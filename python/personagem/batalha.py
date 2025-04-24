import time
from utils import limpar_tela # type: ignore

def batalha_mortal_kombat(personagem1, personagem2):
    limpar_tela()
    print(f"🎮 BATALHA MORTAL KOMBAT: {personagem1.nome} VS {personagem2.nome}!")
    print("=" * 40)
    time.sleep(2)

    while personagem1.vida > 0 and personagem2.vida > 0:
        limpar_tela()

        personagem1.atacar(personagem2)
        if personagem2.vida <= 0:
            break

        personagem2.atacar(personagem1)
        if personagem1.vida <= 0:
            print(f"❌ {personagem1.nome} foi derrotado! {personagem2.nome} venceu!")
            break

        print("📊 Status após o turno:")
        personagem1.exibir_status()
        personagem2.exibir_status()

        time.sleep(3)

    print("\n🏁 FIM DE COMBATE")
    if personagem1.vida > 0:
        print(f"🏆 {personagem1.nome} é o grande vencedor! 🔥🔥 FATALITY!")
    else:
        print(f"☠️ {personagem2.nome} venceu... Vingança das Sombras! 💀")
