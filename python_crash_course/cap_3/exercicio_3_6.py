"""
3.6 – Mais convidados: Você acabou de encontrar uma mesa de jantar maior,
portanto agora tem mais espaço disponível. Pense em mais três convidados para o
jantar.
• Comece com seu programa do Exercício 3.4 ou do Exercício 3.5. Acrescente
uma instrução print no final de seu programa informando às pessoas que você
encontrou uma mesa de jantar maior.
• Utilize insert() para adicionar um novo convidado no início de sua lista.
• Utilize insert() para adicionar um novo convidado no meio de sua lista.
• Utilize append() para adicionar um novo convidado no final de sua lista.
• Exiba um novo conjunto de mensagens de convite, uma para cada pessoa que
está em sua lista.
"""

import random
from pessoa import Pessoa

def printLista(convidados):
    for i in convidados:
        print('\n %s, está convidado para um jantar em minha residência, dia 30 de Fevereiro \n' % (i.name))

def main():
    lista = ['Isaac Asimov', 'Arthur Clarke', 'Frank Hebert', 'William Gibson']
    convidados = []
    for i in lista:
        convidados.append(Pessoa(i))

    printLista(convidados)

    desconvidar = random.randint(0,3)
    
    print("\n %s, não poderá comparecer ao jantar \n" % (convidados[desconvidar].name))

    convidados[desconvidar] = Pessoa('Phillip K. Dick')
    
    printLista(convidados)

    print("\n Encontrada uma mesa maior")

    convidados.insert(0, Pessoa(''))

if __name__ == '__main__':
    main()
