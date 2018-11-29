'''
Armazene os nomes de alguns de seus amigos em uma lista
chamada names. Exiba o nome de cada pessoa acessando cada elemento da lista,
um de cada vez."
'''
from pessoa import Pessoa

def main():
    nomes = []
    while len(nomes) < 5:
        nomes.append(Pessoa(input("Nome: ")))

    for i in nomes:
        i.printNames()

if __name__ == '__main__':
    main()