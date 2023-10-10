

class Task:
    def __init__(self, wcet: int, release_time: int):
        self._wcet = wcet
        self._release_time = release_time
        self._start_time = release_time
        self._finish_time = self._start_time + wcet
        self._core = -1

    @property
    def wcet(self) -> int:
        return self._wcet

    @wcet.setter
    def wcet(self, n: int):
        self._wcet = n

    @property
    def start_time(self) -> int:
        return self._start_time

    @start_time.setter
    def start_time(self, n: int):
        self._start_time = n

    @property
    def finish_time(self) -> int:
        return self._finish_time

    @finish_time.setter
    def finish_time(self, n: int):
        self._finish_time = n

    @property
    def core(self) -> int:
        return self._core

    @core.setter
    def core(self, n: int):
        self._core = n
