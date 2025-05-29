# from itens import arma, armadura, pocao
# print(arma.arma("espada").usar())
# from itens import * 
from itens import Pocao, Arma, Armadura

def main():
    faca = Arma("Tramontina")
    (faca.usar())

    suco = Pocao("Magia Azul")
    (suco.usar())

    blindagem = Armadura("Blindagem do Twobley")
    (blindagem.usar())

if __name__ == "__main__":
    main()