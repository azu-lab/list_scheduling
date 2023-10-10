from .task import Task

class Node(Task):
    def __init__(self, idx: int, wcet: int, prev: set[int]):
        self._idx = idx
        self._wcet = wcet
        self._prev = prev
        self._release_time = 0
        self._start_time = 0
        self._finish_time = self._start_time + wcet
        self._core = -1

    @property
    def wcet(self) -> int:
        return self._wcet

    @wcet.setter
    def wcet(self, n: int):
        self._wcet = n

    @property
    def prev(self) -> set[int]:
        return self._prev


class Dag:
    def __init__(self, wcets: list[int], edges: list[tuple[int, int]]):
        self._nodes: set[Node] = []
        for i, wcet in enumerate(wcets):
            prev: list[int] = []
            for edge in edges:
                if i == edge[1]:
                    prev.append(edge[0])
            self._nodes.append(Node(i, wcet, set(prev)))

    @property
    def nodes(self) -> list[Node]:
        return self._nodes
