import random
from functools import partial
from ordenacao_por_selecao import *

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


# temp_lista = random.sample(range(1, 100), 99)
# lista = ordenacao(temp_lista)
# print(lista)
#lista = [1,3,5,7,9]
#print(pesquisa_binaria(lista, 33))

def assert_true(expr, line):
    try:
        assert expr
    except AssertionError:
        print(expr)

if __name__ == '__main__':
    assert_true(pesquisa_binaria([5, 3, 1, 7, 9], 3) == 0 )
    assert_true(pesquisa_binaria([5, 3, 1, 7, 9], -1) == None )




# TODO write test