"""
   Execution:    python digraph.py entrada.txt
   Dependencies: directed_edge.py

   Dígrafo ponderado implementado usando listas de adjacência (listas Python).
   Arestas paralelas e self-loops são permitidos.

   Baseado na classe Digraph do algs4-py, adaptado para trabalhar com
   arestas ponderadas (DirectedEdge) no contexto do Problema do Carteiro Chinês.

   % python digraph.py ../dados/entrada_eulerizada.txt
   6 vértices, 17 arestas
   0: 0->2 (20.0)  0->1 (10.0)  0->1 (10.0)
   1: 1->4 (10.0)  1->3 (50.0)
   ...
"""

from directed_edge import DirectedEdge


class Digraph:

    def __init__(self, v=0, **kwargs):
        self.V = v
        self.E = 0
        self.adj = [[] for _ in range(self.V)]
        self._in_degree = [0] * self.V

        if 'file' in kwargs:
            # init a digraph by a file input
            in_file = kwargs['file']
            self.V = int(in_file.readline())
            self.adj = [[] for _ in range(self.V)]
            self._in_degree = [0] * self.V
            E = int(in_file.readline())
            for i in range(E):
                parts = in_file.readline().split()
                v, w, weight = int(parts[0]), int(parts[1]), float(parts[2])
                self.add_edge(DirectedEdge(v, w, weight))

    def __str__(self):
        s = "%d vértices, %d arestas\n" % (self.V, self.E)
        for v in range(self.V):
            adjs = "  ".join(str(e) for e in self.adj[v])
            s += "  %d: %s\n" % (v, adjs)
        return s

    def add_edge(self, edge):
        v = edge.from_vertex()
        self.adj[v].append(edge)
        self._in_degree[edge.to_vertex()] += 1
        self.E += 1

    def out_degree(self, v):
        return len(self.adj[v])

    def in_degree(self, v):
        return self._in_degree[v]

    def is_balanced(self):
        for v in range(self.V):
            if self.in_degree(v) != self.out_degree(v):
                return False
        return True

    def edges(self):
        result = []
        for v in range(self.V):
            for edge in self.adj[v]:
                result.append(edge)
        return result

    def reverse(self):
        R = Digraph(self.V)
        for v in range(self.V):
            for edge in self.adj[v]:
                R.add_edge(DirectedEdge(edge.to_vertex(), edge.from_vertex(), edge.weight()))
        return R


if __name__ == '__main__':
    import sys
    f = open(sys.argv[1])
    g = Digraph(file=f)
    print(g)
