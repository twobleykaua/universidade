from abc import ABC, abstractmethod
class Jogador(ABC):
    def __init__(self, nome:str, dano:int):
        self.nome = nome
        self.dano = dano
        self.__saude = 100 #encapsulamento

        @property #decorador retorna apenas como propriedade
        def saude(self):
            return self.__saude

        @saude.setter #decorador retorna apenas como propriedade
        def saude(self, valor):
             self.saude += max(0, valor)
            
        @ abstractmethod
        def atacar(self):
            print(f"{self.nome} atacou!")

        @ abstractmethod
        def defender(self):
                print(f"{self.nome} defendeu!")

if __name__ == '__main__':
    p1 = Jogador("jhow", 50)
    p1.atacar()
    print(p1.get_saude())