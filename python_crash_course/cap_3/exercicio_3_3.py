'''
3.3 – Sua própria lista: Pense em seu meio de transporte preferido, como
motocicleta ou carro, e crie uma lista que armazene vários exemplos. Utilize sua
lista para exibir uma série de frases sobre esses itens, como “Gostaria de ter uma
moto Honda”.
'''
from transporte import Transporte

def main():
    transportes = []
    transportes.append(Transporte('moto', 'Honda'))
    transportes.append(Transporte('carro', 'Crysler'))
    transportes.append(Transporte('bicleta', 'Cannondale'))

    for i in transportes:
        print("Eu gostaria de ter  %s, %s" % (i.tipo, i.marca))

if __name__ == '__main__':
    main()