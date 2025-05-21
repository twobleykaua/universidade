import datetime

class Item:
    def __init__(self, nome, tipo, peso, empilhavel=False, quantidade=1, durabilidade=None, raridade="comum", efeito=None):
        self.nome = nome
        self.tipo = tipo
        self.peso = peso
        self.empilhavel = empilhavel
        self.quantidade = quantidade
        self.durabilidade = durabilidade
        self.raridade = raridade
        self.efeito = efeito
        self.data_adicionado = datetime.datetime.now()

    def __repr__(self):
        base = f"{self.nome} ({self.tipo})"
        if self.empilhavel:
            base += f" x{self.quantidade}"
        if self.durabilidade is not None:
            base += f" [Durabilidade: {self.durabilidade}]"
        base += f" [{self.raridade.capitalize()}]"
        return base


class Inventario:
    def __init__(self, capacidade_peso=100):
        self.itens = []
        self.capacidade_peso = capacidade_peso

    def peso_total(self):
        return sum(item.peso * item.quantidade for item in self.itens)

    def adicionar_item(self, novo_item):
        if self.peso_total() + (novo_item.peso * novo_item.quantidade) > self.capacidade_peso:
            return False
        if novo_item.empilhavel:
            for item in self.itens:
                if item.nome == novo_item.nome:
                    item.quantidade += novo_item.quantidade
                    return True
        self.itens.append(novo_item)
        return True

    def remover_item(self, nome, quantidade=1):
        for item in self.itens:
            if item.nome == nome:
                if item.empilhavel:
                    if item.quantidade > quantidade:
                        item.quantidade -= quantidade
                    else:
                        self.itens.remove(item)
                else:
                    self.itens.remove(item)
                return True
        return False

    def listar_itens(self, filtro_tipo=None):
        for item in sorted(self.itens, key=lambda i: i.raridade, reverse=True):
            if filtro_tipo is None or item.tipo == filtro_tipo:
                print(item)
        print(f"Peso total: {self.peso_total():.1f}/{self.capacidade_peso}")

    def usar_item(self, nome):
        for item in self.itens:
            if item.nome == nome:
                if item.efeito:
                    print(f"Você usou {item.nome}. Efeito: {item.efeito}")
                else:
                    print(f"Você usou {item.nome}.")
                self.remover_item(nome)
                return
        print("Item não encontrado.")

    def equipar_item(self, nome):
        for item in self.itens:
            if item.nome == nome and item.tipo in ["arma", "armadura"]:
                print(f"{item.nome} equipado.")
                return
        print("Não é possível equipar esse item.")

    def reparar_item(self, nome):
        for item in self.itens:
            if item.nome == nome and item.durabilidade is not None:
                item.durabilidade = 100
                print(f"{item.nome} foi reparado.")
                return
        print("Esse item não pode ser reparado.")

    def ordenar_por(self, chave="nome"):
        if chave == "raridade":
            self.itens.sort(key=lambda i: ["comum", "incomum", "raro", "épico", "lendário"].index(i.raridade))
        else:
            self.itens.sort(key=lambda i: getattr(i, chave))
        print(f"Itens ordenados por {chave}.")


inventario = Inventario(capacidade_peso=120)

inventario.adicionar_item(Item("Espada de Aço", "arma", 12, durabilidade=80, raridade="raro"))
inventario.adicionar_item(Item("Poção de Vida", "consumível", 0.5, empilhavel=True, quantidade=5, efeito="Cura 50HP"))
inventario.adicionar_item(Item("Chave do Cofre", "chave", 0.1))
inventario.adicionar_item(Item("Minério de Prata", "recurso", 3, empilhavel=True, quantidade=10))
inventario.adicionar_item(Item("Carta da Rainha", "missão", 0.1, raridade="épico"))

inventario.listar_itens()
inventario.usar_item("Poção de Vida")
inventario.equipar_item("Espada de Aço")
inventario.reparar_item("Espada de Aço")
inventario.ordenar_por("raridade")
inventario.listar_itens()
