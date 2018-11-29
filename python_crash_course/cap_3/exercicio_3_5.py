"""
3.5 – Alterando a lista de convidados: Você acabou de saber que um de seus
convidados não poderá comparecer ao jantar, portanto será necessário enviar um
novo conjunto de convites. Você deverá pensar em outra pessoa para convidar.
• Comece com seu programa do Exercício 3.4. Acrescente uma instrução print
no final de seu programa, especificando o nome do convidado que não poderá
comparecer.
• Modifique sua lista, substituindo o nome do convidado que não poderá
comparecer pelo nome da nova pessoa que você está convidando.
• Exiba um segundo conjunto de mensagens com o convite, uma para cada
pessoa que continua presente em sua lista.
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

if __name__ == '__main__':
    main()
