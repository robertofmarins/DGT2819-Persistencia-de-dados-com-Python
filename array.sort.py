# Array de inteiros
numeros = [42, 7, 19, 3, 88, 25, 14, 60, 1, 33, 9, 71, 5, 27, 50]

print("Array original (inteiros):")
print(numeros)

# Ordenação crescente
numeros.sort()
print("\nArray ordenado de forma crescente:")
print(numeros)

# Ordenação decrescente
numeros.sort(key=None, reverse=True)
print("\nArray ordenado de forma decrescente:")
print(numeros)

# Array de strings
dados = [
    "Roberto",
    "Thais",
    "Maria Laura",
    "João Lucas",
    "1988-09-07",   # dataNascimento
    "1990-10-14",
    "123.456.789-00",  # cpf
    "12.345.678-9"     # rg
]

print("\nArray original (strings):")
print(dados)

# Ordenação crescente (ordem alfabética)
dados.sort()
print("\nArray de strings ordenado de forma crescente:")
print(dados)

# Ordenação decrescente
dados.sort(key=None, reverse=True)
print("\nArray de strings ordenado de forma decrescente:")
print(dados)