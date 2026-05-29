# 🐍 Python Database & Persistence Lab

<div align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge">
  <img src="https://img.shields.io/badge/Algorithms-Sorting-blue?style=for-the-badge" alt="Algorithms Badge">
  <img src="https://img.shields.io/badge/Performance-Benchmarking-orange?style=for-the-badge" alt="Benchmarking Badge">
  <img src="https://img.shields.io/badge/Context-Estácio_College-red?style=for-the-badge" alt="Estácio Badge">
</div>

---

Este projeto é um laboratório prático voltado para a manipulação de arquivos locais e análise empírica de complexidade de algoritmos de ordenação em **Python**. 

Ele foi desenvolvido para fins acadêmicos como trabalho prático avaliativo da disciplina **DGT2819 – Persistência de Dados com Python** na **Estácio de Sá**, durante o **3º Período**.

---

## 🎯 Escopo do Laboratório & Aprendizados

O projeto demonstra a implementação de lógica computacional de baixo nível e manipulação de fluxos de arquivos (File I/O):

- **Manipulação de Arquivos (Leitura/Escrita):** Extração, limpeza e normalização de termos de arquivos de texto (`texto.txt`) e gravação dos dados estruturados de saída em arquivos ordenados (`palavras_ordenadas.txt`).
- **Implementação de Algoritmos de Ordenação:** Desenvolvimento manual dos algoritmos clássicos de ordenação:
  *   **Bubble Sort** ($O(n^2)$ de complexidade no pior caso).
  *   **Selection Sort** ($O(n^2)$ de complexidade constante).
- **Benchmarking e Medição de Performance:** Utilização da biblioteca nativa `time` para capturar e comparar o tempo de execução (em segundos) de cada algoritmo manual contra o método nativo do Python (o algoritmo **Timsort**, com complexidade de tempo de $O(n \log n)$).

---

## 📂 Estrutura dos Arquivos

```bash
/
├── kdd.py                   # Classe principal e roteiro de benchmarking
├── bubble.sort.py           # Script isolado de teste do Bubble Sort
├── selection.sort.py        # Script isolado de teste do Selection Sort
├── array.sort.py            # Script isolado de teste de ordenação nativa
├── ler.txt.py               # Exemplo prático de leitura de arquivos
├── escrever.txt.py          # Exemplo prático de escrita de arquivos
├── texto.txt                # Arquivo de entrada contendo palavras desordenadas
├── palavras_ordenadas.txt   # Arquivo gerado de saída com os termos ordenados
└── README.md                # Documentação técnica do projeto
```

---

## 🚀 Como Executar

Por utilizar apenas a biblioteca padrão do Python, o projeto não possui dependências externas:

1. Certifique-se de ter o Python 3 instalado no sistema.
2. Execute o script principal de benchmarking:
   ```bash
   python kdd.py
   ```
3. O console imprimirá o tempo de execução de cada método de ordenação e atualizará o arquivo `palavras_ordenadas.txt`.
