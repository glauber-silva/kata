'''
Saudações: Comece com a lista usada no Exercício 3.1, mas em vez de
simplesmente exibir o nome de cada pessoa, apresente uma mensagem a elas. O
texto de cada mensagem deve ser o mesmo, porém cada mensagem deve estar
personalizada com o nome da pessoa.
'''
from exercicio_3_1 import Pessoa

a = Pessoa('')

for i in range(len(a.names)):
    print("Saudacoes, %s !" % (a.names[i]))
