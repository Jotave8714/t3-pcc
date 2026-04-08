"""
Ponto de entrada do programa.
Lê o dígrafo ponderado eulerizado, exibe informações de graus,
verifica o balanceamento, encontra o circuito euleriano usando o
método de Hierholzer e exibe o circuito e o custo total.

Uso:
    python main.py [arquivo_entrada]

    Se nenhum arquivo for informado, usa 'dados/entrada_eulerizada.txt'.
"""

import sys
import os

# Adiciona o diretório src ao path para importações locais
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from digraph import Digraph
from directed_eulerian_cycle import DirectedEulerianCycle


def main():
    # Define o arquivo de entrada
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
    else:
        # Caminho padrão relativo ao diretório do projeto
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        filepath = os.path.join(base_dir, "dados", "entrada_eulerizada.txt")

    if not os.path.exists(filepath):
        print(f"Erro: arquivo '{filepath}' não encontrado.")
        sys.exit(1)

    print("=" * 60)
    print("  PROBLEMA DO CARTEIRO CHINÊS - CIRCUITO EULERIANO")
    print("=" * 60)
    print(f"\nArquivo de entrada: {filepath}")

    # 1. Ler o dígrafo ponderado
    with open(filepath, "r") as f:
        graph = Digraph(file=f)
    print(f"\nDígrafo carregado: {graph.V} vértices, {graph.E} arestas")

    # 2. Exibir o dígrafo
    print("\n--- Listas de adjacência ---")
    print(graph)

    # 3. Informar os graus de entrada e saída
    print("--- Graus dos vértices ---")
    print(f"{'Vértice':>8}  {'Entrada':>8}  {'Saída':>8}  {'Delta':>8}  {'Status'}")
    print("-" * 55)

    all_balanced = True
    for v in range(graph.V):
        in_d = graph.in_degree(v)
        out_d = graph.out_degree(v)
        delta = out_d - in_d
        status = "balanceado" if delta == 0 else f"DESBALANCEADO ({delta:+d})"
        if delta != 0:
            all_balanced = False
        print(f"{v:>8}  {in_d:>8}  {out_d:>8}  {delta:>+8}  {status}")

    # 4. Verificar se o grafo está balanceado
    print()
    if all_balanced:
        print("✓ Todos os vértices estão balanceados.")
        print("  O dígrafo admite circuito euleriano.")
    else:
        print("✗ O dígrafo NÃO está balanceado.")
        print("  Não é possível encontrar circuito euleriano.")
        print("  Verifique a eulerização no arquivo de entrada.")
        sys.exit(1)

    # 5. Executar o método de Hierholzer
    print("\n--- Método de Hierholzer ---")
    euler = DirectedEulerianCycle(graph)

    if euler.has_eulerian_cycle():
        # 6. Imprimir o circuito euleriano
        cycle = euler.cycle()
        edges = euler.cycle_edges()

        print("\nCircuito euleriano encontrado!\n")
        print("Sequência de vértices:")
        print("  " + " -> ".join(str(v) for v in cycle))

        print("\nSequência de arestas:")
        for i, edge in enumerate(edges):
            print(f"  {i + 1:>3}. {edge}")

        # 7. Informar o custo total
        print(f"\n{'=' * 40}")
        print(f"  CUSTO TOTAL DO CIRCUITO: {euler.cost():.1f}")
        print(f"{'=' * 40}")
    else:
        print("\n✗ Não foi possível encontrar um circuito euleriano.")
        print("  O dígrafo pode não ser fortemente conexo.")


if __name__ == "__main__":
    main()
