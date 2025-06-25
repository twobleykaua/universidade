from jogadores.cavaleiro import Cavaleiro
from inimigos.morto_vivo import MortoVivo
from inimigos.chefe import Chefe
from npcs.ferreiro import Ferreiro
from itens.pocao import Pocao
from itens.arma import Arma

def menu():
    print("\n--- Menu ---")
    print("1. Atacar inimigo")
    print("2. Usar poção")
    print("3. Falar com o ferreiro")
    print("4. Equipar arma")
    print("5. Sair")
    return input("Escolha uma ação: ")

def main():
    jogador = Cavaleiro("Artorias")
    inimigo = MortoVivo()
    chefe = Chefe()
    ferreiro = Ferreiro()
    pocao = Pocao("Poção Estus", 50)
    espada = Arma("Espada Longa", 20)

    jogador.inventario.append(pocao)
    jogador.inventario.append(espada)

    print(f"\nBem-vindo, {jogador.nome}! Prepare-se para a batalha!")

    while True:
        if jogador.hp <= 0:
            print("Você morreu... GAME OVER.")
            break
        if inimigo.hp <= 0:
            print(f"{inimigo.nome} foi derrotado!")
            inimigo = chefe  # troca para o chefe na segunda fase
            print("Um novo inimigo surge... o CHEFE DEMONÍACO!")
        
        opcao = menu()

        if opcao == "1":
            jogador.atacar(inimigo)
            if inimigo.hp > 0:
                inimigo.atacar(jogador)

        elif opcao == "2":
            for item in jogador.inventario:
                if isinstance(item, Pocao):
                    jogador.hp += item.cura
                    print(f"{jogador.nome} usou {item.nome} e curou {item.cura} de vida. HP atual: {jogador.hp}")
                    jogador.inventario.remove(item)
                    break
            else:
                print("Você não tem poções!")

        elif opcao == "3":
            ferreiro.falar()

        elif opcao == "4":
            for item in jogador.inventario:
                if isinstance(item, Arma):
                    jogador.ataque += item.dano
                    print(f"{jogador.nome} equipou {item.nome}. Ataque aumentado para {jogador.ataque}")
                    jogador.inventario.remove(item)
                    break
            else:
                print("Você não tem nenhuma arma para equipar.")

        elif opcao == "5":
            print("Saindo do jogo...")
            break

        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
