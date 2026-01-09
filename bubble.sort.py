# bubble.sort.py

def bubbleSort(array):
    # Primeiro laço: controla o número de passagens pelo array
    for i in range(len(array)):
        # Segundo laço: compara elementos adjacentes
        for j in range(0, len(array) - i - 1):
            # Se o elemento atual for maior que o próximo, troca
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp


# Array de números com 15 posições (não ordenado)
numeros = [42, 7, 19, 3, 88, 25, 14, 60, 1, 33, 9, 71, 5, 27, 50]

print("Array original:")
print(numeros)

# Aplicação do Bubble Sort
bubbleSort(numeros)

print("\nArray ordenado de forma crescente:")
print(numeros)
