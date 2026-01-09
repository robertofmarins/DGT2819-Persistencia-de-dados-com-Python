# ler.txt.py

# Abrindo o arquivo com open
arquivo = open("loremipsum.txt", "r")

# Imprime todo o conteúdo do arquivo
conteudo = arquivo.read()
print("Conteúdo completo do arquivo:\n")
print(conteudo)

# Volta o cursor para o início do arquivo
arquivo.seek(0)

# Imprime apenas a primeira linha
primeira_linha = arquivo.readline()
print("Primeira linha do arquivo:\n")
print(primeira_linha)

# Volta novamente o cursor para o início
arquivo.seek(0)

# Imprime apenas os 3 primeiros caracteres
tres_primeiros = arquivo.read(3)
print("Três primeiros caracteres do arquivo:")
print(tres_primeiros)

# Fecha o arquivo aberto com open
arquivo.close()

# Utilizando a instrução with
print("\nLeitura do arquivo utilizando with:\n")
with open("loremipsum.txt", "r") as arquivo_with:
    conteudo_with = arquivo_with.read()
    print(conteudo_with)
