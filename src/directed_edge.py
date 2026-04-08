"""
Classe que representa uma aresta dirigida com peso.
Baseada na classe DirectedEdge do algs4-py.
"""


class DirectedEdge:
    """Aresta dirigida ponderada de um vértice v para um vértice w."""

    def __init__(self, v: int, w: int, weight: float):
        self._v = v
        self._w = w
        self._weight = weight
        self._used = False  # marca se a aresta já foi usada no circuito

    def from_vertex(self) -> int:
        """Retorna o vértice de origem."""
        return self._v

    def to_vertex(self) -> int:
        """Retorna o vértice de destino."""
        return self._w

    def weight(self) -> float:
        """Retorna o peso da aresta."""
        return self._weight

    def is_used(self) -> bool:
        """Verifica se a aresta já foi utilizada."""
        return self._used

    def set_used(self, used: bool = True):
        """Marca a aresta como utilizada."""
        self._used = used

    def __str__(self) -> str:
        return f"{self._v}->{self._w} ({self._weight:.1f})"

    def __repr__(self) -> str:
        return self.__str__()

    def __lt__(self, other) -> bool:
        return self._weight < other._weight

    def __gt__(self, other) -> bool:
        return self._weight > other._weight
