# kdd.py

import time

class Ordenador:

    def bubble_sort(self, lista):
        for i in range(len(lista)):
            for j in range(0, len(lista) - i - 1):
                if lista[j] > lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
        return lista

    def selection_sort(self, lista):
        for i in range(len(lista)):
            min_index = i
            for j in range(i + 1, len(lista)):
                if lista[j] < lista[min_index]:
                    min_index = j
            lista[i], lista[min_index] = lista[min_index], lista[i]
        return lista


# Lista para armazenar as palavras
palavras = list()

# Leitura do arquivo txt
with open("texto.txt", "r") as arquivo:
    for linha in arquivo:
        partes = linha.split()
        for palavra in partes:
            palavras.append(palavra.lower())

ordenador = Ordenador()

# Bubble Sort
lista_bubble = palavras.copy()
inicio = time.time()
ordenador.bubble_sort(lista_bubble)
fim = time.time()
print("Bubble Sort:")
print("Tempo de execução:", fim - inicio)
print(lista_bubble)
print()

# Selection Sort
lista_selection = palavras.copy()
inicio = time.time()
ordenador.selection_sort(lista_selection)
fim = time.time()
print("Selection Sort:")
print("Tempo de execução:", fim - inicio)
print(lista_selection)
print()

# Sort nativo do Python
lista_sort = palavras.copy()
inicio = time.time()
lista_sort.sort()
fim = time.time()
print("Sort nativo do Python:")
print("Tempo de execução:", fim - inicio)
print(lista_sort)
print()

# Após comparação, utiliza o sort nativo para gerar o arquivo final
with open("palavras_ordenadas.txt", "w") as saida:
    for palavra in lista_sort:
        saida.write(palavra + "\n")
