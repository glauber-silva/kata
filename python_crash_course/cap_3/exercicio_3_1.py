'''
Armazene os nomes de alguns de seus amigos em uma lista
chamada names. Exiba o nome de cada pessoa acessando cada elemento da lista,
um de cada vez."
'''

class Pessoa:

    names = ['Alisson', 'Diogo', 'Jefferson', 'Cleber', 'Marcus']


    def __init__(self, name):
        self.name = name

    def printNames(self):
        for i in range(len(self.names)):
            print(self.names[i])



def main():
    a = Pessoa('')
    a.printNames()

if __name__ == '__main__':
    main()