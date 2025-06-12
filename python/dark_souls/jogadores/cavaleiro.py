from jogadores  .jogador import Jogador

class Cavaleiro(Jogador):
     def __init__(self, nome:str, dano:int, resistencia=85, armadura="Diamante"):
        self.armadura = armadura
        self.resistencia = resistencia
        super().__init__(nome, dano)


    # self.__saude = 100 #encapsulamento

     @property #decorador retorna apenas como propriedade
     def saude(self):
         return self.__saude

     @saude.setter #decorador retorna apenas como propriedade
     def saude(self, valor):
         self.saude += max(0, valor)
            
     def atacar(self):
         print(f"{self.nome} atacou!")
         print("atacar Polimorfico")
 
     def defender(self):
         print(f"{self.nome} defendeu!")
         print("defender Polimorfico")

     def armadura(self):
         print(f"{self.nome} armadura!")
         print("armadura de diamante")

if __name__ == '__main__':
     cavaleiro = Cavaleiro("rei Artur", 80)
     cavaleiro.atacar()