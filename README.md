# Trabalho Prático 3 — Circuito Euleriano no Problema do Carteiro Chinês

**Disciplina:** Resolução de Problemas com Grafos
**Aluno:** João Victor Feijó Vasconcelos  
**Orientador:** Prof. Ricardo Carubbi  
**Linguagem:** Python

## Descrição

Este projeto implementa o **método de Hierholzer** para encontrar um circuito euleriano em um dígrafo ponderado, no contexto do **Problema do Carteiro Chinês**.

O grafo oficial de entrada foi extraído da Figura 1 do enunciado (baseada na visualização de [algorithms.discrete.ma.tum.de](https://algorithms.discrete.ma.tum.de/graph-algorithms/directed-chinese-postman/index_en.html)), contendo **6 vértices** e **11 arestas dirigidas**.

## Eulerização Manual

### Mapeamento de vértices

| Vértice (letra) | Vértice (número) |
|:---:|:---:|
| a | 0 |
| b | 1 |
| c | 2 |
| d | 3 |
| e | 4 |
| f | 5 |

### Arestas do grafo original (11 arestas)

| De | Para | Peso |
|:---:|:---:|:---:|
| a (0) | c (2) | 20 |
| a (0) | b (1) | 10 |
| b (1) | e (4) | 10 |
| b (1) | d (3) | 50 |
| c (2) | e (4) | 33 |
| c (2) | d (3) | 20 |
| d (3) | f (5) | 12 |
| d (3) | e (4) | 5 |
| e (4) | f (5) | 1 |
| e (4) | a (0) | 12 |
| f (5) | c (2) | 22 |

### Análise de graus

| Vértice | Grau de Entrada | Grau de Saída | Delta (saída − entrada) | Status |
|:---:|:---:|:---:|:---:|:---|
| a (0) | 1 | 2 | +1 | desbalanceado |
| b (1) | 1 | 2 | +1 | desbalanceado |
| c (2) | 2 | 2 | 0 | balanceado |
| d (3) | 2 | 2 | 0 | balanceado |
| e (4) | 3 | 2 | −1 | desbalanceado |
| f (5) | 2 | 1 | −1 | desbalanceado |

### Vértices desbalanceados

- **Excesso de saída (delta > 0):** a (0) com delta = +1, b (1) com delta = +1
- **Excesso de entrada (delta < 0):** e (4) com delta = −1, f (5) com delta = −1

Para eulerizar, é necessário adicionar caminhos dirigidos dos vértices com delta negativo para os vértices com delta positivo, de modo a equilibrar os graus.

### Caminhos mínimos calculados (manualmente / Dijkstra)

| De | Para | Caminho | Custo |
|:---:|:---:|:---|:---:|
| e → a | e → a | direto | 12 |
| e → b | e → a → b | | 22 |
| f → a | f → c → d → e → a | | 59 |
| f → b | f → c → d → e → a → b | | 69 |

### Emparelhamento ótimo

| Opção | Pareamentos | Custo total |
|:---:|:---|:---:|
| 1 | e → a (12) + f → b (69) | 81 |
| 2 | e → b (22) + f → a (59) | 81 |

Ambas as opções têm custo total 81. Foi escolhida a **Opção 1** (e → a e f → b).

### Arestas adicionadas (6 arestas)

Para o caminho **e → a** (custo 12):
- e (4) → a (0), peso 12

Para o caminho **f → b**, que passa por f → c → d → e → a → b (custo 69):
- f (5) → c (2), peso 22
- c (2) → d (3), peso 20
- d (3) → e (4), peso 5
- e (4) → a (0), peso 12
- a (0) → b (1), peso 10

### Resultado

- **Custo total do grafo original:** 195
- **Custo das arestas adicionadas:** 81
- **Custo total do circuito euleriano:** 276

## Instruções de Execução

### Pré-requisitos

- Python 3.6 ou superior

### Execução

A partir do diretório raiz do projeto:

```bash
# Executar com o grafo oficial eulerizado (padrão)
python3 src/main.py

# Ou especificar um arquivo de entrada
python3 src/main.py dados/entrada_eulerizada.txt

# Testar com o exemplo fornecido pelo professor
python3 src/main.py dados/entrada_exemplo_eulerizada.txt

# Verificar o grafo original (sem eulerização)
python3 src/main.py dados/entrada_original.txt
```

### Formato de entrada

```
V
E
v w peso
v w peso
...
```

- `V`: número de vértices
- `E`: número de arestas dirigidas
- Cada linha `v w peso`: aresta dirigida de `v` para `w` com o peso indicado

## Estrutura do Projeto

```
t3-pcc/
├── README.md
├── dados/
│   ├── entrada_original.txt          # Grafo oficial original (11 arestas)
│   ├── entrada_eulerizada.txt        # Grafo oficial eulerizado (17 arestas)
│   ├── entrada_exemplo.txt           # Exemplo do professor (original)
│   └── entrada_exemplo_eulerizada.txt # Exemplo do professor (eulerizado)
└── src/
    ├── main.py                       # Ponto de entrada do programa
    ├── directed_edge.py              # Classe DirectedEdge (aresta ponderada)
    ├── edge_weighted_digraph.py      # Classe EdgeWeightedDigraph (dígrafo ponderado)
    └── directed_eulerian_cycle.py    # Método de Hierholzer
```

## Referências

- Implementação base: `algs4-py` (Princeton Algorithms, 4th Edition — Python)
- Visualização de referência: [Directed Chinese Postman — TUM](https://algorithms.discrete.ma.tum.de/graph-algorithms/directed-chinese-postman/index_en.html)
