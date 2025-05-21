
class A:
    ...#ellipsis
class B:
    ...#ellipsis
class C(A, B):
    ...#ellipsis

#Type anotations
idade: int = 32
salario: float + 35000.50
nome: str = "Julius"
casado: bool = True
dados: dict = {"nome": nome, "salario": salario, "idade": idade}
array: list = [2,5, "ju", 25, 25, 25]
tupla: tuple = (2,5, 25, 25)
unico: set = {2,5,"ju", 25, 25, 25 }

# print(unico)
print(nome.upper()) # metodo builtin
print (vars(C))     # imprime class com dict
#help(C)            # ajuda ver internamente
nome: str = "Ana Paula"
eh_casado: bool = True
pessoa: A = A() #Tipo personalizado
A.cargo = "diretor"

print(A._dict_) # aramazena valores da class