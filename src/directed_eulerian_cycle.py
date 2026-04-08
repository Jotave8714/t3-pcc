"""
Implementação do método de Hierholzer para encontrar um circuito euleriano
em um dígrafo ponderado.

Baseado na classe DirectedEulerianCycle do algs4-py, adaptado para
trabalhar com arestas ponderadas (DirectedEdge) e calcular o custo total.

Referência conceitual:
  https://algorithms.discrete.ma.tum.de/graph-algorithms/directed-chinese-postman/index_en.html
"""

from collections import deque
from digraph import Digraph


class DirectedEulerianCycle:
    """
    Encontra um circuito euleriano em um dígrafo ponderado usando o
    método de Hierholzer.

    Pré-condição: o grafo deve ser balanceado (grau de entrada == grau de
    saída para todos os vértices) e fortemente conexo.
    """

    def __init__(self, graph: Digraph):
        self._cycle = None
        self._edges_in_cycle = None
        self._cost = 0.0

        # Verificação: o grafo deve ter arestas
        if graph.E == 0:
            return

        # Verificação: todos os vértices devem estar balanceados
        for v in range(graph.V):
            if graph.in_degree(v) != graph.out_degree(v):
                return

        # Método de Hierholzer
        # Usa índices para percorrer as listas de adjacência de cada vértice
        adj_iter = [0] * graph.V
        adj_lists = [list(graph.adj[v]) for v in range(graph.V)]

        # Pilha: cada elemento é (vértice, aresta usada para chegar nele)
        # A aresta é None para o vértice inicial
        stack = deque()
        circuit = deque()  # circuito final (vértices e arestas)

        # Começa pelo vértice 0
        stack.append((0, None))

        while stack:
            v, edge_to_v = stack[-1]
            if adj_iter[v] < len(adj_lists[v]):
                # Ainda há arestas não visitadas saindo de v
                edge = adj_lists[v][adj_iter[v]]
                adj_iter[v] += 1
                stack.append((edge.to_vertex(), edge))
            else:
                # Todas as arestas de v foram visitadas
                stack.pop()
                circuit.appendleft((v, edge_to_v))

        # circuit agora contém pares (vértice, aresta_que_leva_ao_vértice)
        # O primeiro elemento tem aresta None (ponto de partida)
        vertices = [item[0] for item in circuit]
        edges = [item[1] for item in circuit if item[1] is not None]

        # Verifica se todas as arestas foram usadas
        if len(edges) != graph.E:
            # Grafo não é fortemente conexo
            self._cycle = None
            self._edges_in_cycle = None
            return

        self._cycle = vertices
        self._edges_in_cycle = edges

        # Calcula o custo total
        self._cost = sum(e.weight() for e in edges)

    def has_eulerian_cycle(self) -> bool:
        """Retorna True se o dígrafo possui um circuito euleriano."""
        return self._cycle is not None

    def cycle(self) -> list:
        """Retorna o circuito euleriano como lista de vértices, ou None."""
        return self._cycle

    def cycle_edges(self) -> list:
        """Retorna o circuito euleriano como lista de arestas, ou None."""
        return self._edges_in_cycle

    def cost(self) -> float:
        """Retorna o custo total do circuito euleriano."""
        return self._cost
