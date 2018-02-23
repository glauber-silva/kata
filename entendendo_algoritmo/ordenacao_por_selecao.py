def busca_menor(arr):
    menor = arr[0]
    indice = 0
    for i in range(1,len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            indice = i
    return indice


def ordenacao(arr):
    novo_arr = []
    for i in range(len(arr)):
        menor = busca_menor(arr)
        novo_arr.append(arr.pop(menor))
    return novo_arr

#print(ordenacao([5,3,6,2,10]))
