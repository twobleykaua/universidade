import time
import random
from jogadores.cavaleiro import Cavaleiro
from inimigos.morto_vivo import MortoVivo
from inimigos.chefe import Chefe
from npcs.ferreiro import Ferreiro
from itens.pocao import Pocao
from itens.arma import Arma

def barra_hp(valor):
    coracoes = "❤️" * (valor // 20)
    return coracoes if coracoes else "💔"

def menu():
    print("\n🛡️ --- Menu ---")
    print("1. ⚔️ Atacar inimigo")
    print("2. 🧪 Usar poção")
    print("3. 🧔‍♂️ Falar com o ferreiro")
    print("4. 🗡️ Equipar arma")
    print("5. 💥 Ataque Especial")
    print("6. ❌ Sair")
    return input("Escolha uma ação: ")

def mostrar_status(jogador, inimigo):
    print(f"\n🎖️ {jogador.nome} - HP: {jogador.hp} {barra_hp(jogador.hp)} | Ataque: {jogador.ataque}")
    print(f"👹 {inimigo.nome} - HP: {inimigo.hp} {barra_hp(inimigo.hp)}")

def ataque_especial_jogador(jogador, inimigo):
    dano = jogador.ataque + random.randint(15, 30)
    print(f"\n⚡ {jogador.nome} usa o ATAQUE DAS SOMBRAS! ⚡")
    print(f"🔥 Causa {dano} de dano brutal no inimigo!")
    inimigo.receber_dano(dano)

def ataque_especial_chefe(jogador, chefe):
    falas = [
        "💬 'Você não tem chance contra mim!'",
        "💬 'Afunde nas trevas!'",
        "💬 'Sinta o poder do Abismo!'"
    ]
    print(random.choice(falas))
    if random.random() < 0.4:
        dano = chefe.ataque + random.randint(10, 20)
        print("\n💀 O CHEFE conjura o GRITO DO ABISMO!")
        print(f"🌪️ {jogador.nome} sofre {dano} de dano sombrio!")
        jogador.receber_dano(dano)
    else:
        chefe.atacar(jogador)
        print(f"💢 Dano recebido: {chefe.ataque}")

def main():
    jogador = Cavaleiro("Artorias")
    inimigo = MortoVivo()
    chefe = Chefe()
    ferreiro = Ferreiro()
    pocao = Pocao("Poção Estus", 50)
    espada = Arma("Espada Longa", 20)

    jogador.inventario.append(pocao)
    jogador.inventario.append(espada)

    chefe_apareceu = False

    print(f"\n🎮 Bem-vindo, {jogador.nome}! Prepare-se para a batalha!")
    mostrar_status(jogador, inimigo)

    while True:
        if jogador.hp <= 0:
            print("\n💀 Você caiu na escuridão... GAME OVER.")
            print("🔄 Tente novamente, Guerreiro.")
            break

        if inimigo.hp <= 0 and not chefe_apareceu:
            print(f"\n✅ {inimigo.nome} foi derrotado!")
            time.sleep(1)
            print("🌫️ Um novo inimigo surge...")
            time.sleep(1)
            print("🔥 O CHEFE DEMONÍACO apareceu! 🔥")
            inimigo = chefe
            chefe_apareceu = True
            mostrar_status(jogador, inimigo)
            continue

        if chefe_apareceu and inimigo.hp <= 0:
            print("🏆 Você derrotou o CHEFE DEMONÍACO!")
            time.sleep(1)
            print("\n⚔️ Vitória conquistada! ⚔️")
            time.sleep(1)
            print("🔥 As cinzas se assentam, e a chama se reacende...")
            time.sleep(2)
            print("\n🎉 --- FIM DO JOGO ---")
            print("📝 Obrigado por jogar, Herói das Cinzas.")
            break

        opcao = menu()

        if opcao == "1":
            if random.random() < 0.2:
                print("💨 Seu ataque errou o alvo!")
            else:
                print("🗡️ Você ataca o inimigo!")
                jogador.atacar(inimigo)
                print(f"💥 Dano causado: {jogador.ataque}")
            time.sleep(1)
            if inimigo.hp > 0:
                print("👹 O inimigo contra-ataca!")
                if isinstance(inimigo, Chefe):
                    ataque_especial_chefe(jogador, inimigo)
                else:
                    if random.random() < 0.2:
                        print("💨 O inimigo errou o ataque!")
                    else:
                        inimigo.atacar(jogador)
                        print(f"💢 Dano recebido: {inimigo.ataque}")

        elif opcao == "2":
            for item in jogador.inventario:
                if isinstance(item, Pocao):
                    jogador.hp += item.cura
                    print(f"🧪 {jogador.nome} usou {item.nome} e curou {item.cura} de vida. ❤️ HP atual: {jogador.hp}")
                    jogador.inventario.remove(item)
                    break
            else:
                print("🚫 Você não tem poções!")

        elif opcao == "3":
            falas_ferreiro = [
                "🔧 'Precisa de reforço na arma, guerreiro?'",
                "🛠️ 'Essa lâmina ainda pode cortar muitos demônios.'",
                "💬 'Não se esqueça de manter sua lâmina afiada!'"
            ]
            print(random.choice(falas_ferreiro))

        elif opcao == "4":
            for item in jogador.inventario:
                if isinstance(item, Arma):
                    jogador.ataque += item.dano
                    print(f"🗡️ {jogador.nome} equipou {item.nome}. Ataque aumentado para {jogador.ataque} ⚔️")
                    jogador.inventario.remove(item)
                    break
            else:
                print("🚫 Você não tem nenhuma arma para equipar.")

        elif opcao == "5":
            ataque_especial_jogador(jogador, inimigo)
            if inimigo.hp > 0:
                print("👹 O inimigo contra-ataca!")
                if isinstance(inimigo, Chefe):
                    ataque_especial_chefe(jogador, inimigo)
                else:
                    inimigo.atacar(jogador)
                    print(f"💢 Dano recebido: {inimigo.ataque}")

        elif opcao == "6":
            print("👋 Saindo do jogo...")
            break

        else:
            print("❓ Opção inválida!")

        mostrar_status(jogador, inimigo)
        time.sleep(1)

if __name__ == "__main__":
    main()
