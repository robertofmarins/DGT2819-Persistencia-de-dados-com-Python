# escrever.txt.py

# Abre (ou cria) o arquivo texto.txt no modo escrita
arquivo = open("texto.txt", "w")

# Cria uma lista vazia
texto = list()

# Adiciona frases genéricas à lista
texto.append("Primeira linha do arquivo.\n")
texto.append("Segunda linha gravada no arquivo.\n")
texto.append("Terceira linha adicionada ao conteúdo.\n")

# Escreve o conteúdo da lista no arquivo
arquivo.writelines(texto)

# Fecha o arquivo
arquivo.close()
