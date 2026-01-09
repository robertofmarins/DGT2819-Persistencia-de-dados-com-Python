# selection.sort.py

# a) Array com 15 números inteiros não ordenados
array = [42, 7, 19, 3, 88, 25, 14, 60, 1, 33, 9, 71, 5, 27, 50]

print("Array original:")
print(array)

# b) Primeiro laço for
for i in range(len(array)):

    # c) Variável que recebe o valor de i
    min_index = i

    # d) Segundo laço for
    for j in range(i + 1, len(array)):

        # e) Verifica se o valor atual é menor que o menor encontrado
        if array[min_index] > array[j]:
            # f) Atualiza o índice do menor valor
            min_index = j

    # g) Troca dos valores
    array[i], array[min_index] = array[min_index], array[i]

# h) Impressão do array ordenado
print("\nArray ordenado de forma crescente:")
print(array)
