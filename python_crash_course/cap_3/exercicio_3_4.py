'''
3.4 – Lista de convidados: Se pudesse convidar alguém, vivo ou morto, para o
jantar, quem você convidaria? Crie uma lista que inclua pelo menos três pessoas
que você gostaria de convidar para jantar. Em seguida, utilize sua lista para exibir
uma mensagem para cada pessoa, convidando-a para jantar.
'''
from pessoa import Pessoa


def main():
    nomes = []
    
    while len(nomes) < 5:
        nomes.append(Pessoa(input('Convidar :')))

    for i in nomes:
        print(' %s, você está convidado para jantar dia 30/02/2019' % i.name)

if __name__ == '__main__':
    main()