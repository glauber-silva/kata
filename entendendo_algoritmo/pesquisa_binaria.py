import random 
import ordenacao_por_selecao

def pesquisa_binaria(lista, item):
    alto = len(lista) - 1
    baixo =  0
    while baixo <= alto:
        meio = int((baixo + alto )/2)
        chute= lista[meio]
        if  chute == item:
            return meio
        if  chute > item:
            alto  = meio - 1
        else:
            baixo = meio + 1

    return None


lista = random.randrange(1,100)
print(lista)
#lista = [1,3,5,7,9]
#print(pesquisa_binaria(lista, 33))
print(pesquisa_binaria(lista, 3))
print(pesquisa_binaria(lista, -1))

